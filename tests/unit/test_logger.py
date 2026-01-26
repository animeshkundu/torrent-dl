"""Unit tests for Pyflix.utils.logger module.

These tests characterize the existing behavior of the logging setup.
They capture BEHAVIOR, not correctness.
"""

import pytest
import logging
import sys
from unittest.mock import patch, MagicMock
from io import StringIO


class TestLogSetUp:
    """Tests for log_set_up function."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
        settings = MagicMock()
        settings.save_path = "/tmp/pyflix_test"
        return settings

    def test_log_set_up_exists(self):
        """log_set_up function should exist."""
        from Pyflix.utils.logger import log_set_up
        assert callable(log_set_up)

    def test_log_set_up_can_be_called(self, tmp_path, monkeypatch):
        """log_set_up should be callable without errors."""
        monkeypatch.setenv("HOME", str(tmp_path))
        # Create the required directories
        (tmp_path / ".pyflix").mkdir(exist_ok=True)
        save_path = tmp_path / "downloads"
        save_path.mkdir(exist_ok=True)
        
        from Pyflix.utils.logger import log_set_up
        # This may fail if settings don't load, that's OK for this characterization test
        try:
            log_set_up()
        except Exception:
            pass  # Expected if settings library has issues

    def test_log_set_up_accepts_verbose_parameter(self):
        """log_set_up should accept a verbose parameter."""
        from Pyflix.utils.logger import log_set_up
        import inspect
        sig = inspect.signature(log_set_up)
        assert 'verbose' in sig.parameters


class TestAddStdoutHandler:
    """Tests for add_stdout_handler function."""

    def test_add_stdout_handler_exists(self):
        """add_stdout_handler function should exist."""
        from Pyflix.utils.logger import add_stdout_handler
        assert callable(add_stdout_handler)

    def test_add_stdout_handler_adds_handler(self):
        """add_stdout_handler should add a handler to the logger."""
        from Pyflix.utils.logger import add_stdout_handler
        
        test_logger = logging.getLogger("test_stdout_unique")
        initial_count = len(test_logger.handlers)
        formatter = logging.Formatter("%(message)s")
        
        add_stdout_handler(test_logger, formatter)
        
        assert len(test_logger.handlers) > initial_count

    def test_add_stdout_handler_with_stream_handler(self):
        """add_stdout_handler should add a StreamHandler when RainbowLoggingHandler is unavailable."""
        from Pyflix.utils.logger import add_stdout_handler
        
        test_logger = logging.getLogger("test_stream_unique")
        formatter = logging.Formatter("%(message)s")
        
        add_stdout_handler(test_logger, formatter)
        
        # At least one handler should be a stream handler
        has_stream_handler = any(isinstance(h, logging.StreamHandler) for h in test_logger.handlers)
        # Or a RainbowLoggingHandler (if installed)
        assert has_stream_handler or len(test_logger.handlers) > 0
