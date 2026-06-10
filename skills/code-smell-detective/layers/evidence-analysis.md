# Layer: Evidence Analysis

## Purpose

Transform observations into traceable investigation evidence.

---

## Evidence Types

- Code structure
- Method length
- Responsibility count
- Dependency count
- Duplicated logic
- Change frequency
- Test coverage
- Runtime incidents

---

## Evidence Format

```yaml
evidence:
  - id: E1
    type: responsibility
    observation: The class validates orders and sends emails.
    supports: God Object
    strength: medium
```

---

## Evidence Quality

Strong evidence is:

- Specific
- Observable
- Relevant
- Linked to a smell
- Not merely stylistic
