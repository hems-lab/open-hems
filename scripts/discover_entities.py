#!/usr/bin/env python3
"""
HEMS Lab — Entity Auto-Discovery & Mapping Tool
Scans Home Assistant states to automatically detect P1 digital meters,
solar inverters, gas meters, and smart plugs.
"""

import sys
import os
import json
import urllib.request

HA_URL = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

def fetch_states():
    if not HA_TOKEN:
        print("⚠️  HA_TOKEN environment variable not set. Please set your Long-Lived Access Token.")
        print("   Usage: HA_TOKEN='your_token' python3 scripts/discover_entities.py")
        sys.exit(1)

    req = urllib.request.Request(
        f"{HA_URL}/api/states",
        headers={
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json",
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"❌ Error connecting to Home Assistant at {HA_URL}: {e}")
        sys.exit(1)

def discover():
    states = fetch_states()
    print(f"🔍 Analyzing {len(states)} entities in Home Assistant...")

    discovered = {
        "p1_active_power": None,
        "solar_power": None,
        "gas_today": None,
        "quarter_peak": None,
    }

    for entity in states:
        entity_id = entity.get("entity_id", "")
        attrs = entity.get("attributes", {})
        dev_class = attrs.get("device_class")

        # P1 Active Power
        if any(k in entity_id for k in ["p1", "dsmr", "active_power", "grid_power"]) and dev_class == "power":
            if not discovered["p1_active_power"]:
                discovered["p1_active_power"] = entity_id

        # Solar Power
        if any(k in entity_id for k in ["solaredge", "solar", "inverter", "pv", "growatt", "huawei", "enphase"]) and dev_class == "power":
            if not discovered["solar_power"] and entity_id != discovered["p1_active_power"]:
                discovered["solar_power"] = entity_id

        # Gas
        if dev_class == "gas" or "gas" in entity_id:
            if not discovered["gas_today"] and "vandaag" in entity_id or "today" in entity_id:
                discovered["gas_today"] = entity_id

        # Peak demand
        if "peak" in entity_id and any(k in entity_id for k in ["quarter", "demand", "kwartier"]):
            discovered["quarter_peak"] = entity_id

    print("\n✅ Auto-Discovery Results:")
    for k, v in discovered.items():
        print(f"  • {k:20}: {v or 'Not detected (configure manually)'}")

    print("\n💡 Copy these entity names into `packages/hems/00_hems_hardware_abstraction.yaml` to complete setup.")

if __name__ == "__main__":
    discover()
