# Security Policy

## Reporting a Vulnerability
If you discover a security vulnerability, credential leak, or privacy issue in Open HEMS, please open a **GitHub Security Advisory** (Private Vulnerability Reporting) or contact the maintainers before disclosing publicly.

## Credential & Privacy Best Practices
- Never commit `.env`, `secrets.yaml`, or personal `config/sites/*.yaml` files (only `example_*.yaml` templates belong in version control).
- Use a dedicated Home Assistant Long-Lived Access Token with minimal scope and rotate it if ever exposed.
- When using cloud AI coding assistants, avoid pasting personal entity histories, street addresses, or EAN meter numbers.
