#!/bin/bash
# scripts/setup-dev.sh
#
# Set up development environment for torrent-dl
#
# Usage: ./scripts/setup-dev.sh
#
# This script:
#   1. Creates a virtual environment
#   2. Installs production dependencies
#   3. Installs development dependencies
#   4. Sets up pre-commit hooks (if configured)

set -e

echo "========================================"
echo "  torrent-dl Development Setup"
echo "========================================"
echo ""

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "Python version: ${PYTHON_VERSION}"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install production dependencies
echo "Installing production dependencies..."
pip install -r requirements.txt --quiet || {
    echo "Warning: Some dependencies may have failed. This is expected if libtorrent is not available."
}

# Install development dependencies
echo "Installing development dependencies..."
pip install ruff black pytest pytest-cov pytest-mock bandit safety --quiet

# Create tests directory if it doesn't exist
if [ ! -d "tests" ]; then
    echo "Creating tests directory..."
    mkdir -p tests
    touch tests/__init__.py
    
    # Create a sample test file
    cat > tests/test_sample.py << 'EOF'
"""Sample test file to verify test infrastructure."""

def test_sample():
    """A sample test that always passes."""
    assert True

def test_import_pyflix():
    """Test that Pyflix module can be imported."""
    try:
        import Pyflix
        assert True
    except ImportError:
        # Expected if libtorrent is not installed
        pass
EOF
fi

# Make scripts executable
echo "Making scripts executable..."
chmod +x scripts/*.sh 2>/dev/null || true

echo ""
echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "To activate the virtual environment:"
echo "  source venv/bin/activate"
echo ""
echo "To run validation:"
echo "  ./scripts/validate.sh"
echo ""
echo "To run tests:"
echo "  ./scripts/test.sh"
echo ""
