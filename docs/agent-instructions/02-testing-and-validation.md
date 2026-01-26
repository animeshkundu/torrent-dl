# 02: Testing and Validation

This document defines the testing requirements and validation protocols for all code changes.

---

## 📊 The 90% Rule

> **MINIMUM 90% CODE COVERAGE FOR ALL NEW CODE**

This is not a guideline—it is a requirement. All new code must have:
- **Unit test coverage**: ≥90%
- **Integration test coverage**: ≥90% for public APIs
- **Edge case coverage**: All identified edge cases must be tested

### Why 90%?

- **Quality Assurance**: High coverage catches regressions
- **Documentation**: Tests serve as executable documentation
- **Confidence**: Enables aggressive refactoring
- **Agent Collaboration**: Future agents can safely modify tested code

### Calculating Coverage

```bash
# Run tests with coverage
pytest --cov=Pyflix --cov-report=term-missing

# Generate HTML report for detailed analysis
pytest --cov=Pyflix --cov-report=html
```

---

## 🎯 Test-Driven Development

> **WRITE TESTS BEFORE OR WITH IMPLEMENTATION**

### The TDD Protocol

```
1. Write a failing test that defines desired behavior
      ↓
2. Write minimal code to make the test pass
      ↓
3. Refactor code while keeping tests green
      ↓
4. Add edge case tests
      ↓
5. Ensure coverage meets requirements
```

### Test Categories

| Category | Purpose | Location |
|----------|---------|----------|
| Unit Tests | Test individual functions/classes | `tests/unit/` |
| Integration Tests | Test component interactions | `tests/integration/` |
| End-to-End Tests | Test full user workflows | `tests/e2e/` |

### Test Naming Convention

```python
# Pattern: test_<function>_<scenario>_<expected_behavior>

def test_download_manager_valid_magnet_starts_download():
    """Test that a valid magnet link initiates download."""
    pass

def test_download_manager_invalid_magnet_raises_error():
    """Test that an invalid magnet link raises ValueError."""
    pass

def test_download_manager_network_failure_retries():
    """Test that network failures trigger retry logic."""
    pass
```

---

## 🔄 Self-Correction Protocol

> **ALWAYS VERIFY YOUR OWN WORK BEFORE COMMITTING**

### Pre-Commit Validation

Before any commit, run:

```bash
# Full validation script
./scripts/validate.sh

# Or manually:
# 1. Lint check
ruff check .
black --check .

# 2. Type check (if applicable)
mypy Pyflix

# 3. Run tests with coverage
pytest --cov=Pyflix --cov-fail-under=90

# 4. Security scan
bandit -r Pyflix
```

### The Validation Loop

```
Make code change
      ↓
Run tests locally → Fail? → Fix and retry
      ↓
Check coverage → Below 90%? → Add tests and retry
      ↓
Run linter → Errors? → Fix and retry
      ↓
All pass? → Commit
```

---

## 📋 Test Checklist

### For Every New Function

- [ ] Unit test for happy path
- [ ] Unit test for error conditions
- [ ] Unit test for edge cases
- [ ] Unit test for boundary values
- [ ] Docstring with usage example

### For Every Bug Fix

- [ ] Regression test that fails before fix
- [ ] Test passes after fix
- [ ] No existing tests broken

### For Every Refactor

- [ ] All existing tests still pass
- [ ] Coverage does not decrease
- [ ] No new warnings introduced

---

## 🧪 Testing Best Practices

### Test Isolation

Each test must:
- Run independently
- Not depend on test execution order
- Clean up any resources it creates
- Use fixtures for shared setup

### Mocking Guidelines

```python
# Good: Mock external dependencies
@patch('Pyflix.torrent.libtorrent.session')
def test_download_manager_initializes_session(mock_session):
    """Test that download manager creates libtorrent session."""
    manager = DownloadManager("magnet:?...")
    mock_session.assert_called_once()

# Bad: Mock internal implementation details
# This makes tests brittle and couples them to implementation
```

### What to Mock

✅ **Do Mock:**
- External APIs (libtorrent, network calls)
- File system operations
- Time-dependent operations
- Random number generators

❌ **Don't Mock:**
- The code you're testing
- Pure functions
- Simple data transformations

---

## 📈 Coverage Reports

### Reading Coverage Reports

```
Name                          Stmts   Miss  Cover   Missing
------------------------------------------------------------
Pyflix/__init__.py               25      2    92%   28, 31
Pyflix/torrent/__init__.py       89     10    89%   45-48, 92-95
Pyflix/utils/helpers.py          45      0   100%
------------------------------------------------------------
TOTAL                           159     12    92%
```

### Addressing Missing Coverage

1. Identify uncovered lines
2. Determine if they are:
   - **Testable**: Write tests
   - **Dead code**: Remove
   - **Error handlers**: Simulate error conditions
3. Do NOT add `# pragma: no cover` without justification

### Acceptable Uncovered Code

Some code may be exempt from coverage:
- CLI entry points (tested via integration tests)
- Error messages that can't be triggered
- Platform-specific fallbacks

Always document exemptions:
```python
if __name__ == "__main__":  # pragma: no cover
    # Entry point - tested via integration tests
    main()
```

---

## 🚨 Test Failure Protocol

### When Tests Fail

1. **Don't panic**: Failing tests are information
2. **Read the error**: Understand what's actually failing
3. **Reproduce locally**: Run the specific failing test
4. **Analyze the cause**:
   - Is your change wrong?
   - Is the test wrong?
   - Is it a flaky test?
5. **Fix appropriately**: Code or test, not both simultaneously

### Flaky Tests

If you encounter a flaky test:
1. Document the flakiness
2. Create an issue for investigation
3. Do NOT delete or skip the test
4. Consider retry mechanisms for inherently non-deterministic tests

---

## 📝 Test Documentation

### Every Test Should Have

```python
def test_function_name():
    """
    Test that [specific behavior] occurs when [specific condition].
    
    Given: [Initial state/setup]
    When: [Action taken]
    Then: [Expected outcome]
    """
    # Arrange
    ...
    # Act
    ...
    # Assert
    ...
```

### Test Organization

```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures
├── unit/
│   ├── __init__.py
│   ├── test_download_manager.py
│   ├── test_strategy.py
│   └── test_helpers.py
├── integration/
│   ├── __init__.py
│   └── test_full_download.py
└── e2e/
    ├── __init__.py
    └── test_cli.py
```

---

*Testing is not overhead. It is the foundation that enables confident, rapid development. Every line of code deserves tests.*
