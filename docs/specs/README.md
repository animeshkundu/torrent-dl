# Technical Specifications

This directory contains technical specifications for features and components of the torrent-dl project.

## Purpose

Technical specifications document the detailed design of features **before** implementation begins. This is a critical part of the "Docs = Code" philosophy.

## For AI Agents: MANDATORY WORKFLOW

> ⚠️ **NO CODE WITHOUT SPEC** ⚠️
>
> AI agents MUST write or update a specification in this directory BEFORE writing any code.

### Workflow

1. **Receive task** → Read existing specs for context
2. **Plan implementation** → Write or update spec document
3. **Get spec reviewed** → Ensure clarity and completeness
4. **Implement code** → Reference spec in commits
5. **Update spec** → Reflect any implementation changes

## Specification Template

Each spec should include:

```markdown
# Spec: [Feature Name]

## Overview
[Brief description of what this feature does]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2

## Technical Design
[Detailed technical approach]

## API/Interface
[Public interfaces exposed by this feature]

## Dependencies
[External libraries, internal modules]

## Testing Strategy
[How this will be tested]

## Security Considerations
[Any security implications]

## Performance Considerations
[Any performance implications]
```

## Naming Convention

- `feature-name-spec.md` - Feature specifications
- `refactor-description-spec.md` - Refactoring specifications
- `bugfix-issue-number-spec.md` - Bug fix specifications

## Example Specs

- `torrent-download-spec.md` - Core download functionality
- `media-streaming-spec.md` - VLC streaming integration

## Validation

Specs are living documents. After implementation:
1. Update the spec with any deviations
2. Mark requirements as completed
3. Add learnings for future reference
