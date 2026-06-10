# Architecture Tests

These tests validate the Agent Architect skill implementation.

---

# Test 1: Single Responsibility

## Given

A relevant agent, team, mission, or world specification.

## When

The specification is reviewed or executed.

## Then

The agent should have one primary mission and no unrelated responsibilities.

## Pass Criteria

- Evidence is present.
- Ownership is clear.
- Governance is respected.
- Output is inspectable.

---

# Test 2: Replaceability

## Given

A relevant agent, team, mission, or world specification.

## When

The specification is reviewed or executed.

## Then

The world should continue to function when the agent implementation is replaced with another implementation that honors the same contract.

## Pass Criteria

- Evidence is present.
- Ownership is clear.
- Governance is respected.
- Output is inspectable.

---

# Test 3: Skill Composition

## Given

A relevant agent, team, mission, or world specification.

## When

The specification is reviewed or executed.

## Then

A composed agent must have a primary skill and mission-relevant supporting skills.

## Pass Criteria

- Evidence is present.
- Ownership is clear.
- Governance is respected.
- Output is inspectable.

---

# Test 4: World Adapter

## Given

A relevant agent, team, mission, or world specification.

## When

The specification is reviewed or executed.

## Then

A world-specific role must trace back to reusable marketplace skills without forking them.

## Pass Criteria

- Evidence is present.
- Ownership is clear.
- Governance is respected.
- Output is inspectable.
