# Methodology

This document describes how analyses in this repository are conducted, what sources are used, and what the limitations of this approach are.

---

## Analytical Approach

Every analysis in this repository is built on open-source intelligence (OSINT). No proprietary tools, sandbox environments, or raw malware samples are used at this stage of the project. This is acknowledged as a limitation and documented explicitly in each analysis.

The goal is not to replicate existing reports. The goal is to synthesize multiple sources, identify inconsistencies, reconstruct operational logic, and map observed behaviors to industry frameworks.

---

## Primary Sources

Sources are evaluated for credibility before use. Preferred sources in order of priority:

1. **Vendor threat intelligence reports** - Mandiant, CrowdStrike, Recorded Future, Secureworks, SentinelOne, Palo Alto Unit 42
2. **Government and institutional reports** - CISA, ENISA, NSA, FBI advisories
3. **Academic and technical research** - Peer-reviewed papers, conference presentations (DEF CON, Black Hat)
4. **CVE databases** - NVD, MITRE CVE
5. **Community intelligence** - VirusTotal, MalwareBazaar, AlienVault OTX (used with caution)

---

## Analysis Process

1. **Collect** - Gather all available sources on the subject
2. **Compare** - Identify where sources agree and where they conflict
3. **Reconstruct** - Build the operational model from the evidence available
4. **Map** - Align observed behaviors to MITRE ATT&CK tactics and techniques
5. **Document limitations** - Explicitly state what could not be verified and why

---

## MITRE ATT&CK Mapping

Every analysis includes a tactics and techniques table mapped to the MITRE ATT&CK framework. Mappings are based on behaviors described in source reports, not inferred.

Format used:

| Tactic | Technique | Technique ID | Source |
|---|---|---|---|

---

## Source Conflict Documentation

When sources disagree on attribution, infection vector, timeline, or behavior, this is documented explicitly in the **Source Analysis** section of each analysis. The goal is not to resolve the conflict artificially but to present the evidence and reason about it.

---

## Limitations of This Repository

- All analyses are based on secondary sources (published reports, advisories). No primary analysis of malware samples is conducted at this stage.
- Attribution claims from source reports are presented with their original caveats, not treated as fact.
- Detection rules (YARA, Sigma) are based on behaviors described in reports and may not have been tested against live samples.
- This is a work in progress. Older analyses may not reflect the current state of a threat.

---

## What Is Out of Scope

- Live malware analysis or reverse engineering (for now)
- Real-time threat feeds
- Penetration testing techniques or offensive tooling
