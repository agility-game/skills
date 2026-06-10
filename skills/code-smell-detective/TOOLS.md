# TOOLS.md — Code Smell Detective

## Purpose

This document defines tools and capsules that the Code Smell Detective skill may use.

---

## Tool Categories

### Repository Tools

Used to inspect source code and history.

Examples:

- GitHub
- GitLab
- Local repository scanner
- Pull request viewer

### Static Analysis Tools

Used to detect measurable signals.

Examples:

- SonarQube
- CodeQL
- Ruff
- ESLint
- Pylint
- PMD
- Checkstyle

### Test Tools

Used to understand safety and regression risk.

Examples:

- Unit test runner
- Coverage reporter
- Mutation testing tool
- CI pipeline logs

### Knowledge Tools

Used to enrich investigation.

Examples:

- Open Notebook
- Architecture decision records
- Documentation search
- Story maps

### Collaboration Tools

Used to turn findings into shared work.

Examples:

- StoriesOnBoard
- PostItUp
- GitHub Issues
- Jira
- Hocuspocus collaborative editor

---

## Tool Use Rules

The detective should:

- Prefer source evidence over assumptions.
- Use static analysis as signal, not final judgment.
- Check tests before recommending refactoring.
- Create small actionable work items.
- Preserve traceability from smell to evidence to fix.

---

## Optional Capsule Bindings

```yaml
capsules:
  github:
    purpose: inspect code and pull requests
  open-notebook:
    purpose: retrieve architecture and design knowledge
  storiesonboard:
    purpose: convert findings into backlog stories
  postitup:
    purpose: cluster smells during retrospectives
  hocuspocus:
    purpose: collaboratively edit investigation reports
```
