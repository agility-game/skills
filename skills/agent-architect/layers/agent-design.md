# Agent Design

Version: 1.0
Skill: Agent Architect
Layer Type: Core Design Layer

---

# Purpose

This layer defines how to design individual agents inside the Agility Game ecosystem.

An agent is not merely a prompt. An agent is a bounded participant with a purpose, role, skill profile, memory model, tool boundary, mission scope, governance model, and measurable outcome.

# Core Question

What should this agent be responsible for, and what should it not be responsible for?

# Design Principles

## Purpose Before Capability

Start with the agent mission, not its tools.

Good examples:

- Investigate architectural debt in a repository.
- Coach a team through retrospective improvement.
- Validate whether a release is ready.

Weak examples:

- Use an LLM to answer questions.
- Automate everything.
- Act like a developer.

## Clear Role Boundary

Every agent needs a bounded role describing what it owns, advises on, escalates, and must never do.

## Skill-Based Identity

Agents should be composed from skills.

Example:

```yaml
agent: architecture-detective
skills:
  - software-architect
  - code-smell-detective
  - threat-modeler
```

## Minimal Tool Access

Agents receive only the tools needed for the mission. Tool access is granted by mission, department, world, and governance rules.

## Observable Outputs

Every agent must produce inspectable artifacts such as decisions, reports, pull request comments, investigation notes, risk findings, and mission summaries.

# Agent Specification Fields

```yaml
id: architecture-detective
name: Architecture Detective
type: ai-agent
version: 1.0.0
mission: Investigate architectural risks and code smells.
skills:
  - software-architect
  - code-smell-detective
department: architecture-review
authority:
  can_recommend: true
  can_modify_code: false
  can_create_issues: true
  can_merge_pull_requests: false
memory:
  working: enabled
  episodic: enabled
  semantic: enabled
  organizational: read-only
tools:
  - github
  - open-notebook
  - code-analysis
outputs:
  - architecture-findings
  - refactoring-recommendations
  - adr-drafts
```

# Agent Types

## Advisor Agent
Provides guidance. Examples: Architecture Advisor, Product Advisor, Security Advisor.

## Worker Agent
Completes bounded tasks. Examples: Test Generator, Documentation Writer, Refactoring Assistant.

## Coordinator Agent
Routes work and coordinates other agents. Examples: Mission Coordinator, Department Coordinator.

## Auditor Agent
Validates outputs. Examples: Quality Auditor, Compliance Auditor.

## World Agent
Represents a world-specific role. Examples: Colony Operations Agent, Detective Bureau Agent.

# Design Checklist

- Does the agent have one clear mission?
- Is the role boundary explicit?
- Are skills listed?
- Are tools limited?
- Are outputs observable?
- Is authority constrained?
- Is escalation defined?
- Is memory scoped?
- Can the agent be tested?
- Can the agent be replaced without changing the kernel?

# Anti-Pattern Warning

Avoid creating universal agents. A universal agent becomes unclear, unsafe, difficult to test, and impossible to govern. Prefer a network of small, specialized agents.
