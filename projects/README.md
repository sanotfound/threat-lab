# Independent Projects

This section holds standalone tools built to develop a specific skill, tracked as a gap in [SKILLS.md](../SKILLS.md), or to build first-hand understanding of a technique ahead of writing one of the OSINT analyses in `analysis/`. It is distinct from the rest of this repository in what it produces: `analysis/` produces write-ups about threats, `analysis/labs/` documents exercises against an intentionally vulnerable target, this section produces working code.

The list of planned projects, their priority, and the reasoning behind the execution order lives in [ROADMAP.md](../ROADMAP.md)'s **Independent Projects** section. This directory is where the actual result of working through that list lands, one subfolder per project, created only once that project is actually started, not scaffolded in advance for the whole list.

---

## Structure

Each project gets its own folder, named after the project (kebab-case, e.g. `dns-lookup-cli/`):

```
projects/
├── README.md
├── TEMPLATE.md
└── dns-lookup-cli/
    ├── README.md      # what/why/how, following TEMPLATE.md
    └── (source code)
```

See [TEMPLATE.md](TEMPLATE.md) for what each project's own `README.md` should cover.

---

## Relationship to the Rest of This Repository

- A project built here to prepare for a planned `analysis/attacks/` or `analysis/malware/` write-up should be referenced from that analysis once it is written (e.g., "built and tested the underlying technique first-hand, see `projects/supply-chain-attack-simulator/`").
- Detection logic that comes out of a project here and generalizes into a reusable rule still belongs in `detection/`, not duplicated inside the project folder.
- This directory follows no fixed language or framework, each project uses whatever the skill being developed actually calls for (see the language noted per project in ROADMAP.md).
