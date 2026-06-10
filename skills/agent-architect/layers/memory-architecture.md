# Memory Architecture

Version: 1.0
Skill: Agent Architect
Layer Type: Memory Layer

---

# Purpose

This layer defines memory design for agents and agent ecosystems. Memory gives agents continuity, but it also creates risk.

# Core Question

What should this agent remember, for how long, and under whose authority?

# Memory Types

## Working Memory
Short-lived mission context such as current task, recent instructions, active constraints. Retention: current mission only.

## Episodic Memory
Records of past events such as previous missions, decisions made, incidents handled, retrospective findings.

## Semantic Memory
Stable knowledge such as architecture principles, domain vocabulary, patterns, anti-patterns.

## Organizational Memory
Shared institutional knowledge such as ADRs, standards, policies, playbooks, governance decisions.

# Memory Scope

Memory should be scoped by agent, skill, department, world, organization, and mission.

# Memory Access Levels

## None
Use for stateless or sensitive tasks.

## Read-Only
Use for advisors, auditors, and review agents.

## Append-Only
Use for mission logs, incident logs, and audit trails.

## Curated Write
Agent may propose memory updates, but human or governance approval is required.

## Autonomous Write
Use sparingly and only within narrow boundaries.

# Memory Record Format

```yaml
id: mem-architecture-001
type: decision
scope: department
owner: software-architect-agent
created_at: 2026-06-10
source_mission: monolith-modernization
summary: The team selected a modular monolith before extracting services.
evidence:
  - adr-0007
  - architecture-review-2026-06
retention: long-term
review_after: 2026-12-10
```

# Memory Governance

Every memory system should define who can read, write, approve, delete, and correct memory; how long memory lives; and how it is audited.

# Memory Risks

## Stale Memory
Mitigation: expiration dates, review dates, confidence scores.

## Memory Pollution
Mitigation: curation workflow, source requirements, human approval.

## Over-Personalization
Mitigation: separate world memory from skill memory.

## Hidden State
Mitigation: memory summaries, audit logs, explainable retrieval.

# Design Checklist

- Does the agent need memory?
- Which memory types are required?
- What is the retention policy?
- Can users inspect memory?
- Can memory be corrected?
- Are decisions traceable?
