# RUBRICS.md — Code Smell Detective

## Purpose

This document defines assessment rubrics for Code Smell Detective missions.

---

## Investigation Report Rubric

| Dimension | Excellent | Adequate | Weak |
|---|---|---|---|
| Observation | Accurately explains code behavior and structure. | Describes main behavior but misses some context. | Misstates or invents behavior. |
| Smell Identification | Correctly names smell and explains why. | Names plausible smell with partial explanation. | Names smell without evidence. |
| Evidence | Specific, traceable, relevant. | Some evidence, but not complete. | Mostly opinion. |
| Risk Assessment | Connects smell to maintainability, testability, or change risk. | Mentions risk generally. | No meaningful risk explanation. |
| Refactoring Plan | Small, safe, sequenced, test-aware. | Useful but incomplete. | Vague or risky rewrite. |
| Communication | Clear, respectful, teachable. | Understandable but rough. | Blaming, vague, or confusing. |

---

## Smell Classification Rubric

A smell classification is strong when it includes:

1. Name of smell.
2. Code symptoms.
3. Why the symptoms fit.
4. Possible alternative explanations.
5. Confidence level.
6. Impact.
7. Suggested next move.

---

## Refactoring Plan Rubric

A good refactoring plan must include:

- First safe step
- Required tests
- Expected behavior preservation
- Extraction or movement target
- Rollback option
- Risk level

---

## Communication Rubric

Feedback should be:

- Specific
- Respectful
- Actionable
- Prioritized
- Educational

Avoid:

- “Bad code”
- “Just rewrite it”
- “Obviously wrong”
- “Everyone knows...”
