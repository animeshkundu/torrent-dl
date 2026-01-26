#!/bin/bash
# scripts/test.sh
#
# Run tests with coverage
#
# Usage: ./scripts/test.sh [pytest args]
#
# Examples:
#   ./scripts/test.sh                    # Run all tests
#   ./scripts/test.sh -v                 # Verbose output
#   ./scripts/test.sh -k "test_name"     # Run specific test
#   ./scripts/test.sh --cov-report=html  # Generate HTML coverage report

set -e

# Default coverage threshold
COVERAGE_THRESHOLD=${COVERAGE_THRESHOLD:-90}

echo "Running tests with coverage..."
echo "Coverage threshold: ${COVERAGE_THRESHOLD}%"
echo ""

# Run pytest with coverage
pytest \
    --cov=Pyflix \
    --cov-report=term-missing \
    --cov-fail-under=${COVERAGE_THRESHOLD} \
    "$@"

echo ""
echo "✓ Tests passed with coverage >= ${COVERAGE_THRESHOLD}%"
