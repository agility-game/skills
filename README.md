# Agility Game Skills

Version: 1.0

---

# Purpose

The Skills Repository contains the reusable competencies used throughout the Agility Game ecosystem.

Skills represent knowledge, behavior, decision-making patterns, tools, missions, and progression systems that can be assigned to:

- Human Players
- AI Players
- Departments
- Teams
- NPCs
- Worlds
- Scenarios

Skills are independent from gameplay content and runtime implementations.

This allows skills to be reused across multiple worlds and scenarios.

---

# Relationship to Other Repositories

## Kernel

Responsible for execution.

Repository:

agility-game/platform

---

## Worlds

Provide context.

Examples:

- Software Factory
- Space Colony
- Medieval Kingdom
- Smart City

---

## Scenarios

Provide gameplay situations.

Examples:

- Sprint Planning
- Incident Response
- Product Launch

---

## Capsules

Provide capabilities.

Examples:

- Open Notebook
- Hocuspocus
- StoriesOnBoard
- PostItUp

---

## Skills

Provide intelligence.

Examples:

- Architect
- Product Owner
- Developer
- Scrum Master
- Tester
- Security Engineer

---

# Repository Structure
```
skills/
├── README.md
├── SKILL_SPECIFICATION.md
├── SKILL_SCHEMA.yaml
├── SKILL_RUNTIME.md
├── SKILL_SCORING.md
├── SKILL_LEVELING.md
├── SKILL_MARKETPLACE.md
└── skills/
```
---

# Core Principle

Skills are reusable.

A skill should work in any world.

Worlds change.

Scenarios change.

Capsules change.

Skills remain stable.

---

# References

See:

../architecture/kernel/KERNEL_SETUP.md

../architecture/layers/LAYERS_FRAMEWORK.md
