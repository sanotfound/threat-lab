# The Intelligence Cycle

> Reference document on the Intelligence Cycle and how it is used in this repository.

---

## What It Is

The Intelligence Cycle is the classic model, adapted from traditional (military and government) intelligence tradecraft, describing how raw information becomes finished, actionable intelligence. It predates cybersecurity entirely and is not specific to it, threat intelligence is one of many domains that adopted it. Unlike the Cyber Kill Chain or MITRE ATT&CK, it does not describe what an attacker does, and unlike the Diamond Model or Pyramid of Pain, it does not describe how to analyze an intrusion. It describes the **production process** an analyst follows to turn scattered sources into something a reader can act on.

---

## The Six Phases

| Phase | Description |
|---|---|
| **1. Direction (Planning)** | Defining what question is actually being answered and why, before collecting anything. Without this, collection has no way to know when it has enough. |
| **2. Collection** | Gathering raw information from sources, prioritized by credibility (see [METHODOLOGY.md](../METHODOLOGY.md)'s source priority list). |
| **3. Processing** | Converting raw collected material into a usable, comparable form, filtering out what is not relevant or not credible enough to use. |
| **4. Analysis** | Comparing sources, identifying agreement and conflict, reconstructing the operational logic, and mapping it to established frameworks. This is where interpretation happens, not before it. |
| **5. Dissemination** | Delivering the finished analysis to whoever needs it, in a form suited to them (a technical report is not the same document as an executive summary of the same finding). |
| **6. Feedback** | Whether the finished product actually answered the original question from Direction, and what that implies for the next cycle. |

---

## Strengths and Limitations

**Strengths:**
- Forces a clear separation between *collecting* information and *interpreting* it, a common failure mode is treating a single source's claim as already-analyzed conclusion
- Explicitly includes Feedback, most technical frameworks in this repository describe a single pass and have no notion of revisiting or correcting a finished product
- Domain-agnostic; the same six phases describe how a SOC analyst, a journalist, or a government intelligence officer actually works

**Limitations:**
- Describes an idealized, mostly linear sequence; real analysis loops back constantly (a Processing-stage discovery routinely sends the analyst back to Collection)
- Says nothing about *what* to look for or *how* to structure the finished analysis, it is a process model, not a content model, which is why it is paired with MITRE ATT&CK and the other frameworks in this repository rather than used alone
- Originates from a context (state intelligence services) with very different stakes, resourcing, and classification concerns than an open-source security researcher has

---

## How It Is Used in This Repository

This is, functionally, already what [METHODOLOGY.md](../METHODOLOGY.md)'s Analysis Process describes (Collect, Compare, Reconstruct, Map, Document limitations), just not previously named as such. Making that connection explicit here is the point of adding this document: the repository's process was already following this model, this formalizes it rather than introducing a new practice.

| METHODOLOGY.md step | Intelligence Cycle phase |
|---|---|
| (implicit, choosing a subject from ROADMAP.md) | Direction |
| Collect | Collection |
| Compare | Processing |
| Reconstruct, Map | Analysis |
| The published `.md` file itself | Dissemination |
| (not currently formalized) | Feedback |

Feedback is the one phase this repository does not yet do deliberately, there is no current mechanism for revisiting an older analysis when new information emerges. That is a real, named gap rather than a hedge, see the Notes section of any analysis this applies to.

---

## Resources

- [ODNI - What is Intelligence?](https://www.dni.gov/index.php/what-we-do/what-is-intelligence) (note: this .gov domain may block automated fetches with a 403; it resolves normally in a browser as of this writing)
- [CIA - A Consumer's Guide to Intelligence, 1999 edition (Internet Archive)](https://archive.org/details/consumersguide_tenet), the original no longer resolves on cia.gov directly
