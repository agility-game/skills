# Skill Specification

Version: 1.0

---

# Purpose

This document defines the standard structure of an Agility Game skill.

All skills must conform to this specification.

---

# Skill Definition

A skill is a reusable competency that can be assigned to a player, team, department, NPC, or AI agent.

A skill contains:

- Knowledge
- Behaviors
- Goals
- Missions
- Tools
- Scoring Rules
- Achievements

---

# Required Structure
```
skill-name/
│
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
│
├── layers/
├── templates/
├── assets/
└── tests/
```
---

# Skill Components

## Knowledge

What the skill knows.

Examples:

- Architecture principles
- Scrum concepts
- Security practices

---

## Behaviors

How the skill acts.

Examples:

- Facilitate discussions
- Review designs
- Investigate incidents

---

## Goals

Desired outcomes.

Examples:

- Reduce risk
- Improve quality
- Increase delivery speed

---

## Tools

Resources available to the skill.

Examples:

- GitHub
- Open Notebook
- StoriesOnBoard

---

## Missions

Activities available to the skill.

Examples:

- Create architecture
- Perform threat model
- Plan sprint

---

## Achievements

Recognition earned through gameplay.

Examples:

- Security Champion
- Master Architect
- Agile Facilitator

---

# Design Rules

Skills must:

- Be reusable
- Be composable
- Be testable
- Be measurable
- Be independent of worlds
