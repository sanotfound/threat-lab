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

**This is not** a list of threats. **It is not a copy** of MITRE ATT&CK.  
Every analysis here involves source cross-referencing, explicit mapping to industry frameworks, and documented limitations.

---

## Repository Structure

```
threat-lab/
├── analysis/
│   ├── malware/        # Malware family analysis (ransomware, trojans, worms, etc.)
│   ├── attacks/        # Attack technique analysis (BGP hijacking, SQL injection, etc.)
│   ├── campaigns/      # Threat campaign analysis
│   ├── actors/         # Threat actor profiling
│   └── labs/           # Hands-on exercises in an isolated personal lab (Kali + Metasploitable2)
├── detection/
│   ├── yara/           # YARA detection rules
│   └── sigma/          # Sigma rules for SIEM
├── intelligence/
│   ├── iocs/           # Indicators of Compromise
│   └── reports/        # Threat intelligence reports and summaries
├── frameworks/         # Reference documents for MITRE ATT&CK, Kill Chain, etc.
├── projects/           # Standalone tools built to close specific skill gaps
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

## How Practice and Analysis Relate

This repository has two kinds of work: OSINT-based analyses (`analysis/malware/`, `attacks/`, `campaigns/`, `actors/`) built from published, secondary sources, and hands-on practice (`analysis/labs/`, `projects/`) done firsthand against systems I own and control, in a private, isolated virtual lab (Kali Linux and Metasploitable2) or as standalone tools.

Practice is not scoped to match each analysis one-to-one. Its purpose is building real technical grounding, how an operating system actually behaves under the hood (processes, memory, the filesystem) and how network and protocol communication actually happens. Some of the most significant threats documented here (a destructive wiper like NotPetya, for instance) are neither ethical nor sensible to rebuild just to study firsthand, and there is no intention of ever doing so. Where a lab exercise or project happens to study the same technique an analysis later covers (see [ARP poisoning](analysis/labs/metasploitable2/05-arp-poisoning-mitm.md), for one), that overlap is a bonus, not a requirement for the analysis to exist.

Any offensive technique practiced hands-on here, in the labs specifically, is practiced for exactly one reason: understanding what it affects and how, well enough to reason about detection and mitigation. Each lab exercise takes a purple team approach for this reason, pairing the offensive technique with an equal or greater focus on the defensive side. Building new offensive capability (malware, exploits, tooling meant to attack rather than to understand) is out of scope here, regardless of how technically interesting it might be, and every tool used is a legitimate, widely-taught IT/security tool applied only against systems I own and control.

See [analysis/labs/README.md](analysis/labs/README.md) for the scope, ground rules, and format of the hands-on exercises, and [METHODOLOGY.md](METHODOLOGY.md) for how the OSINT-based analyses are conducted.

---

## Frameworks Used

| Framework | Purpose |
|---|---|
| [MITRE ATT&CK](frameworks/mitre-attack.md) | Tactic and technique mapping |
| [Cyber Kill Chain](frameworks/cyber-kill-chain.md) | Attack phase structuring |
| [Diamond Model](frameworks/diamond-model.md) | Threat actor relationship modeling |
| [Pyramid of Pain](frameworks/pyramid-of-pain.md) | IOC prioritization |
| [NIST CSF](frameworks/nist-csf.md) | Organizational defensive posture, `attacks/` and `malware/` analyses |
| [Intelligence Cycle](frameworks/intelligence-cycle.md) | The analysis process itself (see METHODOLOGY.md) |

---

## Roadmap

See [ROADMAP.md](ROADMAP.md) for planned analyses and project milestones.

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a dated record of all additions and updates.
