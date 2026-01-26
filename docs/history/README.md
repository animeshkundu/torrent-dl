# History & Handoffs

This directory maintains records of significant changes, handoffs between agents, and deprecated logic.

## Purpose

- **Continuity**: Track context across agent sessions
- **Learning**: Document what worked and what didn't
- **Archaeology**: Understand why code exists in its current form

## For AI Agents

### Recording Handoffs

When completing a task, create a handoff document:

```markdown
# Handoff: [Task Description]

## Date
YYYY-MM-DD

## Agent/Author
[Agent ID or Human Author]

## Completed Work
- [What was accomplished]
- [Key files modified]

## Open Items
- [What remains to be done]
- [Known issues]

## Context for Next Agent
- [Important decisions made]
- [Gotchas discovered]
- [Recommendations]

## References
- [Related PRs/Issues]
- [Related specs/ADRs]
```

### Recording Deprecated Logic

When deprecating code, document:

```markdown
# Deprecated: [Component/Feature Name]

## Date Deprecated
YYYY-MM-DD

## Reason
[Why this was deprecated]

## Replacement
[What to use instead]

## Migration Guide
[How to migrate]

## Removal Timeline
[When this will be removed]
```

## File Naming Convention

- `YYYY-MM-DD-handoff-description.md` - Handoff records
- `YYYY-MM-DD-deprecated-component.md` - Deprecation notices
- `YYYY-MM-DD-incident-description.md` - Post-incident reviews

## Archive Policy

- Handoffs older than 1 year may be archived
- Deprecation notices remain until code is removed
- Incident reports are kept indefinitely

## Related Documentation

- See `docs/adrs/` for architectural decisions
- See `docs/specs/` for feature specifications
