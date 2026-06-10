# WORLD_INTEGRATION_GUIDE.md

Agility Game World Integration Guide

Version: 1.0

Status: Core Specification

Repository: agility-game/skills

⸻

Purpose

Worlds provide context.

Skills provide competencies.

Departments provide organization.

Missions provide activities.

Achievements provide progression.

The World Integration Guide defines how these components interact.

⸻

Core Principle

Skills are reusable.

Worlds are variable.

The same skill should function in any world.

⸻

Integration Model
```
World
    ↓
Departments
    ↓
Skills
    ↓
Missions
    ↓
Achievements
    ↓
Story Progression
```
⸻

Example World

Software Factory

Departments

* Product
* Architecture
* Engineering
* Quality
* Security
* Operations

Skills

All core marketplace skills.

Missions

* Build Feature
* Fix Defect
* Deploy Release

Achievements

Engineering focused.

⸻

Example World

Space Colony

Departments

* Colony Planning
* Infrastructure
* Exploration
* Research

Skill Mapping

Software Architect
→ Colony Architect

Software Engineer
→ Systems Engineer

Quality Analyst
→ Safety Analyst

DevOps Engineer
→ Colony Operations Engineer

AI Engineer
→ Autonomous Systems Engineer

Missions

* Build Habitat
* Optimize Energy Grid
* Expand Colony

⸻

Example World

Code Smell Detective

Departments

* Detective Bureau
* Forensics
* Architecture Review
* Technical Analysis

Skill Mapping

Software Architect
→ Architecture Detective

Software Engineer
→ Refactoring Detective

Quality Analyst
→ Validation Detective

Threat Modeler
→ Security Detective

AI Engineer
→ Investigation Assistant

Missions

* Investigate God Object
* Solve Circular Dependency Case
* Refactor Legacy Monolith

Achievements

Detective-specific achievements.

⸻

World Adapters

Worlds adapt skills without changing skills.

Example

Base Skill

Software Architect

World Adapter

Cyberpunk Megacity

Display Name

Systems Planner

Capabilities

Remain unchanged.

This preserves marketplace compatibility.

⸻

World Creation Rules

Every world must define:

World Metadata

Departments

Mission Types

Achievement Extensions

Story Framework

Difficulty Curves

Economy Rules

NPC Definitions

Agent Definitions

Victory Conditions

⸻

World Progression

Worlds evolve through states.

Examples

Startup

→ Growth

→ Enterprise

→ Global Platform

Or

Small Colony

→ Regional Colony

→ Planetary Civilization

Skills remain reusable throughout progression.

⸻

Multi-World Gameplay

Players may travel between worlds.

Skills persist.

Achievements persist.

Reputation persists.

World-specific assets remain local.

This creates a persistent player identity across the Agility Game ecosystem.

⸻

Long-Term Vision

The Agility Game Kernel executes worlds.

Departments organize work.

Skills provide capabilities.

Missions create experiences.

Achievements create progression.

Worlds create stories.

Together they form an extensible ecosystem capable of simulating:

* Software Organizations
* Product Organizations
* AI Organizations
* Cybersecurity Programs
* Startups
* Enterprises
* Space Colonies
* Fantasy Kingdoms
* Future Worlds

without changing the kernel itself.
