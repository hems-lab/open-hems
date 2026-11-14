# 🎬 Open HEMS — Video Walkthrough & Quickstart Script (5 Minutes)

Use this script to record a community quickstart video for YouTube / Home Assistant Community Forum.

## 0:00 – 0:45 | The Problem & Vision
- **Visual**: Show a typical Home Assistant energy dashboard with vendor-locked automations.
- **Narration**: "Most Home Assistant energy automations break the moment you swap an inverter, smart plug, or heat pump. Open HEMS fixes that with a clean Hardware Abstraction Layer (HAL) and an AI Agent Skill."

## 0:45 – 2:00 | Architecture Overview
- **Visual**: Open `packages/hems/` in VS Code / Antigravity:
  - `00_hems_hardware_abstraction.yaml`
  - `10_hems_capacity_tariff.yaml`
  - `20_hems_smart_appliances.yaml`
- **Narration**: "You only map your physical entities once in `00_hems_hardware_abstraction.yaml`. Everything else—peak shaving and solar surplus dispatching—runs on standardized `hems_*` aliases."

## 2:00 – 3:30 | AI Agent Auto-Mapping Demo
- **Visual**: Run `scripts/discover_entities.py` (with `HA_TOKEN` in env, never hardcoded) and invoke the AI agent using `.agents/skills/hems-agent/SKILL.md`.
- **Narration**: "Whether you use Google Antigravity, Claude Code, GitHub Copilot, or Cursor, the included `SKILL.md` teaches your agent how to discover your Home Assistant entities and wire up Open HEMS in minutes."

## 3:30 – 4:30 | Multi-Site & Privacy Best Practices
- **Visual**: Show `config/sites/example_site_a.yaml` and `.github/workflows/dlp-guard.yml`.
- **Narration**: "Always copy example profiles to `*.local.yaml` so your address, EANs, and tokens stay private."

## 4:30 – 5:00 | Call to Action
- **Visual**: `https://github.com/hems-lab/open-hems` & Home Assistant Community thread.
- **Narration**: "Star the repo, open an issue for your region's tariff rules, and share your setup!"
