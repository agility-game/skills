# Multi-Agent Systems

Version: 1.0
Skill: Agent Architect
Layer Type: Collaboration Layer

---

# Purpose

This layer defines how multiple agents collaborate inside Agility Game. Multi-agent design is about useful collaboration structures, not merely increasing the number of agents.

# Core Question

Which agents should collaborate, compete, review, delegate, or escalate?

# Collaboration Models

## Sequential Workflow

Agents work in order.

Example:

Product Owner Agent -> Architect Agent -> Engineer Agent -> Quality Agent -> DevOps Agent

Use when work has clear phases and each output becomes the next input.

## Parallel Analysis

Agents analyze the same input from different perspectives.

Example: Security Agent reviews risks, Quality Agent reviews testability, Architect Agent reviews structure.

## Debate Model

Agents propose alternatives and critique each other. Use when strategy is uncertain and trade-offs matter.

## Manager-Worker Model

A coordinator agent delegates tasks and consolidates outputs. Use when a mission has many subtasks.

## Peer Review Model

Agents review each other's outputs. Use when quality matters and mistakes are expensive.

# Coordination Artifacts

Recommended artifacts:

- Mission brief
- Agent responsibility matrix
- Shared glossary
- Decision log
- Risk register
- Output registry
- Escalation log

# Responsibility Matrix

```markdown
| Responsibility | Primary Agent | Supporting Agents | Human Approval |
|---|---|---|---|
| Architecture decision | Architect Agent | Security Agent, DevOps Agent | Required |
| Code refactoring | Engineer Agent | Quality Agent | Required for merge |
| Release validation | Quality Agent | CI/CD Agent | Required |
```

# Communication Rules

Every agent message should include sender, recipient, mission, context, request, evidence, expected output, and deadline or turn limit.

# Conflict Resolution

1. Capture the disagreement.
2. Identify assumptions.
3. Compare evidence.
4. Ask for missing context.
5. Escalate if authority is insufficient.
6. Produce a decision record.

# Failure Modes

## Agent Echo Chamber
Mitigation: add auditor agent, require evidence, require dissenting view.

## Role Collision
Mitigation: define ownership and use responsibility matrices.

## Coordination Explosion
Mitigation: limit agent count and prefer smaller missions.

## Authority Confusion
Mitigation: define authority levels and human approval gates.

# Design Checklist

- Is collaboration necessary?
- Are agent roles distinct?
- Is the collaboration model explicit?
- Is there a shared mission brief?
- Is escalation defined?
- Are outputs merged into one coherent result?
