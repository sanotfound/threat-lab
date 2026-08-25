# Roadmap

This document outlines the planned development of Threat Lab. Priorities shift as the project evolves.

---

## Current Focus

- Establishing base structure and documentation standards
- Writing the first complete malware analysis
- Building YARA rule templates aligned with analyses

---

## Planned Analyses

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
- [ ] Weak/default credential attacks (MySQL, brute force with Hydra)
- [ ] UnrealIRCd backdoor
- [x] ARP poisoning / MITM within the isolated network
- [x] Sigma rule authored from a lab exercise's log evidence
- [x] SIEM (Wazuh) deployment attempted, deferred due to a host hardware constraint. See [wazuh-siem-attempt.md](analysis/labs/wazuh-siem-attempt.md)
- [ ] Correlation-based detection of the vsftpd connect-without-login pattern (contingent on revisiting the SIEM attempt above)

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
