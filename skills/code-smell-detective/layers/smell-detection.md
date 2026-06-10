# Layer: Smell Detection

## Purpose

Detect probable code smells from source code evidence.

---

## Inputs

- Code snippet
- File path
- Language
- Test context
- Change context

---

## Output

```yaml
smells:
  - name: Long Method
    confidence: high
    evidence:
      - method contains validation, calculation, persistence, and notification
    impact:
      - harder to test
      - multiple reasons to change
```

---

## Rules

- Do not classify without evidence.
- Prefer multiple weak signals over one superficial signal.
- Include confidence level.
- Include alternative interpretations when useful.
