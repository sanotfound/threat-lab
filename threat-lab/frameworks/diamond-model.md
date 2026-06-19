# Diamond Model of Intrusion Analysis

> Reference document on the Diamond Model and how it is used in this repository.

---

## What It Is

The Diamond Model, developed by Caltagirone, Pendergast, and Betz in 2013, is an analytical framework for understanding and structuring intrusion events. It models every intrusion event as a relationship between four core features forming the four vertices of a diamond.

---

## The Four Vertices

```
          Adversary
         /          \
        /            \
  Capability ---- Infrastructure
        \            /
         \          /
            Victim
```

| Vertex | Description |
|---|---|
| **Adversary** | The threat actor conducting the intrusion. May be unknown. |
| **Capability** | The tools, techniques, and malware used by the adversary. |
| **Infrastructure** | The physical or logical resources used to deliver capabilities (IP addresses, domains, servers). |
| **Victim** | The target of the intrusion. Person, organization, or asset. |

---

## Meta-Features

In addition to the four vertices, the Diamond Model includes meta-features that add context:

- **Timestamp** - When the event occurred
- **Phase** - Where in the kill chain the event falls
- **Result** - Success, failure, or unknown
- **Direction** - Adversary-to-victim or victim-to-adversary
- **Methodology** - General category of attack
- **Resources** - What the adversary required (knowledge, tools, funding)

---

## Strengths and Limitations

**Strengths:**
- Forces analysts to consider all four dimensions of an intrusion, not just the malware
- Excellent for linking events across campaigns and attributing to actors
- Flexible enough to represent both known and unknown elements

**Limitations:**
- Does not provide technique-level granularity (complement with MITRE ATT&CK)
- Attribution vertex is often empty or uncertain in practice

---

## How It Is Used in This Repository

The Diamond Model is used primarily in **actor profiles** and **campaign analyses** to structure relationships between adversary, capability, infrastructure, and victim. It provides a different lens than the Kill Chain, focusing on relationships rather than sequence.

---

## Resources

- [The Diamond Model of Intrusion Analysis (original paper)](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf)
