# [Exercise Name]

> One-line description of what was done and against which service/vulnerability.

![Target](https://img.shields.io/badge/target-metasploitable2-red)
![Complexity](https://img.shields.io/badge/complexity-low%20%2F%20medium%20%2F%20high-orange)

---

## Part 1: Attack

Technical mechanics of the attack itself, executed with full knowledge of what is being done and why.

### Objective

What this part sets out to demonstrate or learn about the attack.

### Reconnaissance

What was discovered prior to this exercise, and how (tool, command, output). Reference the environment's recon file if applicable.

### Execution

Step-by-step account of what was actually run, in order. Include exact commands and relevant output.

| Step | Command / Action | Result |
|---|---|---|
| 1 | | |
| 2 | | |

### MITRE ATT&CK Mapping

| Tactic | Technique | Technique ID |
|---|---|---|
| | | |

### Impact Observed

What was concretely achieved (e.g., shell access, data read, privilege level). Evidence-based only, no speculation about impact beyond what was directly observed.

---

## Part 2: Defense (Threat Hunting)

Investigation conducted from the defender's side, on the same incident, structured as a real triage would be: something prompted a look, and every conclusion is argued from evidence found during this investigation, not from what was already known from Part 1.

### Trigger

The narrative prompt that started the investigation (a report, an observation, a suspicion), not a restatement of what Part 1 already revealed. In this lab, this substitutes for the SIEM/IDS alert a real environment would generate.

### Investigation

Step-by-step account of what was checked, in what order, and why. Each step should be justified by what the previous step's evidence suggested, not by foreknowledge of the attack.

### Findings

What the evidence concretely showed, and the conclusion drawn from it: attack type confirmed, and how confident that conclusion is given what was actually found.

### Detection

What log, network, or host artifact this activity generates in general. Link to a Sigma/YARA rule in `/detection/` if one was written for this exercise.

### Mitigation and Prevention

What configuration, patch, or control would have prevented or limited this.

---

## Evidence

Screenshots/output stored in `assets/`, referenced here.

---

## Notes / Open Questions

Anything unclear, or follow-up worth exploring in a later exercise.
