"""
Pytest configuration and shared fixtures for torrent-dl tests.

This file contains fixtures that are available to all tests in the test suite.
Add common test utilities and fixtures here.
"""

import sys
import pytest

# Install mock libtorrent BEFORE any Pyflix imports
# This is critical for testing without the actual libtorrent library
from tests import mocks

sys.modules['libtorrent'] = mocks


@pytest.fixture
def sample_magnet_link():
    """Provide a sample magnet link for testing.
    
    Note: This is a fake magnet link for testing purposes only.
    Do not use real magnet links in tests.
    """
    return "magnet:?xt=urn:btih:0000000000000000000000000000000000000000&dn=test"


@pytest.fixture
def temp_download_dir(tmp_path):
    """Provide a temporary directory for download tests.
    
    This directory is automatically cleaned up after each test.
    """
    download_dir = tmp_path / "downloads"
    download_dir.mkdir()
    return download_dir
