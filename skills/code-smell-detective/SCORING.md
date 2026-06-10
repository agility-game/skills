# SCORING.md — Code Smell Detective

## Purpose

This document defines scoring for the Code Smell Detective skill.

---

## Total Score

Maximum score per mission: 100 points.

---

## Scoring Dimensions

### 1. Observation Accuracy — 20 points

Measures whether the detective accurately describes the code.

Full score requires:

- Correct summary of behavior
- Clear identification of relevant structures
- No invented facts

---

### 2. Smell Classification — 20 points

Measures whether the detective names the correct smell or smells.

Full score requires:

- Correct smell name
- Explanation of why it applies
- Acknowledgement of uncertainty where needed

---

### 3. Evidence Quality — 20 points

Measures whether claims are supported by evidence.

Full score requires:

- Specific code references
- Observable symptoms
- No unsupported accusations

---

### 4. Refactoring Plan — 20 points

Measures whether proposed improvements are safe and useful.

Full score requires:

- Incremental steps
- Test strategy
- Clear expected benefit
- Low unnecessary disruption

---

### 5. Communication — 20 points

Measures whether the report is understandable and respectful.

Full score requires:

- Clear language
- Prioritized findings
- No blame
- Actionable recommendations

---

## Score Bands

| Score | Rating | Meaning |
|---:|---|---|
| 0-39 | Unsolved | The investigation is weak or unsupported. |
| 40-59 | Apprentice Detective | Some useful clues, but incomplete reasoning. |
| 60-79 | Capable Detective | Solid finding with practical next steps. |
| 80-94 | Senior Detective | Strong evidence and high-quality refactoring plan. |
| 95-100 | Master Detective | Excellent reasoning, prioritization, and teaching value. |

---

## Penalties

Subtract points for:

- Unsupported smell claims
- Overly broad rewrite advice
- Ignoring missing tests
- Confusing formatting with design quality
- Blaming developers
- Failing to prioritize
