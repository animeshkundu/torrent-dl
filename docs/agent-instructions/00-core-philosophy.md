# 00: Core Philosophy

This document establishes the fundamental principles that ALL AI agents MUST follow when working on this repository.

---

## 🎯 The Prime Directive: Docs = Code

> **NO CODE IS WRITTEN WITHOUT DOCUMENTATION**

Documentation is not an afterthought—it is the blueprint. Every piece of code must have corresponding documentation that explains:
- **What** it does
- **Why** it exists
- **How** it should be used

### Mandatory Documentation Workflow

```
1. Receive Task
      ↓
2. Read existing docs (specs, ADRs, architecture)
      ↓
3. Write/Update spec in docs/specs/ BEFORE coding
      ↓
4. Implement code
      ↓
5. Update documentation to reflect implementation
      ↓
6. Create handoff in docs/history/
```

### Where to Document

| Change Type | Documentation Location |
|-------------|------------------------|
| New feature | `docs/specs/feature-name-spec.md` |
| Architecture change | `docs/adrs/NNNN-decision.md` + `docs/architecture/` |
| Bug fix | Update relevant spec, add to history |
| Refactor | `docs/specs/refactor-description-spec.md` |

---

## 🔄 The Sync Protocol

After completing ANY work:

1. **Update History**: Create a handoff document in `docs/history/`
   - Date and agent identifier
   - Summary of work completed
   - Open items and recommendations
   - Context for future agents

2. **Update Specs**: Ensure specifications reflect current implementation
   - Mark completed requirements
   - Note any deviations from original plan
   - Add learnings

3. **Update Architecture**: If you changed system structure
   - Update Mermaid diagrams
   - Document new components
   - Update integration points

---

## 👔 The CEO Model

When working with sub-agents or delegated tasks:

### The CEO (Chief Execution Officer)
- The initiating agent that receives the original task
- **Responsibilities:**
  - Break down complex tasks into sub-tasks
  - Coordinate between sub-agents
  - Verify combined output meets requirements
  - Own the final quality of deliverables

### The Workers
- Sub-agents executing specific, scoped tasks
- **Responsibilities:**
  - Execute assigned task completely
  - Report blockers immediately
  - Document their work
  - Not exceed their scope

### Communication Protocol

```
CEO receives task
  ↓
CEO creates execution plan
  ↓
CEO delegates to Workers (with full context)
  ↓
Workers execute and report back
  ↓
CEO integrates and verifies
  ↓
CEO delivers final result
```

---

## 🧠 First Principles Thinking

Every decision must be rooted in first principles:

### The Reasoning Protocol

1. **Question Assumptions**
   - Why does the current code work this way?
   - What problem was it originally solving?
   - Is that problem still relevant?

2. **Deep Thinking**
   - Consider edge cases
   - Think about failure modes
   - Evaluate long-term implications

3. **Step-by-Step Planning**
   - Break complex problems into steps
   - Document your reasoning
   - Validate each step before proceeding

### The Anti-Patterns

❌ **Don't:**
- Copy code without understanding it
- Make changes without reading context
- Assume patterns are correct because they exist
- Skip documentation "to save time"

✅ **Do:**
- Research before implementing
- Read existing code thoroughly
- Question existing patterns
- Document everything

---

## 📋 Pre-Flight Checklist

Before making ANY code change, verify:

- [ ] I have read `docs/agent-instructions/` (this folder)
- [ ] I have checked `docs/adrs/` for relevant decisions
- [ ] I have read the relevant specification in `docs/specs/`
- [ ] I understand the system architecture from `docs/architecture/`
- [ ] I have written or updated the spec BEFORE coding
- [ ] I have a plan for testing my changes

After completing work:

- [ ] Code is implemented and tested
- [ ] Documentation is updated
- [ ] Handoff document is created in `docs/history/`
- [ ] Validation passes: `./scripts/validate.sh`

---

## 🚨 Escalation Protocol

When encountering issues:

1. **Uncertainty**: If unsure about a decision, document your reasoning and options
2. **Blockers**: Report blockers immediately with context
3. **Scope Creep**: If task scope expands, pause and re-plan
4. **Conflicts**: If finding conflicting requirements, surface them before proceeding

---

*This philosophy is non-negotiable. Adherence ensures code quality, maintainability, and successful collaboration between human and AI developers.*
