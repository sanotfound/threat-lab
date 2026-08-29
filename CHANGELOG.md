# Changelog

All additions and updates to this repository are recorded here in reverse chronological order.

---

## [v0.6] - 2026-08-29

### Added
- Lab exercise 05: ARP cache poisoning and bidirectional MITM against Metasploitable2 and a new third host, `alpine-endpoint` (192.168.10.40), comparing a naive execution against a properly executed attack, then a defense investigation conducted with no foreknowledge of the attack
- `detection/sigma/arp-cache-poisoning-duplicate-mac.yml`, the second Sigma rule authored from a lab exercise
- `frameworks/nist-csf.md` and `frameworks/intelligence-cycle.md`, two new framework references
- `SKILLS.md`, a capability checklist tracked separately from ROADMAP.md's deliverable list
- `projects/`, a new top-level section for standalone tools, with its own README and TEMPLATE
- ROADMAP.md: new **Independent Projects** section, 14 tools sourced from reviewing an external learning resource, filtered and ordered for this repository's specific goals

### Updated
- `analysis/attacks/TEMPLATE.md` and `analysis/malware/TEMPLATE.md`: `Detection` and `Mitigation` sections replaced with a single `Defensive Posture (NIST CSF)` section
- `analysis/malware/ransomware/wannacry.md`: retrofit to the NIST CSF structure for consistency with the new template
- `METHODOLOGY.md`: Analysis Process now links to `frameworks/intelligence-cycle.md` as the general model it is a specific instance of
- `analysis/labs/metasploitable2/assets/`: reorganized into one subfolder per exercise (`assets/01/` through `assets/05/`), all existing image references updated
- `analysis/labs/metasploitable2/00-environment.md`: documents the third VM, the `LabCyber` network, its hub-like behavior, and the host's RAM constraint
- README.md: repository structure diagram and frameworks table both reflect the additions above
- ROADMAP.md: WannaCry and ARP poisoning/MITM marked complete, Current Focus updated

---

## [v0.5] - 2026-08-22

### Added
- Lab exercise 04: Samba `usermap_script` command execution (CVE-2007-2447), the first exercise fully documented in the new Attack/Defense two-part format
- Attack chapters now structured around the Cyber Kill Chain; Defense chapters around the NIST incident response lifecycle, with findings answering the 5 W's, plus new Containment and Recovery sections

### Updated
- TEMPLATE.md and labs/README.md: formalize the Kill Chain and NIST-based structure, and the convention of embedding evidence inline in the text rather than in a separate section
- ROADMAP.md: Samba exercise marked complete

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
