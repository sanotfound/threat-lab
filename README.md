# Threat Lab

> A structured knowledge base for threat intelligence analysis, focused on understanding how threats operate, not just what they are.

![Status](https://img.shields.io/badge/status-active%20development-blue)
![Methodology](https://img.shields.io/badge/methodology-MITRE%20ATT%26CK%20aligned-red)
![Last Updated](https://img.shields.io/badge/last%20updated-2026-green)

---

## What This Is

Threat Lab is a personal threat intelligence repository built to document, analyze, and map cyber threats using open-source intelligence (OSINT). Each analysis goes beyond surface-level description, focusing on operational models, attack chains, source conflicts, and what remains unverified.

This is a long-term project. It evolves as my technical knowledge deepens.

---

## What This Is Not

This is not a list of threats. It is not a copy of MITRE ATT&CK.  
Every analysis here involves source cross-referencing, explicit mapping to industry frameworks, and documented limitations.

---

## Repository Structure

```
threat-lab/
├── analysis/
│   ├── malware/        # Malware family analysis (ransomware, trojans, worms, etc.)
│   ├── attacks/        # Attack technique analysis (BGP hijacking, SQL injection, etc.)
│   ├── campaigns/      # Threat campaign analysis
│   └── actors/         # Threat actor profiling
├── detection/
│   ├── yara/           # YARA detection rules
│   └── sigma/          # Sigma rules for SIEM
├── intelligence/
│   ├── iocs/           # Indicators of Compromise
│   └── reports/        # Threat intelligence reports and summaries
├── frameworks/         # Reference documents for MITRE ATT&CK, Kill Chain, etc.
├── resources/          # References and useful links
└── .github/            # Issue templates
```

---

## Methodology

All analyses follow a consistent methodology documented in [METHODOLOGY.md](METHODOLOGY.md).

Key principles:
- Every claim is sourced
- Source conflicts are documented explicitly
- MITRE ATT&CK mapping is included in every analysis
- Limitations are always stated

---

## Frameworks Used

| Framework | Purpose |
|---|---|
| [MITRE ATT&CK](frameworks/mitre-attack.md) | Tactic and technique mapping |
| [Cyber Kill Chain](frameworks/cyber-kill-chain.md) | Attack phase structuring |
| [Diamond Model](frameworks/diamond-model.md) | Threat actor relationship modeling |
| [Pyramid of Pain](frameworks/pyramid-of-pain.md) | IOC prioritization |

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned analyses and project milestones.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a dated record of all additions and updates.
