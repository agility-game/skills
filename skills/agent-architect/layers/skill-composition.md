# Skill Composition

Version: 1.0
Skill: Agent Architect
Layer Type: Composition Layer

---

# Purpose

This layer defines how agents combine multiple skills. Many useful agents are composites. The Agent Architect decides which skills should be combined and where the boundary becomes too broad.

# Core Question

Which skill combination creates useful agency without creating confusion?

# Composition Examples

## Security Architect Agent

Skills: software-architect, security-engineer, threat-modeler.

Purpose: Design secure systems and evaluate architectural risk.

## Platform Engineer Agent

Skills: devops-engineer, ci-cd-engineer, software-engineer.

Purpose: Build and operate internal developer platforms.

## AI Product Strategist Agent

Skills: product-owner, business-analyst, ai-engineer.

Purpose: Define valuable AI-enabled product capabilities.

## Code Smell Detective Agent

Skills: code-smell-detective, software-architect, software-engineer, software-quality-analyst.

Purpose: Investigate, explain, and propose remediation for code smells.

# Composition Rules

## Compose Around Missions
Do not combine skills merely because they are related. Combine them because a mission requires them.

## Limit Primary Identity
Each agent should have one primary identity. Secondary skills support the primary identity.

## Avoid Skill Overload
If an agent needs more than five major skills, create a team instead.

## Separate Conflicting Duties
Do not combine maker and approver when governance requires separation.

# Skill Weighting

```yaml
agent: security-architect
skills:
  software-architect: 0.50
  security-engineer: 0.30
  threat-modeler: 0.20
```

# Skill Composition Checklist

- What is the primary skill?
- What are supporting skills?
- Are any duties conflicting?
- Would a team be better?
- Does the mission require this combination?
- Can scoring attribute performance to each skill?
