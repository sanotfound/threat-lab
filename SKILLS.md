# Skills Checklist

A living checklist of the capabilities a Threat Intelligence & Hunting professional needs, independent of any single piece of work in this repository. The point of tracking this separately from [ROADMAP.md](ROADMAP.md) is that ROADMAP.md tracks *deliverables* (which analysis, which lab exercise), this tracks *capabilities*, several deliverables can exercise the same skill, and a skill can be worth developing even outside of any planned deliverable.

Status for each item reflects an honest read of what this repository's existing work actually exercises, not aspiration. `covered` means real, repeated practice exists. `partial` means it has been touched but not deliberately practiced. `gap` means it has not been exercised at all yet.

Skill categories originally sourced from reviewing an external, unaffiliated learning resource ([CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects), `ROADMAPS/THREAT-INTELLIGENCE-ANALYST.md`), adapted to this repository's own scope and reworded, not copied verbatim.

---

## Technical Skills

| Skill | Status | Where |
|---|---|---|
| Network analysis (Wireshark, tcpdump) | covered | Labs 02, 05 |
| Threat modeling frameworks | covered | `frameworks/` (six frameworks applied across analyses and labs) |
| Malware analysis basics | partial | `wannacry.md` is OSINT synthesis, not original dynamic/static analysis |
| Indicator enrichment and validation | covered | Source Analysis sections evaluate *reported* IOCs; `projects/dns-lookup-cli/` now adds live re-verification of a domain indicator (DNS + WHOIS state) |
| SIEM platforms (Splunk, ELK, QRadar) | partial | Wazuh attempted and deferred, see `analysis/labs/wazuh-siem-attempt.md` |
| Zeek | gap | |
| Threat intelligence platforms (MISP, ThreatConnect, Anomali) | gap | |
| OSINT tooling (Maltego, Shodan, TheHarvester) | gap | |
| Scripting (Python for automation) | covered | `projects/dns-lookup-cli/`|

## Analytical Skills

| Skill | Status | Where |
|---|---|---|
| Critical thinking | covered | Recurring throughout, e.g. catching an unsourced claim before it entered `wannacry.md`, verifying the MITRE Shield/Engage status before recommending a framework |
| Pattern recognition | covered | Lab 05 defense investigation, identifying the ARP anomaly from raw `tcpdump` output |
| Hypothesis development and testing | covered | Source Analysis sections; lab 05's investigation ruled out two methods before choosing one, with stated reasoning |
| Data correlation | covered | Lab 05, correlating the ARP anomaly against the specific FTP session via link-layer addresses |
| Attribution analysis | partial | `wannacry.md` evaluates *others'* attribution arguments, has not yet built an original attribution case from raw evidence |
| Strategic thinking | partial | Present in NIST CSF work; not yet exercised by an `actors/` or `campaigns/` piece |
| Trend analysis | gap | Nothing in the repo yet looks at a threat's evolution over time |

## Communication Skills

| Skill | Status | Where |
|---|---|---|
| Technical documentation | covered | The whole repository |
| Intelligence report writing | covered | Every analysis and lab exercise |
| Executive briefings | partial | Executive Summary sections exist in every template, never validated against an actual non-technical reader |
| Information sharing (structured IOC formats) | gap | STIX 2.1 already planned in `ROADMAP.md`, not started |
| Stakeholder communication (multi-audience framing) | gap | Everything so far has one implicit audience (a technical recruiter) |

---

## Intelligence Types

Not a skill, a lens for classifying the *kind* of output being produced. Worth naming because it already maps cleanly onto this repository's existing structure, even though that mapping was not deliberate until now:

| Type | Focus | Maps to |
|---|---|---|
| Strategic | Long-term trends, actor capability and intent, industry landscape | `analysis/actors/` |
| Operational | Campaign tracking, TTPs, infrastructure, medium-term planning | `analysis/campaigns/` |
| Tactical | IOCs, signatures, attack patterns, immediate response | `analysis/malware/`, `analysis/attacks/` |

---

## Notes

- This file should be revisited periodically, not just written once. A skill moving from `gap` to `partial` to `covered` is itself worth noticing.
- Some `gap` items (Python scripting, structured IOC sharing) are already independently planned in `ROADMAP.md`. Others (OSINT tooling, threat intel platforms) are not yet planned anywhere and may be worth converting into an actual roadmap item rather than staying an abstract gap.
