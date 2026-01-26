# Claude AI Instructions for torrent-dl

This file provides repository-level instructions for Claude and other AI coding assistants working on the torrent-dl project.

---

## ⚠️ MANDATORY: Read Before Any Action

Before answering ANY request or making ANY code change, you MUST:

1. **Read Agent Instructions**: `docs/agent-instructions/`
   - Start with `00-core-philosophy.md`
   - This defines the workflow you MUST follow

2. **Check ADRs**: `docs/adrs/`
   - Review past architectural decisions
   - Avoid proposing changes that contradict existing decisions

3. **Review Specifications**: `docs/specs/`
   - Check if a spec exists for the area you're modifying
   - If not, create one before writing code

4. **Understand Architecture**: `docs/architecture/`
   - Review system diagrams
   - Understand how components interact

---

## Project Overview

**torrent-dl** is a Python library and CLI tool for watching and downloading torrents simultaneously. It combines BitTorrent downloading capabilities with media streaming functionality.

### Tech Stack

- **Language**: Python 3.x
- **Core Library**: libtorrent-rasterbar (via python-libtorrent)
- **Media Playback**: VLC Player
- **Package Manager**: pip

### Project Structure

```
torrent-dl/
├── Pyflix/                 # Main package
│   ├── __init__.py         # Entry point and CLI
│   ├── torrent/            # Torrent engine
│   │   ├── __init__.py     # Download manager
│   │   ├── strategy.py     # Download strategy
│   │   └── moov.py         # MP4 atom handling
│   └── utils/              # Utilities
│       ├── logger.py       # Logging
│       ├── settings.py     # Configuration
│       ├── streamer.py     # HTTP streaming
│       └── ...             # Other utilities
├── docs/                   # Documentation (READ THIS)
│   ├── agent-instructions/ # Agent protocols (MANDATORY)
│   ├── adrs/               # Architecture decisions
│   ├── specs/              # Technical specifications
│   ├── architecture/       # System diagrams
│   └── history/            # Handoffs and history
├── scripts/                # Automation scripts
├── tests/                  # Test suite
└── requirements.txt        # Dependencies
```

---

## Coding Standards

### Style

- Follow PEP 8 for Python code
- Use type hints for all function signatures
- Use docstrings for all public functions and classes
- Maximum line length: 100 characters

### Naming Conventions

- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_SNAKE_CASE` for constants
- Prefix private methods with underscore: `_private_method`

### Documentation

- Every public function needs a docstring
- Complex logic needs inline comments
- Update `docs/` when making changes

---

## Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python -m torrent-dl <magnet_link>

# Run validation (lint + test)
./scripts/validate.sh

# Run tests with coverage
pytest --cov=Pyflix --cov-report=term-missing

# Run linter
ruff check .
black --check .
```

---

## Critical Rules

### 1. Documentation First

> **NO CODE WITHOUT DOCUMENTATION**

Before writing code:
1. Check if a spec exists in `docs/specs/`
2. If not, write one first
3. Update spec after implementation

### 2. Test Everything

> **90% MINIMUM CODE COVERAGE**

- Write tests before or with implementation
- All new code must have tests
- Run `./scripts/validate.sh` before committing

### 3. Research Before Implementing

> **DO NOT HALLUCINATE APIs**

- If unsure about an API, search for documentation
- Verify library versions and compatibility
- Check for security advisories

### 4. Respect Architecture Decisions

> **CHECK ADRs BEFORE PROPOSING CHANGES**

- Read `docs/adrs/` for past decisions
- If your change contradicts an ADR, discuss first
- Create new ADR for significant architectural changes

---

## Restrictions

### Never Modify

- Configuration files with secrets (if any)
- Third-party vendored code
- Build artifacts

### Always Check Before Modifying

- Core torrent engine (`Pyflix/torrent/`)
- Public API signatures
- Configuration schema

---

## Getting Help

- **Architecture Questions**: See `docs/architecture/system-overview.md`
- **Past Decisions**: See `docs/adrs/`
- **Feature Specs**: See `docs/specs/`
- **Agent Protocols**: See `docs/agent-instructions/`

---

## Update Protocol

After completing any work:

1. Update relevant documentation
2. Create handoff in `docs/history/`
3. Run validation: `./scripts/validate.sh`
4. Ensure tests pass and coverage meets requirements

---

*This file is synchronized with `.github/copilot-instructions.md`. Keep them consistent.*
