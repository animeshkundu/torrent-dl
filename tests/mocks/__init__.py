"""Mock libtorrent module for testing without the actual library.

This module provides mock implementations of libtorrent's core classes
and functions to enable testing the application logic without requiring
the actual libtorrent library (which requires system-level installation).

Usage:
    import sys
    from tests.mocks import mock_libtorrent
    sys.modules['libtorrent'] = mock_libtorrent
"""

from unittest.mock import MagicMock
from enum import IntEnum


# Version info
version = "2.0.0-mock"


class storage_mode_t(IntEnum):
    """Mock storage mode enumeration."""
    storage_mode_allocate = 0
    storage_mode_sparse = 1
    storage_mode_compact = 2


class MockTorrentInfo:
    """Mock torrent info object."""
    
    def __init__(self, num_files=1, piece_length=16384):
        self._files = []
        self._piece_length = piece_length
        for i in range(num_files):
            file_info = MagicMock()
            file_info.path = f"test_video_{i}.mp4"
            file_info.size = 100 * 1024 * 1024  # 100 MB
            self._files.append(file_info)
    
    def files(self):
        return self._files
    
    def piece_length(self):
        return self._piece_length
    
    def num_pieces(self):
        return 100


class MockTorrentStatus:
    """Mock torrent status object."""
    
    def __init__(self):
        self.state = 3  # Downloading
        self.progress = 0.5
        self.download_rate = 1024 * 500  # 500 KB/s
        self.upload_rate = 1024 * 100  # 100 KB/s
        self.num_peers = 10
        self.pieces = [True] * 50 + [False] * 50  # 50% downloaded


class MockTorrentHandle:
    """Mock torrent handle."""
    
    def __init__(self):
        self._status = MockTorrentStatus()
        self._info = MockTorrentInfo()
        self._metadata = True
        self._seed = False
        self._sequential = False
        self._priorities = {}
        self._deadlines = {}
        self._download_queue = []
    
    def status(self):
        return self._status
    
    def get_torrent_info(self):
        return self._info
    
    def has_metadata(self):
        return self._metadata
    
    def is_seed(self):
        return self._seed
    
    def set_sequential_download(self, value):
        self._sequential = value
    
    def piece_priority(self, index, priority=None):
        if priority is not None:
            self._priorities[index] = priority
        return self._priorities.get(index, 1)
    
    def set_piece_deadline(self, index, deadline):
        self._deadlines[index] = deadline
    
    def set_upload_limit(self, limit):
        pass
    
    def set_download_limit(self, limit):
        pass
    
    def get_download_queue(self):
        return self._download_queue


class MockSession:
    """Mock libtorrent session."""
    
    def __init__(self):
        self._handles = []
    
    def listen_on(self, port_from, port_to):
        pass
    
    def start_dht(self):
        pass
    
    def add_torrent(self, params):
        handle = MockTorrentHandle()
        self._handles.append(handle)
        return handle


def session():
    """Create a mock session."""
    return MockSession()


def add_magnet_uri(sess, magnet, params):
    """Add a magnet URI to a session."""
    return MockTorrentHandle()
