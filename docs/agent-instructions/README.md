# Agent Instructions

This directory contains protocol documents that ALL AI agents MUST read and follow when working on the torrent-dl repository.

## Reading Order

AI agents should read these documents in order:

1. **[00-core-philosophy.md](./00-core-philosophy.md)** - Fundamental principles (REQUIRED FIRST)
2. **[01-research-and-web.md](./01-research-and-web.md)** - Research protocols
3. **[02-testing-and-validation.md](./02-testing-and-validation.md)** - Testing requirements
4. **[03-tooling-and-pipelines.md](./03-tooling-and-pipelines.md)** - CI/CD and automation

## Quick Reference

### The Three Laws

1. **Docs = Code**: No code changes without updating documentation
2. **Test Everything**: 90% minimum code coverage requirement
3. **Research First**: Use web search before implementing

### The CEO Model

When an AI agent receives a task:
- The initiating agent is the **CEO** (Chief Execution Officer)
- Sub-agents are **workers** executing specific tasks
- CEOs are responsible for coordination and final verification

### Mandatory Checkpoints

Before making ANY code change:
- [ ] Read `docs/adrs/` for past decisions
- [ ] Read relevant specs in `docs/specs/`
- [ ] Check `docs/architecture/` for system understanding

After completing work:
- [ ] Update or create specs in `docs/specs/`
- [ ] Update `docs/architecture/` if structural changes
- [ ] Create handoff in `docs/history/`
- [ ] Run validation: `./scripts/validate.sh`

## Why This Matters

This repository is designed for **Agentic Coding** where multiple AI agents work in parallel. These protocols ensure:

- **Consistency**: All agents follow the same rules
- **Quality**: Code is tested and documented
- **Continuity**: Context is preserved between sessions
- **Safety**: Decisions are researched and validated
