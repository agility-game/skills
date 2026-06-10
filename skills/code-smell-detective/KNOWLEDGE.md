# KNOWLEDGE.md — Code Smell Detective

## Purpose

This document defines the knowledge required by the Code Smell Detective skill.

---

## Core Knowledge Areas

### 1. Code Smells

The detective should recognize at least the following smells:

- God Object
- Long Method
- Large Class
- Feature Envy
- Data Clumps
- Primitive Obsession
- Shotgun Surgery
- Divergent Change
- Duplicate Code
- Switch Statements
- Inappropriate Intimacy
- Message Chains
- Middle Man
- Speculative Generality
- Dead Code
- Lazy Class
- Refused Bequest
- Temporary Field

---

### 2. Design Principles

The detective should understand:

- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle
- Separation of Concerns
- Information Hiding
- Coupling and Cohesion
- Encapsulation
- Composition over Inheritance

---

### 3. Refactoring Techniques

Common refactorings include:

- Extract Method
- Extract Class
- Move Method
- Move Field
- Introduce Parameter Object
- Replace Primitive with Value Object
- Replace Conditional with Polymorphism
- Introduce Strategy
- Introduce Facade
- Remove Dead Code
- Rename for Clarity
- Split Phase

---

### 4. Investigation Reasoning

The detective must separate:

- Evidence from opinion
- Symptom from root cause
- Local smell from architectural smell
- Urgent risk from cosmetic improvement
- Safe refactoring from risky rewrite

---

### 5. Software Quality Dimensions

The detective evaluates:

- Readability
- Maintainability
- Testability
- Extensibility
- Reliability
- Security impact
- Operational risk
- Cognitive load

---

## Detection Heuristics

### God Object

Possible signs:

- One class knows too much.
- One class does too much.
- Many unrelated responsibilities are grouped together.
- Many other modules depend on it.
- Changes frequently affect the same class.

### Long Method

Possible signs:

- Method is hard to summarize in one sentence.
- Multiple abstraction levels are mixed.
- Local variables accumulate over time.
- Comments divide the method into hidden sections.

### Feature Envy

Possible signs:

- A method uses another object’s data more than its own.
- Logic appears to belong closer to another class.
- Getters are repeatedly called on another object.

### Shotgun Surgery

Possible signs:

- One small change requires edits in many files.
- Business rules are duplicated across modules.
- Related logic is scattered.

---

## Investigation Questions

- What is this code responsible for?
- How many reasons does it have to change?
- Where is the business rule located?
- What would break if this changed?
- Is this complexity essential or accidental?
- Can this be refactored safely with tests?
- What is the smallest useful improvement?
