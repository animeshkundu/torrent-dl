# 03: Tooling and Pipelines

This document defines automation, scripting, and CI/CD requirements for the repository.

---

## 🔧 Tool Creation Protocol

> **IF YOU DO IT TWICE, AUTOMATE IT**

### The Rule

If an AI agent performs a verification or repetitive task more than once, they MUST:
1. Write a script to automate it
2. Place it in `scripts/`
3. Document its usage
4. Update this document if it's a common tool

### Script Requirements

Every script must:
- Be executable (`chmod +x`)
- Have a shebang (`#!/bin/bash` or `#!/usr/bin/env python3`)
- Include usage documentation
- Return appropriate exit codes
- Handle errors gracefully

### Script Template

```bash
#!/bin/bash
# scripts/example-task.sh
#
# Description: [What this script does]
# Usage: ./scripts/example-task.sh [args]
#
# Exit codes:
#   0 - Success
#   1 - General error
#   2 - Invalid arguments

set -e  # Exit on error
set -u  # Error on undefined variables

# Script logic here

echo "Task completed successfully"
exit 0
```

---

## 📁 Scripts Directory

### Standard Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `validate.sh` | Full validation (lint, test, coverage) | `./scripts/validate.sh` |
| `lint.sh` | Run linters only | `./scripts/lint.sh` |
| `test.sh` | Run tests with coverage | `./scripts/test.sh` |
| `setup-dev.sh` | Set up development environment | `./scripts/setup-dev.sh` |

### Creating New Scripts

1. **Name clearly**: `verb-noun.sh` (e.g., `check-types.sh`)
2. **Document usage**: In script header and README
3. **Test locally**: Ensure it works before committing
4. **Integrate with CI**: Add to workflows if appropriate

---

## 🔄 CI/CD Priority

> **GITHUB ACTIONS IS THE SOURCE OF TRUTH**

### Workflow Hierarchy

1. **CI (Continuous Integration)**: `ci.yml`
   - Runs on every PR and push
   - Lint → Test → Coverage → Security

2. **CD (Continuous Deployment)**: `deploy.yml` (if applicable)
   - Runs on release tags
   - Build → Test → Deploy

### Workflow Standards

Every workflow must:
- Run on `ubuntu-latest` (unless platform-specific)
- Cache dependencies for speed
- Fail fast on lint errors
- Report coverage to codecov or similar
- Include security scanning

---

## 📋 Workflow Template

### CI Workflow Structure

```yaml
name: CI

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install linters
        run: pip install ruff black
      - name: Run Ruff
        run: ruff check .
      - name: Check formatting
        run: black --check .

  test:
    runs-on: ubuntu-latest
    needs: lint  # Only test if lint passes
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest --cov=Pyflix --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v4

  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Bandit
        run: |
          pip install bandit
          bandit -r Pyflix -f json -o bandit-report.json || true
      - name: Upload Bandit report
        uses: actions/upload-artifact@v4
        with:
          name: bandit-report
          path: bandit-report.json
```

---

## 🛠️ Required Tools

### Linting & Formatting

| Tool | Purpose | Installation |
|------|---------|--------------|
| ruff | Fast Python linter | `pip install ruff` |
| black | Code formatter | `pip install black` |
| isort | Import sorter | `pip install isort` |
| mypy | Type checker | `pip install mypy` |

### Testing

| Tool | Purpose | Installation |
|------|---------|--------------|
| pytest | Test runner | `pip install pytest` |
| pytest-cov | Coverage plugin | `pip install pytest-cov` |
| pytest-mock | Mocking plugin | `pip install pytest-mock` |

### Security

| Tool | Purpose | Installation |
|------|---------|--------------|
| bandit | Security linter | `pip install bandit` |
| safety | Dependency checker | `pip install safety` |

---

## 🔐 Security Scanning

### Required Scans

1. **Static Analysis**: Bandit for Python code
2. **Dependency Scanning**: Safety or GitHub Dependabot
3. **Code Scanning**: CodeQL for comprehensive analysis

### Integration Points

```yaml
# In CI workflow
security:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: python
    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v3
```

---

## 📦 Dependency Management

### Requirements Files

- `requirements.txt` - Production dependencies
- `requirements-dev.txt` - Development dependencies
- `requirements-test.txt` - Test dependencies

### Best Practices

1. **Pin versions**: `package==1.2.3`, not `package>=1.0`
2. **Audit regularly**: Run `pip-audit` or `safety check`
3. **Use dependabot**: Enable automatic security updates
4. **Document updates**: Note why dependencies changed

---

## 🚀 Local Development Setup

### One-Command Setup

```bash
# Clone and setup
git clone <repo>
cd torrent-dl
./scripts/setup-dev.sh

# Activate virtual environment
source venv/bin/activate

# Run validation
./scripts/validate.sh
```

### setup-dev.sh Contents

```bash
#!/bin/bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks (optional)
pre-commit install

echo "Development environment ready!"
```

---

## 📝 Pipeline Documentation

### Documenting Workflows

Every workflow file should include:
- Comment header explaining purpose
- Documentation of required secrets
- Link to relevant documentation

```yaml
# .github/workflows/ci.yml
#
# Continuous Integration workflow for torrent-dl
#
# Triggers: Push to main/master, Pull requests
# Required secrets: CODECOV_TOKEN (optional for public repos)
#
# Related docs: docs/agent-instructions/03-tooling-and-pipelines.md
```

---

## 🎯 For AI Agents

### When Creating Tools

1. Check if a similar tool exists
2. Follow the script template
3. Document thoroughly
4. Test locally before committing
5. Add to CI if appropriate

### When Modifying CI

1. Test workflow locally with `act` if possible
2. Make changes incrementally
3. Ensure backward compatibility
4. Update this documentation

### Validation Checklist

Before committing any automation:

- [ ] Script is executable
- [ ] Script has documentation
- [ ] Script handles errors
- [ ] CI workflow is valid YAML
- [ ] Workflow tested on a branch first

---

*Automation is investment. Time spent creating tools pays dividends in reliability and speed. Automate relentlessly.*
