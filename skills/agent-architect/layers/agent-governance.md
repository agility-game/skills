# Agent Governance

Version: 1.0
Skill: Agent Architect
Layer Type: Governance Layer

---

# Purpose

This layer defines governance for agent ecosystems. Governance prevents agent systems from becoming unsafe, confusing, unaccountable, or unmaintainable.

# Core Question

Who is allowed to decide, act, approve, remember, escalate, and change the system?

# Governance Domains

## Authority
What may the agent do? Recommend, draft, create issues, open pull requests, modify files, deploy systems, or approve changes.

## Accountability
Who is responsible for agent outputs? Human owner, department owner, mission owner, world owner, or governance board.

## Approval
Which actions require approval? Code merge, production deployment, policy change, memory update, customer-facing communication.

## Auditability
What must be recorded? Prompt input, agent decision, tool call, evidence used, output produced, approval result.

## Escalation
When must the agent stop and ask for help? Ambiguous authority, high-risk change, conflicting instructions, missing evidence, safety or compliance risk.

# Authority Levels

- Level 0: Observe
- Level 1: Recommend
- Level 2: Draft
- Level 3: Propose Change
- Level 4: Execute Approved Change
- Level 5: Autonomous Execution within narrow, pre-approved boundaries

# Governance Policy Example

```yaml
agent: release-coordinator
authority_level: 3
allowed_actions:
  - summarize_release_status
  - create_release_checklist
  - open_release_issue
requires_approval:
  - production_deployment
  - customer_announcement
  - rollback_decision
audit:
  enabled: true
  store:
    - decision
    - evidence
    - output
    - approval
escalation:
  - failed_security_gate
  - unresolved_p1_defect
  - conflicting_release_status
```

# Human-in-the-Loop Gates

Recommended gates: security-impacting change, production-impacting change, compliance-impacting change, financial-impacting change, external communication, memory policy change.

# Governance Anti-Patterns

- Invisible Authority
- Rubber-Stamp Approval
- No Audit Trail
- Tool Sprawl
- Memory Without Ownership

# Governance Review Checklist

- Is authority explicitly defined?
- Are approval gates clear?
- Is accountability assigned?
- Are tool permissions limited?
- Is memory governed?
- Are actions auditable?
- Is escalation defined?
- Can the agent be disabled safely?
- Can decisions be explained?
