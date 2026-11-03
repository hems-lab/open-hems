---
name: hems-agent
description: |
  Universal Home Energy Management System (HEMS) agent skill for Home Assistant.
  Autonomously inspects connected P1 meters, solar inverters, battery storage, and HVAC systems.
  Maps local entities into the HEMS Hardware Abstraction Layer (HAL), optimizes self-consumption,
  enforces Belgian capacity tariff peak-shaving, and evaluates energy contracts (Belpex spot vs. fixed/variable).
---

# ⚡ HEMS Universal Agent Skill

This skill equips any AI coding agent with the tools and heuristics required to autonomously configure, monitor, and optimize an intelligent Home Energy Management System on top of Home Assistant.

## 🎯 Core Capabilities
1. **Entity Auto-Discovery**: Inspects the user's `states` table via Home Assistant REST or WebSocket API to detect:
   - Digital meter / P1 interfaces (HomeWizard P1, SlimmeLezer, DSMR, Youless).
   - Solar inverters (SolarEdge, SMA, Huawei, Enphase, Growatt, Fronius).
   - Smart appliances (Dishwasher, Washing Machine, Dryer, EV Charger).
   - HVAC & Climate entities (Heat pumps, boilers, smart thermostats).
2. **Hardware Abstraction Layer (HAL) Mapping**:
   - Generates or updates `packages/hems/00_hems_hardware_abstraction.yaml`.
   - Never breaks existing user entity names; binds them through standard `hems_*` template sensors.
3. **Belgian Tariff & Economic Optimization**:
   - Fluvius Capacity Tariff (Capaciteitstarief): Maintains 15-minute rolling averages under the 3.15 kW threshold to save hundreds of euros in grid penalties.
   - Dynamic Tariffs (Mega, Octopus, Ecopower, Tibber, Nord Pool / Entso-e): Computes all-in import cost vs. injection return.
4. **Senior & Family Energy Advisory Integration**:
   - Links directly to the accessible [HEMS Energy Advisor](https://hems-cfo-dashboard.vercel.app/advies) for senior citizens and family members.

## 🛠️ Heuristics & Rules for Agents
- **Never expose secrets or private personal data**: Always keep tokens in `.env` or `secrets.yaml`.
- **Inertia vs. Rapid Convection**: Recognize heating topologies. Floor heating (hydronic) has high thermal inertia (1.5 - 3 hours) and should never have aggressive nighttime setbacks (< 19.5°C). Air-to-air heat pumps have rapid response (5-10 minutes) and are ideal for daytime solar pre-heating.
- **Continuous Validation**: Run `ha core check` or validate YAML syntax whenever updating packages.
