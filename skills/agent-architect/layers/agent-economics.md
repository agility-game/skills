# Agent Economics

Version: 1.0
Skill: Agent Architect
Layer Type: Economy Layer

---

# Purpose

This layer defines how agents consume resources, create value, and participate in gameplay economies. Agent economics helps prevent unlimited automation from flattening the game.

# Core Question

What does this agent cost, what value does it create, and how is that value measured?

# Resource Types

- Time: agent turns, execution cycles, review time.
- Compute: model usage, tool usage, infrastructure cost.
- Attention: human review, approval, interpretation.
- Risk: possible damage caused by incorrect output.
- Trust: confidence earned through performance.

# Value Types

Agents may create value through faster feedback, better decisions, reduced defects, lower risk, improved documentation, increased learning, and better collaboration.

# Cost Model

```yaml
agent: architecture-detective
mission_cost:
  turns: 5
  human_review_minutes: 15
  tool_calls:
    github: 3
    open-notebook: 2
risk: medium
expected_value:
  architecture_risk_reduction: high
  learning_value: medium
```

# Trust Economy

Trust increases when outputs are accurate, recommendations are useful, risks are caught, human review passes, and missions succeed.

Trust decreases when outputs are unsupported, evidence is weak, governance is violated, missions fail, or escalation is ignored.

# Unlocks

Higher-trust agents may unlock more complex missions, more autonomy, more tools, department roles, and world roles.

# Economic Anti-Patterns

- Free Infinite Agents
- Hidden Cost
- Automation Without Value
- Trust Inflation

# Design Checklist

- Is agent cost visible?
- Is agent value measurable?
- Does trust affect authority?
- Are tool costs tracked?
- Is human review cost represented?
- Can agents lose trust?
- Are high-risk actions more expensive?
