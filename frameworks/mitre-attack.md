# MITRE ATT&CK

> Reference document on how the MITRE ATT&CK framework is used in this repository.

---

## What It Is

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. It is the primary framework used to structure and contextualize all analyses in this repository.

Official resource: https://attack.mitre.org

---

## Structure

ATT&CK organizes adversary behavior into three levels:

**Tactics** - The adversary's tactical goal. The "why" of an action.  
**Techniques** - How the adversary achieves the tactic. The "how".  
**Sub-techniques** - More specific implementations of a technique.

---

## Tactics (Enterprise Matrix)

| ID | Tactic | Description |
|---|---|---|
| TA0001 | Initial Access | Getting into the network |
| TA0002 | Execution | Running malicious code |
| TA0003 | Persistence | Maintaining foothold |
| TA0004 | Privilege Escalation | Gaining higher permissions |
| TA0005 | Defense Evasion | Avoiding detection |
| TA0006 | Credential Access | Stealing credentials |
| TA0007 | Discovery | Exploring the environment |
| TA0008 | Lateral Movement | Moving through the network |
| TA0009 | Collection | Gathering data of interest |
| TA0010 | Exfiltration | Stealing data |
| TA0011 | Command and Control | Communicating with compromised systems |
| TA0040 | Impact | Manipulating, interrupting, or destroying systems |

---

## How It Is Used in This Repository

Every analysis includes a **MITRE ATT&CK Mapping** table in this format:

| Tactic | Technique | Technique ID | Source |
|---|---|---|---|
| Initial Access | Phishing: Spearphishing Attachment | T1566.001 | [Source] |

Mappings are based only on behaviors explicitly described in source reports. Inferred techniques are noted as such.

---

## Resources

- [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) - Visual layer for mapping techniques
- [ATT&CK Matrix for Enterprise](https://attack.mitre.org/matrices/enterprise/)
- [ATT&CK for ICS](https://attack.mitre.org/matrices/ics/)
