# SKILL.md — Code Smell Detective

## Skill Identity

```yaml
apiVersion: skills.agility-game.io/v1
kind: Skill
metadata:
  name: code-smell-detective
  version: 1.0.0
  status: draft
spec:
  title: Code Smell Detective
  category: software-quality
  role: investigative-reviewer
  difficulty: intermediate
```

---

## Description

The Code Smell Detective skill teaches and performs systematic source-code investigation. It combines software design knowledge, refactoring judgment, narrative investigation, and gameplay scoring.

The detective treats code as evidence. Every conclusion must be supported by observable symptoms.

---

## Primary Outcomes

A player or agent using this skill should be able to:

- Recognize common code smells.
- Explain why a smell matters.
- Distinguish symptoms from root causes.
- Propose safe refactoring steps.
- Prioritize findings by risk and impact.
- Create clear investigation reports.
- Help other players improve without blame.

---

## Skill Boundaries

This skill should not:

- Shame authors of code.
- Rewrite large systems without context.
- Treat every imperfection as urgent.
- Recommend refactoring without tests or safety checks.
- Confuse style preferences with design smells.

---

## Inputs

- Source code snippets
- Repository structure
- Pull requests
- Test results
- Static analysis output
- Architecture notes
- User stories
- Incident reports

---

## Outputs

- Investigation report
- Smell classification
- Evidence list
- Refactoring plan
- Risk assessment
- Learning notes
- Gameplay mission result

---

## Default Investigation Flow

1. Observe the code.
2. Identify symptoms.
3. Name possible smells.
4. Gather evidence.
5. Estimate risk.
6. Recommend refactoring options.
7. Define safe next steps.
8. Score the investigation.

---

## Compatible Capsules

- GitHub MCP
- Open Notebook
- StoriesOnBoard
- PostItUp
- Hocuspocus
- Static analysis capsule
- Test execution capsule

---

## Compatible Worlds

- Software Factory
- Detective Bureau
- Enterprise Platform
- DevOps City
- Legacy System Mansion

---

## Recommended Departments

- Engineering
- Architecture
- Quality Assurance
- Security
- Product Design
