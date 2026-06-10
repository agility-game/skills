# World Integration

Version: 1.0
Skill: Agent Architect
Layer Type: World Layer

---

# Purpose

This layer defines how agent ecosystems are adapted to Agility Game worlds. Worlds provide context. Skills provide capability. Agents enact roles inside worlds.

# Core Question

How should agents appear, behave, and collaborate inside this world?

# World Adapter Concept

A world adapter changes presentation and context without changing the underlying skill.

Example mappings:

- Software Architect -> Code Smell Detective: Architecture Detective
- Software Architect -> Space Colony: Habitat Systems Architect
- Software Architect -> Cyber Defense World: Security Systems Architect

The capability remains compatible with the marketplace.

# Agent World Mapping

Each world should define display names, departments, mission types, achievement extensions, tool availability, governance constraints, NPC roles, and player roles.

# Example: Code Smell Detective

```yaml
world: code-smell-detective
agents:
  architecture-detective:
    base_skills:
      - software-architect
      - code-smell-detective
    department: architecture-review
    missions:
      - investigate-god-object
      - identify-architectural-debt
      - draft-refactoring-plan
  refactoring-detective:
    base_skills:
      - software-engineer
    department: forensics
    missions:
      - refactor-long-method
      - remove-duplicate-code
      - simplify-complex-class
```

# Example: Agility Game Platform World

Agents: Kernel Architect, Capsule Designer, Skill Librarian, Mission Generator, Achievement Curator, World Builder.

# World Integration Rules

1. Do not fork base skills.
2. Use world adapters.
3. Keep world-specific vocabulary in world files.
4. Keep reusable capability in skill files.
5. Keep governance compatible with kernel policy.
6. Keep achievements portable where possible.

# World-Specific Memory

World memory may include local story history, NPC relationships, mission outcomes, world economy state, and local terminology.

World memory should not overwrite core skill knowledge.

# Design Checklist

- Are base skills reused?
- Are world names mapped clearly?
- Are missions world-specific but skill-compatible?
- Are achievements connected?
- Are tools available in the world?
- Are governance constraints defined?
- Can the world run without changing the kernel?
