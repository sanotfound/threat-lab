# Pyramid of Pain

> Reference document on the Pyramid of Pain and how it is used in this repository.

---

## What It Is

The Pyramid of Pain, created by David Bianco in 2013, describes the relationship between types of indicators of compromise (IOCs) and how much pain it causes an adversary when defenders detect and respond to those indicators.

The higher the indicator on the pyramid, the harder it is for the attacker to change it.

---

## The Pyramid

```
        /\
       /  \         TTPs              <- Most painful for adversary
      /----\
     /      \       Tools
    /--------\
   /          \     Network Artifacts
  /------------\
 /              \   Host Artifacts
/----------------\
/                  \ Domain Names
/--------------------\
        Hash Values  <- Least painful for adversary
```

---

## Levels Explained

| Level | Examples | Pain for Adversary |
|---|---|---|
| **Hash Values** | MD5, SHA1, SHA256 of malware files | Trivial - change one byte, hash changes |
| **IP Addresses** | C2 server IPs | Easy - switch hosting provider |
| **Domain Names** | C2 domains, phishing domains | Simple - register a new domain |
| **Network Artifacts** | User-agent strings, URI patterns, protocol quirks | Annoying - requires changing tooling |
| **Host Artifacts** | Registry keys, file paths, mutex names | Annoying - requires changing implant behavior |
| **Tools** | Specific malware families, exploit frameworks | Challenging - requires developing or buying new tools |
| **TTPs** | Tactics, Techniques, and Procedures (MITRE ATT&CK) | Extremely painful - requires changing entire methodology |

---

## Implications for Detection

Detections built on file hashes are easily bypassed. Detections built on TTPs are resilient. This is why this repository prioritizes:

1. Behavioral detection (Sigma rules based on TTPs)
2. YARA rules based on code patterns and artifacts rather than hashes alone
3. MITRE ATT&CK mapping in every analysis

---

## How It Is Used in This Repository

The Pyramid of Pain informs **IOC documentation** and **detection rule design**. When documenting IOCs, each indicator is categorized by its level on the pyramid. This communicates the operational value of each indicator to defenders.

---

## Resources

- [The Pyramid of Pain - David Bianco](http://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
