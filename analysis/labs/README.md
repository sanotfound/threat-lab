# Labs

This section documents hands-on exercises conducted in a private, isolated lab environment, as opposed to the rest of `analysis/`, which is built on OSINT synthesis of third-party reports (see [METHODOLOGY.md](../../METHODOLOGY.md)).

---

## Scope and Ground Rules

- All activity documented here is conducted against systems I own and control, running in an isolated virtual network with no internet-facing exposure.
- The target systems are intentionally vulnerable training platforms (e.g., Metasploitable2), designed for this exact purpose.
- The goal is **not** offensive skill-building for its own sake. Every exercise is written up with equal or greater emphasis on **detection and mitigation** than on exploitation itself.
- No techniques documented here are applied to systems outside this lab.

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

Each exercise follows the same structure (see [TEMPLATE.md](TEMPLATE.md)):

1. **Reconnaissance**: what was discovered and how
2. **Execution**: how the attack/technique was carried out, step by step
3. **MITRE ATT&CK Mapping**: tactic, technique, ID
4. **Impact Observed**: what was actually achieved, with evidence
5. **Detection**: what artifacts this leaves and how to catch it (Sigma/YARA where applicable)
6. **Mitigation and Prevention**: how this is prevented or hardened against

---

## Relationship to Main Analyses

Findings here may later feed into a full `analysis/attacks/` or `analysis/malware/` writeup once cross-referenced with public sources, per the standard methodology. Lab notes themselves are primary research and are not held to the multi-source verification standard used elsewhere in this repository.
