# Roadmap

This document outlines the planned development of Threat Lab. Priorities shift as the project evolves.

---

## Current Focus

- Base structure and documentation standards established
- First complete malware analysis (WannaCry) and first complete hands-on lab arc (Metasploitable2, exercises 01-06) done
- Building YARA rule templates aligned with analyses

---

## Planned Analyses

These are not ordered by relation to hands-on practice, see [METHODOLOGY.md](METHODOLOGY.md#relationship-to-hands-on-practice) for how the analyses below and the practice in `analysis/labs/`/`projects/` actually relate.

### Malware

- [x] WannaCry (Ransomware)
- [ ] NotPetya (Wiper/Ransomware)
- [ ] Emotet (Trojan/Loader)
- [ ] Stuxnet (Worm)
- [ ] Mirai (Botnet)

### Attacks

- [ ] BGP Hijacking
- [ ] SQL Injection
- [ ] DNS Spoofing
- [ ] ARP Poisoning
- [ ] Supply Chain Attack

### Actors

- [ ] Lazarus Group
- [ ] APT28 (Fancy Bear)
- [ ] Sandworm

### Campaigns

- [ ] Operation Aurora
- [ ] SolarWinds (SUNBURST)

---

## Hands-On Labs

Practical exercises conducted in an isolated Kali Linux and Metasploitable2 lab, documented in `analysis/labs/`. See [analysis/labs/README.md](analysis/labs/README.md) for scope and format.

### Metasploitable2

- [x] Reconnaissance and service enumeration (Nmap)
- [x] TCP three-way handshake and Wireshark fundamentals
- [x] vsftpd 2.3.4 backdoor exploitation (CVE-2011-2523)
- [x] Samba `usermap_script` RCE (CVE-2007-2447)
- [ ] distccd unauthenticated RCE (CVE-2004-2687)
- [x] SSH password brute force with Hydra against a weak credential (exercise 06), log evidence feeds the SSH Brute Force Detector project below
- [ ] MySQL weak/default credential access
- [ ] UnrealIRCd backdoor
- [x] ARP poisoning / MITM within the isolated network
- [x] Sigma rule authored from a lab exercise's log evidence
- [x] SIEM (Wazuh) deployment attempted, deferred due to a host hardware constraint. See [wazuh-siem-attempt.md](analysis/labs/wazuh-siem-attempt.md)
- [ ] Correlation-based detection of the vsftpd connect-without-login pattern (contingent on revisiting the SIEM attempt above)

---

## Independent Projects

Standalone tools, separate from the OSINT analyses and the Metasploitable2 lab arc, chosen to close specific gaps tracked in [SKILLS.md](SKILLS.md) or to build first-hand understanding ahead of writing a planned analysis above. Candidates sourced from reviewing [CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects), filtered down to the ones that build a Threat Intelligence & Hunting relevant skill, offensive/exploit-development-focused projects from that list were deliberately excluded. Ordered by suggested execution sequence, not by the source repository's own tiering.

**Phase 1: quick builds, fit a short morning session**

- [x] DNS Lookup CLI Tool
- [ ] SSH Brute Force Detector
- [ ] Systemd Persistence Scanner
- [ ] DNS Sinkhole

**Phase 2: same tier, technically heavier, better suited to a longer block**

- [ ] Canary Token Generator
- [ ] Linux eBPF Security Tracer

**Phase 3: OSINT/CTI collection tooling**

- [ ] Security News Scraper (automates the Collection phase of [frameworks/intelligence-cycle.md](frameworks/intelligence-cycle.md))
- [ ] Subdomain Takeover Scanner

**Phase 4: heavier analysis and detection**

- [ ] Secrets Scanner
- [ ] JA3/JA4 TLS Fingerprinting Tool
- [ ] Binary Analysis Tool (closes the "malware analysis basics" gap in SKILLS.md; scoped deliberately light: string extraction, file type/packing identification, flagging suspicious API calls via a decompiler's higher-level output, not manual raw-assembly reading)

**Phase 5: builds first-hand understanding ahead of a planned Attacks analysis above**

- [ ] Supply Chain Attack Simulator (do before writing the Supply Chain Attack analysis)
- [ ] SBOM Generator & Vulnerability Matcher

**Phase 6: log analysis and correlation, closes the SIEM gap in SKILLS.md**

- [ ] Pandas-based log analysis warm-up (no dedicated repo tooling, practice project): re-analyze existing lab artifacts (e.g. the ARP poisoning capture from [lab exercise 05](analysis/labs/metasploitable2/05-arp-poisoning-mitm.md), exported to CSV) or a sample auth log, using Pandas to filter, group, and spot patterns programmatically instead of manually. Deliberately scoped smaller than the SIEM Dashboard below, first hands-on contact with Pandas before adding a full-stack app on top of it.
- [ ] SIEM Dashboard

---

## Planned Improvements

- [ ] Add sandbox analysis to existing reports (as technical skills develop)
- [ ] Test and validate YARA rules against public sample repositories
- [ ] Add Sigma rules for each malware analysis
- [ ] Develop IOC tracking with structured format (STIX 2.1)
- [ ] GitHub Actions for automated rule validation

---

## Long-term Vision

This repository is designed to grow alongside my technical development in threat intelligence. As skills in dynamic analysis, reverse engineering, and detection engineering develop, analyses will be updated to reflect primary research rather than secondary source synthesis only.
