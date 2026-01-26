#!/bin/bash
# scripts/lint.sh
#
# Run linters on the codebase
#
# Usage: ./scripts/lint.sh
#
# Exit codes:
#   0 - No lint errors
#   1 - Lint errors found

set -e

echo "Running Ruff linter..."
ruff check .

echo ""
echo "Checking code formatting with Black..."
black --check --diff .

echo ""
echo "✓ All lint checks passed!"
