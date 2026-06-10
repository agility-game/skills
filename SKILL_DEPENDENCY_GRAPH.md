SKILL_DEPENDENCY_GRAPH.md

Skill Dependency Graph

Version: 1.0

Status: Recommended

Repository: agility-game/skills

⸻

Purpose

This document defines the relationships between skills within the Agility Game ecosystem.

Skills should not be viewed as isolated capabilities.

Real-world agility emerges through collaboration between skills.

The dependency graph describes:

* Collaboration paths
* Knowledge dependencies
* Mission dependencies
* Progression dependencies
* Organizational dependencies

⸻

Core Engineering Skill Pack

The initial engineering skill ecosystem consists of:

* Software Architect
* Software Engineer
* Software Quality Analyst
* CI/CD Engineer
* DevOps Engineer

⸻

Dependency Model

The graph does not imply hierarchy.

The graph describes collaboration.
```
                    Software Architect
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
      Software Engineer  Quality Analyst  DevOps Engineer
             │                               │
             └───────────────┬───────────────┘
                             ▼
                      CI/CD Engineer
```
⸻

Software Architect

Primary Focus

* System Design
* Technical Strategy
* Architecture Governance
* Architectural Debt

Collaborates With

* Software Engineer
* Quality Analyst
* DevOps Engineer

Produces

* ADRs
* Architecture Diagrams
* Technology Decisions
* Roadmaps

Consumes

* Quality Reports
* Operational Metrics
* Implementation Feedback

⸻

Software Engineer

Primary Focus

* Feature Delivery
* Refactoring
* Maintainability
* Code Quality

Collaborates With

* Architect
* Quality Analyst
* CI/CD Engineer

Produces

* Source Code
* Unit Tests
* Refactoring Plans

Consumes

* Architecture Decisions
* Acceptance Criteria
* Pipeline Feedback

⸻

Software Quality Analyst

Primary Focus

* Risk Assessment
* Verification
* Validation
* Test Strategy

Collaborates With

* Architect
* Engineer
* CI/CD Engineer

Produces

* Test Plans
* Quality Reports
* Risk Assessments

Consumes

* Requirements
* Architecture Decisions
* Deployment Evidence

⸻

CI/CD Engineer

Primary Focus

* Automation
* Build Systems
* Delivery Pipelines
* Release Quality

Collaborates With

* Engineer
* Quality Analyst
* DevOps Engineer

Produces

* Pipelines
* Release Workflows
* Build Metrics

Consumes

* Source Code
* Tests
* Platform Capabilities

⸻

DevOps Engineer

Primary Focus

* Platform Engineering
* Operations
* Observability
* Reliability

Collaborates With

* Architect
* Engineer
* CI/CD Engineer

Produces

* Infrastructure
* Monitoring
* Operational Dashboards

Consumes

* Architecture Decisions
* Application Requirements
* Release Pipelines

⸻

Mission Collaboration Examples

Example 1

Mission:
Refactor Monolith

Participants:

* Architect
* Engineer
* Quality Analyst

Outputs:

* Refactoring Plan
* Updated Code
* Validation Report

⸻

Example 2

Mission:
Kubernetes Migration

Participants:

* Architect
* DevOps Engineer
* CI/CD Engineer

Outputs:

* Target Architecture
* Infrastructure
* Deployment Pipeline

⸻

Example 3

Mission:
Eliminate God Object

Participants:

* Architect
* Engineer
* Quality Analyst

Outputs:

* Smell Analysis
* Refactored Design
* Regression Test Results

⸻

Future Skills

Future skills should extend this graph.

Examples:

* Product Owner
* Scrum Master
* Security Engineer
* UX Designer
* Platform Engineer
* Site Reliability Engineer
* AI Engineer

The dependency graph evolves with the ecosystem.
