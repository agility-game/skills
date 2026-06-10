# Orchestration

Version: 1.0
Skill: Agent Architect
Layer Type: Execution Layer

---

# Purpose

This layer defines how agents are coordinated during missions. Orchestration is the design of flow, responsibility, timing, handoffs, and recovery.

# Core Question

How does work move through the agent ecosystem?

# Orchestration Patterns

## Linear Pipeline
Business Analyst -> Architect -> Engineer -> QA -> CI/CD -> DevOps. Use for predictable workflows.

## Hub-and-Spoke
A coordinator delegates to specialists. Use for complex multi-skill missions.

## Blackboard
Agents contribute to a shared workspace. Use for discovery, investigation, brainstorming, and research.

## Event-Driven
Agents respond to state changes. Use for runtime worlds and operational events.

## Human-Gated
Agents complete steps, but humans approve transitions. Use for high-risk workflows.

# Mission State Machine

```text
Created -> Assigned -> In Progress -> Review -> Approved -> Completed -> Archived
```

Optional states: Blocked, Escalated, Rejected, Reopened, Cancelled.

# Handoff Requirements

Every handoff should include mission state, completed work, open questions, risks, evidence, and recommended next action.

# Failure Recovery

Agents should handle missing input, conflicting output, tool failure, agent timeout, low confidence, and governance blocks.

Recovery options: retry, ask, escalate, reassign, split mission, pause mission.

# Orchestration Checklist

- Is the workflow explicit?
- Are handoffs structured?
- Is mission state tracked?
- Are failures recoverable?
- Are approval gates integrated?
- Is the number of agents justified?
- Is the final output consolidated?
