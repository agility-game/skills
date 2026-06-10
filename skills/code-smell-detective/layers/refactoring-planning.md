# Layer: Refactoring Planning

## Purpose

Create safe, incremental refactoring plans from smell findings.

---

## Planning Principles

1. Preserve behavior.
2. Add or confirm tests first.
3. Make one responsibility move at a time.
4. Prefer reversible steps.
5. Stop when risk outweighs benefit.

---

## Refactoring Plan Format

```yaml
plan:
  goal: Reduce God Object risk
  steps:
    - add characterization tests
    - extract email notification behavior
    - inject notification dependency
    - verify behavior through tests
  risk: medium
  rollback: keep original class until tests pass
```
