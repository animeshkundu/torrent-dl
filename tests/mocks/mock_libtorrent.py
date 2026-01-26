"""Mock libtorrent module for testing without the actual library.

This file re-exports everything from the __init__.py mock implementation.
See tests/mocks/__init__.py for the actual mock implementation.
"""

# Re-export everything from the main mock module
from tests.mocks import (
    version,
    storage_mode_t,
    MockTorrentInfo,
    MockTorrentStatus,
    MockTorrentHandle,
    MockSession,
    session,
    add_magnet_uri,
)

__all__ = [
    'version',
    'storage_mode_t',
    'MockTorrentInfo',
    'MockTorrentStatus',
    'MockTorrentHandle',
    'MockSession',
    'session',
    'add_magnet_uri',
]
