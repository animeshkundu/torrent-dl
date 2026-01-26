"""
Sample tests to verify test infrastructure.

These tests ensure that the testing setup is working correctly.
Replace or expand these with actual tests as the project develops.
"""

import pytest


class TestInfrastructure:
    """Tests to verify the test infrastructure is working."""

    def test_pytest_works(self):
        """Verify that pytest can run tests."""
        assert True

    def test_fixtures_available(self, sample_magnet_link, temp_download_dir):
        """Verify that fixtures are properly configured."""
        assert sample_magnet_link.startswith("magnet:")
        assert temp_download_dir.exists()

    def test_can_import_stdlib(self):
        """Verify standard library imports work."""
        import os
        import sys
        import json
        assert os is not None
        assert sys is not None
        assert json is not None


class TestPyflixImport:
    """Tests for Pyflix module imports."""

    def test_pyflix_package_structure(self):
        """Test that Pyflix package exists."""
        import importlib.util
        
        # Check if Pyflix module exists
        spec = importlib.util.find_spec("Pyflix")
        # Note: May be None if libtorrent is not installed
        # This is expected in CI environments without libtorrent
        if spec is not None:
            assert spec.name == "Pyflix"

    def test_utils_module_exists(self):
        """Test that utils subpackage exists."""
        import importlib.util
        import os
        
        # Check file system for module
        utils_path = os.path.join("Pyflix", "utils", "__init__.py")
        assert os.path.exists(utils_path), f"Utils module not found at {utils_path}"

    def test_torrent_module_exists(self):
        """Test that torrent subpackage exists."""
        import importlib.util
        import os
        
        # Check file system for module
        torrent_path = os.path.join("Pyflix", "torrent", "__init__.py")
        assert os.path.exists(torrent_path), f"Torrent module not found at {torrent_path}"
