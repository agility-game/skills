# MISSIONS.md — Code Smell Detective

## Purpose

This document defines missions that can be assigned to the Code Smell Detective skill.

---

## Mission Format

Each mission should include:

- Mission ID
- Title
- Scenario
- Objective
- Inputs
- Tasks
- Success Criteria
- Scoring Dimensions
- Rewards

---

## Mission 1: The Case of the God Object

```yaml
id: csd-001
title: The Case of the God Object
difficulty: intermediate
duration: 30-60 minutes
```

### Scenario

A class has grown over several sprints. Developers are afraid to change it because every modification seems to break something else.

### Objective

Identify whether the class is a God Object and propose a safe decomposition plan.

### Inputs

- Class source code
- Test coverage summary
- Change history
- Known bug reports

### Tasks

1. Identify responsibilities inside the class.
2. Count reasons to change.
3. Identify external dependencies.
4. Name the smell.
5. Propose extraction candidates.
6. Define the first safe refactoring step.

### Success Criteria

- Responsibilities are clearly listed.
- Evidence supports the smell classification.
- Refactoring plan is incremental.
- Testing strategy is included.

### Rewards

- Achievement: God Object Hunter
- XP: 100

---

## Mission 2: The Long Method Trail

```yaml
id: csd-002
title: The Long Method Trail
difficulty: beginner
duration: 20-40 minutes
```

### Scenario

A method mixes validation, calculation, logging, database access, and response formatting.

### Objective

Detect the Long Method smell and propose extraction steps.

### Tasks

1. Divide the method into conceptual sections.
2. Identify mixed abstraction levels.
3. Propose extracted methods.
4. Preserve behavior with tests.

### Rewards

- Achievement: Method Mapper
- XP: 60

---

## Mission 3: Feature Envy Interrogation

```yaml
id: csd-003
title: Feature Envy Interrogation
difficulty: intermediate
duration: 30-45 minutes
```

### Scenario

A service method repeatedly pulls data from another object and makes decisions that seem to belong elsewhere.

### Objective

Determine whether behavior should move closer to the data.

### Rewards

- Achievement: Responsibility Relocator
- XP: 80

---

## Mission 4: Duplicate Code Cold Case

```yaml
id: csd-004
title: Duplicate Code Cold Case
difficulty: beginner
duration: 20-30 minutes
```

### Scenario

The same business rule appears in multiple modules.

### Objective

Find duplication and propose a safe consolidation strategy.

### Rewards

- Achievement: Duplication Detective
- XP: 70

---

## Mission 5: Shotgun Surgery Alarm

```yaml
id: csd-005
title: Shotgun Surgery Alarm
difficulty: advanced
duration: 45-90 minutes
```

### Scenario

A small requirement change forces edits in controllers, services, validators, mappers, and tests.

### Objective

Identify scattered responsibilities and propose a design that localizes change.

### Rewards

- Achievement: Change Localizer
- XP: 130
