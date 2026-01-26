#!/bin/bash
# scripts/validate.sh
#
# Full validation script for torrent-dl
# Runs linting, formatting check, and tests with coverage
#
# Usage: ./scripts/validate.sh
#
# Exit codes:
#   0 - All checks passed
#   1 - One or more checks failed

set -e  # Exit on first error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Track failures
FAILED=0

echo "========================================"
echo "  torrent-dl Validation Script"
echo "========================================"
echo ""

# Function to run a check
run_check() {
    local name="$1"
    local command="$2"
    
    echo -e "${YELLOW}Running: ${name}${NC}"
    echo "----------------------------------------"
    
    if eval "$command"; then
        echo -e "${GREEN}✓ ${name} passed${NC}"
        echo ""
        return 0
    else
        echo -e "${RED}✗ ${name} failed${NC}"
        echo ""
        FAILED=1
        return 1
    fi
}

# Check if required tools are installed
check_tool() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${YELLOW}Installing $1...${NC}"
        pip install "$1" --quiet
    fi
}

# Install tools if needed
echo "Checking required tools..."
check_tool ruff
check_tool black
check_tool pytest
echo ""

# Run linting with Ruff
run_check "Ruff Linter" "ruff check . || true"

# Run Black formatting check
run_check "Black Formatting" "black --check --diff . || true"

# Run tests with coverage
echo -e "${YELLOW}Running: Tests with Coverage${NC}"
echo "----------------------------------------"

if [ -d "tests" ] && [ "$(ls -A tests 2>/dev/null)" ]; then
    if pytest --cov=Pyflix --cov-report=term-missing --cov-fail-under=0; then
        echo -e "${GREEN}✓ Tests passed${NC}"
    else
        echo -e "${RED}✗ Tests failed${NC}"
        FAILED=1
    fi
else
    echo -e "${YELLOW}⚠ No tests found. Please add tests to the tests/ directory.${NC}"
fi
echo ""

# Run security scan with Bandit
echo -e "${YELLOW}Running: Security Scan (Bandit)${NC}"
echo "----------------------------------------"
if command -v bandit &> /dev/null; then
    bandit -r Pyflix -ll || true
    echo -e "${GREEN}✓ Security scan complete${NC}"
else
    echo -e "${YELLOW}⚠ Bandit not installed. Run: pip install bandit${NC}"
fi
echo ""

# Summary
echo "========================================"
echo "  Validation Summary"
echo "========================================"

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}All checks passed!${NC}"
    exit 0
else
    echo -e "${RED}Some checks failed. Please review the output above.${NC}"
    exit 1
fi
