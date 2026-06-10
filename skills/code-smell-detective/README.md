# Code Smell Detective Skill

Version: 1.0.0  
Status: Draft  
Skill ID: `code-smell-detective`  
Repository Path: `agility-game/skills/code-smell-detective`

---

## Purpose

The Code Smell Detective skill enables a player, agent, or department to investigate source code, identify design smells, explain risks, propose refactorings, and turn findings into playable Agility Game missions.

This skill is designed for use by:

- Human players learning software design
- AI agents reviewing code
- Engineering departments inside Agility Game worlds
- Scenario authors creating detective-style software quality missions
- Code Smell Detective story-world characters

---

## Skill Summary

A Code Smell Detective observes code like a crime scene.

The detective does not merely say that code is “bad.” Instead, the detective:

1. Identifies symptoms.
2. Names likely smells.
3. Explains consequences.
4. Collects evidence.
5. Suggests refactorings.
6. Prioritizes fixes.
7. Converts the investigation into learning.

---

## Core Responsibilities

- Detect code smells
- Explain architectural risk
- Identify maintainability issues
- Recommend refactorings
- Create investigation reports
- Convert findings into missions
- Help players learn better design judgment

---

## Directory Structure

```text
code-smell-detective/
├── README.md
├── SKILL.md
├── KNOWLEDGE.md
├── BEHAVIORS.md
├── MISSIONS.md
├── TOOLS.md
├── SCORING.md
├── ACHIEVEMENTS.md
├── RUBRICS.md
├── PROMPTS.md
├── EXAMPLES.md
├── layers/
├── templates/
├── assets/
└── tests/
```

---

## Relationship to Agility Game

This skill is reusable across worlds.

Examples:

- In a software factory world, the detective investigates production code.
- In a detective story world, the detective solves design crimes.
- In a training world, the detective guides players through refactoring exercises.
- In an enterprise world, the detective supports architecture governance.

---

## References

- `../architecture/kernel/KERNEL_SETUP.md`
- `../architecture/layers/LAYERS_FRAMEWORK.md`
- `../SKILL_SPECIFICATION.md`
- `../SKILL_RUNTIME.md`
- `../SKILL_SCORING.md`
