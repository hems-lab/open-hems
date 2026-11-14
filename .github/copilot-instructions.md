# GitHub Copilot & AI Agent Instructions — Open HEMS

Welcome! **Open HEMS** is a modular, hardware-agnostic Home Energy Management System for **Home Assistant**.

## Quickstart for AI Agents (Antigravity, Claude Code, GitHub Copilot, Cursor)
1. Read `.agents/skills/hems-agent/SKILL.md` for the full hardware abstraction & discovery workflow.
2. Inspect `packages/hems/`:
   - `00_hems_hardware_abstraction.yaml` — Hardware Abstraction Layer (HAL) aliases
   - `10_hems_capacity_tariff.yaml` — Peak shaving & capacity tariff protection
   - `20_hems_smart_appliances.yaml` — Solar surplus appliance scheduling
3. Use `config/sites/example_site_a.yaml` as a template for multi-site profiles. Copy to `*.local.yaml` (gitignored).

## Strict Security & Anonymity Rules
- **NEVER** commit real names, street addresses, EAN meter numbers, IBANs, Home Assistant URLs, or `HA_TOKEN` values.
- Keep all tokens in `.env` or `secrets.yaml`.
- All PRs and pushes are checked by `.github/workflows/dlp-guard.yml`.
