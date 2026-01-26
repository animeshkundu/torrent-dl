# GitHub Agents Configuration

This directory is a placeholder for GitHub-native agent configurations.

## Purpose

As GitHub expands its AI agent capabilities, this directory will contain:
- Agent persona definitions
- Task-specific agent configurations
- Agent permission scopes
- Workflow integrations

## Structure (Planned)

```
.github/agents/
├── README.md                 # This file
├── code-review.yml           # Code review agent config
├── documentation.yml         # Documentation agent config
├── security.yml              # Security review agent config
└── testing.yml               # Test generation agent config
```

## Current Status

This directory is currently empty except for this README. As GitHub releases native agent configuration support, this directory will be populated with appropriate configurations.

## Related Documentation

- See `docs/agent-instructions/` for agent behavior protocols
- See `.github/copilot-instructions.md` for Copilot configuration

## Contributing

When GitHub announces agent configuration formats:
1. Create agents following our established protocols
2. Document each agent's purpose and scope
3. Test agents in a non-production environment first
4. Ensure agents follow `docs/agent-instructions/`
