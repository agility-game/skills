# Skills

- [References](./REFERENCES.md)

This repository fits very naturally into the architecture we have been developing around the Agility Game kernel.

Given your current architecture, I would position skills as a first-class concept alongside:

* platform → runtime/kernel
* worlds → business domains and environments
* capsules → installable capabilities
* scenarios → gameplay content
* skills → reusable agent competencies

Recommended Role of agility-game/skills

The repository should become the canonical library of capabilities that can be attached to:

* Human players
* AI players
* Departments
* NPCs
* Worlds
* Capsules

Examples:
```
skills/
├── product-owner/
├── scrum-master/
├── architect/
├── developer/
├── tester/
├── security-engineer/
├── ux-designer/
├── business-analyst/
├── devops-engineer/
├── release-manager/
└── facilitator/
```
Each skill would contain:
```
Skill
 ├── Knowledge
 ├── Behaviors
 ├── Goals
 ├── Tools
 ├── Prompts
 ├── Scoring
 ├── Missions
 └── Achievements
```
⸻

How Layers Fits

The Layers framework you referenced earlier is almost a perfect match.

Instead of treating Layers as a separate system, use it as the implementation model for Agility Game skills.

Example:
```
agility-game/skills
architect/
├── skill.yaml
├── prompts/
├── rubrics/
├── missions/
├── achievements/
└── layers/
    ├── architecture-review.md
    ├── threat-modeling.md
    ├── domain-modeling.md
    └── technical-roadmapping.md
```
The Layers assets become the internal building blocks of a skill.

⸻

Skill Structure

I would standardize every skill as:
```
skill/
│
├── README.md
├── SKILL.md
├── KNOWLEDGE.md
├── MISSIONS.md
├── ACHIEVEMENTS.md
├── SCORING.md
├── PROMPTS.md
├── TOOLS.md
├── RUBRICS.md
├── EXAMPLES.md
│
├── layers/
├── assets/
├── templates/
└── tests/
```
⸻

Runtime Integration

The Agility Game Kernel can load skills dynamically:
```
player:
  name: Sarah
skills:
  - architect
  - developer
  - security-engineer
```
The runtime then resolves:
```
Kernel
  ↓
Skill Resolver
  ↓
Prompt Resolver
  ↓
Tool Resolver
  ↓
Mission Engine
```
This aligns perfectly with the kernel architecture.

⸻

Relationship with Capsules

A useful distinction:

Capsule

Installs functionality

Examples:

* Hocuspocus
* Open Notebook
* PostItUp
* StoriesOnBoard

Skill

Uses functionality

Examples:

* Product Owner
* Scrum Master
* Architect
* Developer

Diagram:
```
Architect Skill
        │
        ▼
 ┌──────────────┐
 │ OpenNotebook │
 └──────────────┘
Developer Skill
        │
        ▼
 ┌──────────────┐
 │ GitHub MCP   │
 └──────────────┘
Scrum Master Skill
        │
        ▼
 ┌──────────────┐
 │ StoriesBoard │
 └──────────────┘
```
⸻

Relationship with Worlds

Worlds define context.

Example:
```
World
 └── Space Colony
Skill
 └── Architect
Mission
 └── Design colony power grid
```
Same architect skill:
```
World
 └── Medieval Kingdom
Mission
 └── Design castle defenses
```
The skill remains reusable.

⸻

Relationship with Departments

Your earlier department model becomes even stronger.
```
Department
 ├── Product
 ├── Design
 ├── Engineering
 ├── Security
 ├── Operations
 └── Leadership
```
Departments are collections of skills.

Example:
```
department: engineering
skills:
  - architect
  - developer
  - tester
  - devops-engineer
```
⸻

What I Would Add Next

Inside agility-game/skills:
```
skills/
├── README.md
├── SKILL_SPECIFICATION.md
├── SKILL_SCHEMA.yaml
├── SKILL_RUNTIME.md
├── SKILL_SCORING.md
├── SKILL_LEVELING.md
├── SKILL_MARKETPLACE.md
└── examples/
```
These documents become the foundation for every future skill.

⸻

Long-term Vision

The most powerful interpretation is:
```
Kernel
    +
Worlds
    +
Capsules
    +
Scenarios
    +
Skills
    =
Agility Game
```
Where:

* Kernel = execution engine
* Worlds = context
* Capsules = capabilities
* Scenarios = gameplay
* Skills = intelligence and behavior

This turns agility-game/skills into one of the core repositories of the entire ecosystem rather than merely a collection of prompts.
