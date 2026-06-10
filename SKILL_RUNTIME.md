# Skill Runtime

Version: 1.0

---

# Purpose

Defines how skills are loaded by the Agility Game Kernel.

---

# Runtime Flow
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
↓
Scoring Engine
```
---

# Skill Loading

Example:

player:
  name: Sarah

skills:
  - architect
  - developer

---

# Resolution Process

1. Load skill definition
2. Load behaviors
3. Load prompts
4. Load tools
5. Load missions
6. Load scoring

---

# Tool Injection

Skills may consume capabilities from capsules.

Example:

Architect
→ Open Notebook

Developer
→ GitHub MCP

Scrum Master
→ StoriesOnBoard

---

# Runtime Isolation

Skills must never modify the kernel.

Customization belongs inside skills.

The kernel remains shared and upgradeable.
