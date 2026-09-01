# Labs

This section documents hands-on exercises conducted in a private, isolated lab environment, as opposed to the rest of `analysis/`, which is built on OSINT synthesis of third-party reports (see [METHODOLOGY.md](../../METHODOLOGY.md)).

---

## Scope and Ground Rules

- All activity documented here is conducted against systems I own and control, running in an isolated virtual network with no internet-facing exposure.
- The target systems are intentionally vulnerable training platforms (e.g., Metasploitable2), designed for this exact purpose.
- The goal is **not** offensive skill-building for its own sake. Every exercise is written up with equal or greater emphasis on **detection and mitigation** than on exploitation itself.
- No techniques documented here are applied to systems outside this lab.

---

## Why the Target Systems Are Old

Metasploitable2 ships vulnerabilities from 2007-2011. That age is not a limitation on relevance: the specific CVE is old, the mechanism behind it is not. Command injection, weak credential policy, cryptographic downgrade, ARP cache poisoning, none of these have expiration dates, they keep showing up in current systems under different names. Legacy systems nobody can afford to take fully offline (industrial control, healthcare, government) are a permanent, current fixture of real environments, not a historical footnote, and recognizing and handling that is itself a live skill, not a nostalgia exercise. Practicing against an old target also forces engagement with fundamentals a newer, more abstracted system might paper over, the same reason hands-on practice exists at all (see [METHODOLOGY.md](../../METHODOLOGY.md#relationship-to-hands-on-practice)).

---

## On Dual-Use Tools

Nearly every tool used in this section (Nmap, Metasploit, Wireshark, etc.) is a legitimate, widely-taught IT/security tool with everyday defensive uses: asset inventory, firewall auditing, compliance scanning, troubleshooting, authorized penetration testing. None of them are illegal or restricted to use.

What makes an action legitimate or not is not the tool, it's **authorization**. Running these tools against systems you own or are explicitly authorized to test (as is the case here) is lawful; running them against systems you do not have permission to test is not, regardless of intent. Every exercise in this section is scoped exclusively to the isolated lab described in `00-environment.md`.

---

## Structure

Each target environment gets its own folder (e.g., `metasploitable2/`). Inside:

- `00-environment.md`: network topology, IPs, and lab setup
- `NN-exercise-name.md`: one file per exercise, numbered sequentially in the order performed
- `assets/`: supporting screenshots/evidence for that environment's exercises

---

## Exercise Format

Starting with the exercises that follow the vsftpd backdoor (03), each new exercise is split into two parts (see [TEMPLATE.md](TEMPLATE.md)):

**Part 1: Attack.** Technical mechanics, executed with full knowledge of what is being done, structured around the Cyber Kill Chain (reconnaissance, weaponization, delivery, exploitation, installation, command and control, actions on objectives), plus MITRE ATT&CK mapping and impact observed.

**Part 2: Defense (Threat Hunting).** The same incident investigated from the defender's side, structured as a real triage would be, following the shape of the NIST incident response lifecycle. A narrative trigger (a report, an observation) stands in for the SIEM/IDS alert this lab does not have, and every conclusion is argued from evidence found during the investigation, not from what Part 1 already revealed. Findings answer the 5 W's (who, what, where, why, when) directly. Containment sections name the naive first response (e.g., blocking a single IP) and explain why it falls short before presenting what actually closes the exploitation path. This section closes with recovery, detection artifacts, and mitigation/prevention.

**Conclusion.** Synthesizes both parts using whichever of this repo's frameworks were not already applied above, typically the Diamond Model and the Pyramid of Pain, without repeating findings already stated.

Earlier exercises (01, 02) predate this format and remain single-flow.

Evidence screenshots are embedded inline, at the point in the text they support, rather than collected in a separate section at the end. Exercises 01 through 03 predate this convention and still use a standalone Evidence section.

---

## Relationship to Main Analyses

Findings here may later feed into a full `analysis/attacks/` or `analysis/malware/` writeup once cross-referenced with public sources, per the standard methodology. Lab notes themselves are primary research and are not held to the multi-source verification standard used elsewhere in this repository.
