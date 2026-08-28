# NIST Cybersecurity Framework (CSF)

> Reference document on the NIST CSF and how it is used in this repository.

---

## What It Is

The NIST Cybersecurity Framework was first published in 2014 and most recently updated to version 2.0 in February 2024. Unlike the Cyber Kill Chain or MITRE ATT&CK, it does not model an attack, it models an organization's cybersecurity posture, organized into six high-level Functions. It is voluntary guidance, not a checklist or compliance standard, meant to give organizations a common vocabulary to describe and communicate their current and target security posture regardless of sector or size.

This is a different kind of framework from the others used in this repository, and it is worth being explicit about that distinction: the Kill Chain and MITRE ATT&CK describe what an *attacker* does, and the Diamond Model and Pyramid of Pain describe how to *analyze* an intrusion once it happens. The CSF describes what a *defending organization* does, on an ongoing basis, independent of any single incident.

---

## The Six Functions

| Function | Description |
|---|---|
| **Govern (GV)** | Establishes and monitors the organization's cybersecurity risk management strategy, expectations, and policy. The newest function, added in version 2.0, made explicit rather than implied across the other five. |
| **Identify (ID)** | Understand the organization's assets, data, systems, and the risks to them, well enough to prioritize effort. |
| **Protect (PR)** | Safeguards to prevent or reduce the likelihood and impact of a cybersecurity event: access control, awareness training, data security, platform and infrastructure hardening. |
| **Detect (DE)** | Timely discovery of cybersecurity events, through continuous monitoring and the analysis of adverse events. |
| **Respond (RS)** | Actions taken once an event is detected, to contain and reduce its impact. |
| **Recover (RC)** | Restoring assets and operations affected by a cybersecurity incident, in a timely manner. |

---

## Strengths and Limitations

**Strengths:**
- Function-based structure maps directly to how a real security program (and its budget, staffing, and tooling) is actually organized, not just to a single incident's timeline
- Vendor- and sector-agnostic, widely recognized outside pure technical audiences, useful for communicating with non-technical stakeholders
- Version 2.0's addition of Govern makes explicit that detection and response controls exist inside an organizational risk decision, not in a vacuum

**Limitations:**
- Deliberately high-level; it says an organization should "Detect" and "Respond", not how, that granularity has to come from elsewhere (MITRE ATT&CK, Sigma/YARA rules, specific vendor controls)
- Describes a continuous posture, not a single event, applying it to one specific historical incident requires translating "what the organization should be doing in general" into "what these specific findings imply about that general posture"
- Adoption and maturity vary enormously between organizations; simply mapping controls to functions says nothing about how well each one is actually implemented

---

## How It Is Used in This Repository

The CSF is used to structure the **Defensive Posture** section of `attacks/` and `malware/` analyses, replacing separate `Detection` and `Mitigation` sections with a single set of Function-based subsections (Identify through Recover, and Govern where relevant). This is a deliberate shift from a narrow "how would I catch this on the wire" scope to a broader "what would an organization's security program need to be doing across its whole lifecycle to handle this threat" scope. It complements MITRE ATT&CK, which still provides the technique-level granularity the CSF itself does not.

It is not used in `analysis/labs/`, where the NIST Incident Response Lifecycle (SP 800-61) is the better fit, since those exercises are single-incident investigations, not general organizational posture assessments.

---

## Resources

- [NIST CSF 2.0 Official Site](https://www.nist.gov/cyberframework)
- [NIST CSF 2.0 Reference Document (NIST CSWP 29)](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
