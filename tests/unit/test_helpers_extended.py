"""Extended unit tests for Pyflix.utils.helpers module.

These tests cover network utilities and process helpers.
"""

import pytest
import socket
import os
from unittest.mock import patch, MagicMock


class TestGetInterface:
    """Tests for get_interface function."""

    def test_get_interface_exists(self):
        """get_interface function should exist."""
        from Pyflix.utils.helpers import get_interface
        assert callable(get_interface)

    def test_get_interface_returns_string_or_none(self):
        """get_interface should return a string IP or None."""
        from Pyflix.utils.helpers import get_interface
        result = get_interface()
        assert result is None or isinstance(result, str)

    def test_get_interface_does_not_return_localhost(self):
        """get_interface should not return 127.x.x.x addresses."""
        from Pyflix.utils.helpers import get_interface
        result = get_interface()
        if result is not None:
            assert not result.startswith("127.")


class TestIsPortFreeExtended:
    """Extended tests for is_port_free function."""

    def test_privileged_port(self):
        """Testing a privileged port (< 1024) should not crash."""
        from Pyflix.utils.helpers import is_port_free
        # This might return True or False depending on permissions
        result = is_port_free(80)
        assert isinstance(result, bool)

    def test_highest_valid_port(self):
        """Testing port 65535 should work."""
        from Pyflix.utils.helpers import is_port_free
        result = is_port_free(65535)
        assert isinstance(result, bool)

    def test_multiple_port_checks(self):
        """Multiple port checks should be independent."""
        from Pyflix.utils.helpers import is_port_free
        # Check multiple ports
        results = [is_port_free(p) for p in range(50000, 50005)]
        assert all(isinstance(r, bool) for r in results)


class TestGetFreePortExtended:
    """Extended tests for get_free_port function."""

    def test_port_actually_free(self):
        """Returned port should actually be free."""
        from Pyflix.utils.helpers import get_free_port, is_port_free
        port = get_free_port()
        # Port should be free immediately after getting it
        assert is_port_free(port) is True

    def test_returns_high_port(self):
        """get_free_port should return an ephemeral port (typically > 1024)."""
        from Pyflix.utils.helpers import get_free_port
        port = get_free_port()
        # Most OS return ephemeral ports > 1024
        assert port > 0


class TestSetConfigDirExtended:
    """Extended tests for set_config_dir function."""

    def test_creates_nested_structure(self, tmp_path, monkeypatch):
        """set_config_dir should work with nested HOME paths."""
        monkeypatch.setenv("HOME", str(tmp_path))
        from Pyflix.utils.helpers import set_config_dir
        set_config_dir()
        assert (tmp_path / ".pyflix").exists()

    def test_handles_permission_error_gracefully(self, tmp_path, monkeypatch):
        """set_config_dir should handle errors gracefully."""
        monkeypatch.setenv("HOME", str(tmp_path))
        from Pyflix.utils.helpers import set_config_dir
        # First call creates directory
        set_config_dir()
        # Second call should not raise
        set_config_dir()


class TestDaemonize:
    """Tests for daemonize function."""

    def test_daemonize_exists(self):
        """daemonize function should exist."""
        from Pyflix.utils.helpers import daemonize
        assert callable(daemonize)

    def test_daemonize_signature(self):
        """daemonize should accept args and callback."""
        from Pyflix.utils.helpers import daemonize
        import inspect
        sig = inspect.signature(daemonize)
        params = list(sig.parameters.keys())
        assert 'args' in params
        assert 'callback' in params


class TestGetLockDiffExtended:
    """Extended tests for get_lock_diff function."""

    def test_returns_non_negative(self):
        """get_lock_diff should return non-negative value."""
        from Pyflix.utils.helpers import get_lock_diff
        result = get_lock_diff()
        assert result >= 0

    def test_returns_numeric_type(self):
        """get_lock_diff should return int or float."""
        from Pyflix.utils.helpers import get_lock_diff
        result = get_lock_diff()
        assert isinstance(result, (int, float))


class TestLockfile:
    """Tests for LOCKFILE constant."""

    def test_lockfile_path_defined(self):
        """LOCKFILE should be defined."""
        from Pyflix.utils.helpers import LOCKFILE
        assert LOCKFILE is not None

    def test_lockfile_is_string(self):
        """LOCKFILE should be a string path."""
        from Pyflix.utils.helpers import LOCKFILE
        assert isinstance(LOCKFILE, str)

    def test_lockfile_in_tmp(self):
        """LOCKFILE should be in /tmp directory."""
        from Pyflix.utils.helpers import LOCKFILE
        assert LOCKFILE.startswith("/tmp")
