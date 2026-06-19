# Cyber Kill Chain

> Reference document on the Cyber Kill Chain framework and how it is used in this repository.

---

## What It Is

The Cyber Kill Chain was developed by Lockheed Martin in 2011. It models the stages of a cyberattack as a sequential chain, based on the military concept of a kill chain. Breaking any link in the chain disrupts the attack.

---

## The Seven Stages

| Stage | Description |
|---|---|
| **1. Reconnaissance** | The attacker gathers information about the target. Passive (OSINT) or active (scanning). |
| **2. Weaponization** | The attacker creates a deliverable payload combining an exploit with a backdoor or malware. |
| **3. Delivery** | The weapon is transmitted to the target. Email attachment, malicious link, USB, watering hole. |
| **4. Exploitation** | The exploit triggers. A vulnerability in software, hardware, or human behavior is activated. |
| **5. Installation** | The malware installs itself on the target system. Persistence is established. |
| **6. Command and Control (C2)** | The malware establishes a channel back to the attacker for remote control. |
| **7. Actions on Objectives** | The attacker executes their goal. Data exfiltration, ransomware deployment, sabotage. |

---

## Strengths and Limitations

**Strengths:**
- Intuitive and easy to communicate to non-technical stakeholders
- Useful for structuring incident timelines
- Helps identify which defensive controls address which stages

**Limitations:**
- Linear model does not reflect the reality of modern attacks, which are often iterative and non-sequential
- Does not address insider threats well
- Does not provide the granularity of MITRE ATT&CK at the technique level
- Adversary actions inside the network (post-exploitation) are compressed into a single stage

---

## How It Is Used in This Repository

The Kill Chain is used as a secondary structuring tool for **Attack Chain** sections in analyses. It provides a high-level narrative frame, while MITRE ATT&CK provides the technical granularity.

---

## Resources

- [Lockheed Martin - Intelligence-Driven Computer Network Defense](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf)
