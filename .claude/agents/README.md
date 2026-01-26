# Claude Agents Configuration

This directory is a placeholder for Claude-specific agent configurations.

## Purpose

This directory will contain configurations for Claude AI agents, including:
- Specialized agent personas
- Task-specific system prompts
- Agent capability definitions
- Project-specific knowledge

## Structure (Planned)

```
.claude/agents/
├── README.md                 # This file
├── code-assistant.md         # Code assistance agent
├── documentation.md          # Documentation agent
├── code-review.md            # Code review agent
└── testing.md                # Test generation agent
```

## Current Status

This directory is currently empty except for this README. Agent configurations will be added as Claude's agentic capabilities expand.

## Related Documentation

- See `docs/agent-instructions/` for agent behavior protocols
- See `claude.md` in the repository root for Claude instructions

## Agent Design Principles

When creating Claude agents for this project:

1. **Follow Core Philosophy**: All agents must adhere to `docs/agent-instructions/00-core-philosophy.md`
2. **Documentation First**: Agents should prioritize documentation before code
3. **Research Enabled**: Agents should use web search for verification
4. **Test Driven**: Agents must write tests for their code

## Contributing

When adding new agent configurations:
1. Follow the naming convention: `purpose.md`
2. Include clear scope and limitations
3. Reference relevant documentation
4. Test thoroughly before committing
