# Changelog

All additions and updates to this repository are recorded here in reverse chronological order.

---

## [v0.4] - 2026-08-21

### Added
- `analysis/labs/wazuh-siem-attempt.md`: documents a Wazuh SIEM deployment attempt, the working remote syslog configuration achieved, and the host hardware constraint (8GB RAM) that led to deferring it

### Updated
- ROADMAP.md: Hands-On Labs section reflects the Sigma rule and the deferred SIEM attempt

---

## [v0.3] - 2026-08-20

### Added
- Hands-on labs track (`analysis/labs/`): scope, ground rules, and exercise template
- Metasploitable2 lab environment documentation (`analysis/labs/metasploitable2/00-environment.md`)
- Lab exercise 01: reconnaissance and service enumeration with Nmap
- Lab exercise 02: TCP three-way handshake and Wireshark fundamentals
- Lab exercise 03: vsftpd 2.3.4 backdoor exploitation (CVE-2011-2523)
- First Sigma rule for the lab track, written from exercise 03's log evidence: `detection/sigma/vsftpd-backdoor-connect-review.yml`

### Updated
- README.md: repository structure and a new Hands-On Labs section
- METHODOLOGY.md: scoped the OSINT methodology to exclude `analysis/labs/`, which follows its own primary-research methodology
- ROADMAP.md: added a Hands-On Labs section tracking lab progress

---

## [v0.2] - 2026-06-20

### Added
- WannaCry ransomware analysis (`analysis/malware/ransomware/wannacry.md`)
- WannaCry YARA detection rules (`detection/yara/wannacry.yar`)
- WannaCry Sigma rules for VSS deletion and service creation (`detection/sigma/wannacry-vss-deletion.yml`)

---

## [v0.1] - 2026-06-19

### Added
- Base repository structure
- METHODOLOGY.md
- ROADMAP.md
- Analysis templates: malware, attacks, campaigns, actors
- Detection templates: YARA, Sigma
- IOC template
- Framework reference documents: MITRE ATT&CK, Cyber Kill Chain, Diamond Model, Pyramid of Pain
- Resources and references

---

## Format

```
## [vX.X] - YYYY-MM-DD

### Added
- New analyses, files, or sections

### Updated
- Revised or expanded existing content

### Fixed
- Corrections to errors in previous analyses
```
