# [Exercise Name]

> One-line description of what was done and against which service/vulnerability.

![Target](https://img.shields.io/badge/target-metasploitable2-red)
![Complexity](https://img.shields.io/badge/complexity-low%20%2F%20medium%20%2F%20high-orange)

---

## Part 1: Attack

Technical mechanics of the attack itself, executed with full knowledge of what is being done and why, structured around the Cyber Kill Chain (see [frameworks/cyber-kill-chain.md](../../frameworks/cyber-kill-chain.md)). Embed evidence screenshots inline, right at the step or claim they support, rather than collecting them in a separate section at the end.

### Objective

What this part sets out to demonstrate or learn about the attack.

### Reconnaissance

What was discovered prior to this exercise, and how (tool, command, output). Reference the environment's recon file if applicable.

### Weaponization

How the specific exploit/tool was selected and prepared, and why, based on what reconnaissance revealed.

### Delivery

How the exploit was sent to the target.

### Exploitation

The moment the vulnerability was actually triggered, and what happened as a direct result.

### Installation

Any persistence established (backdoor accounts, scheduled tasks, added keys), if applicable to this exercise.

### Command and Control

The channel used to communicate with or control the compromised system going forward, if applicable.

### Actions on Objectives

What the attacker ultimately achieved or demonstrated.

### MITRE ATT&CK Mapping

| Tactic | Technique | Technique ID |
|---|---|---|
| | | |

### Impact Observed

What was concretely achieved (e.g., shell access, data read, privilege level). Evidence-based only, no speculation about impact beyond what was directly observed.

---

## Part 2: Defense (Threat Hunting)

Investigation conducted from the defender's side, on the same incident, structured as a real triage would be: something prompted a look, and every conclusion is argued from evidence found during this investigation, not from what was already known from Part 1. Follows the general shape of the NIST incident response lifecycle. Embed evidence screenshots inline, right where they support the point being made, not collected separately.

### Trigger

The narrative prompt that started the investigation (a report, an observation, a suspicion), not a restatement of what Part 1 already revealed. In this lab, this substitutes for the SIEM/IDS alert a real environment would generate.

### Investigation

Step-by-step account of what was checked, in what order, and why. Each step should be justified by what the previous step's evidence suggested, not by foreknowledge of the attack.

### Findings

What the evidence concretely showed, and the conclusion drawn from it, answering the 5 W's directly:

- **Who**: source of the activity (IP, account involved)
- **What**: the type of attack and actions taken
- **Where**: which service, host, or system was affected
- **Why**: the vulnerability or misconfiguration that made this possible
- **When**: timeline reconstructed from evidence

State how confident each conclusion is given what was actually found.

### Containment

How the incident would be (or was) contained: what would be disabled, isolated, or blocked to stop it from continuing or spreading. Name the naive first response most people reach for (e.g., blocking a single IP) and explain concretely why it is temporary or insufficient, before presenting the measure that actually closes the exploitation path rather than reacting to one instance of it.

### Recovery

What would be done to reverse the damage and restore a trustworthy state: accounts to remove, systems to patch or rebuild, credentials to rotate.

### Detection

What log, network, or host artifact this activity generates in general. Link to a Sigma/YARA rule in `/detection/` if one was written for this exercise.

### Mitigation and Prevention

What configuration, patch, or control would have prevented or limited this, directly answering what could have been different.

---

## Conclusion

Synthesizes both parts using frameworks not already applied above (MITRE ATT&CK and the Cyber Kill Chain are used in Part 1, the NIST-style lifecycle in Part 2). Do not repeat findings already stated, reframe the incident through a different analytical lens instead.

### Diamond Model

Adversary, capability, infrastructure, and victim for this incident (see [frameworks/diamond-model.md](../../frameworks/diamond-model.md)), and the relationships between them.

### Pyramid of Pain

Rank the indicators uncovered during the investigation (hashes, IPs, domains, host/network artifacts, tools, TTPs, see [frameworks/pyramid-of-pain.md](../../frameworks/pyramid-of-pain.md)) by how much difficulty or cost denying each one actually imposes on the attacker. Connect this back to why some of the containment or mitigation choices above are durable and others are not.

---

## Notes / Open Questions

Anything unclear, or follow-up worth exploring in a later exercise.
