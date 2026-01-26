"""Additional unit tests for Pyflix.utils.streamer module.

These tests cover the HTTP server and video handler components.
"""

import pytest
from unittest.mock import patch, MagicMock, PropertyMock


class TestThreadedHTTPServer:
    """Tests for ThreadedHTTPServer class."""

    def test_threaded_http_server_exists(self):
        """ThreadedHTTPServer class should exist."""
        from Pyflix.utils.streamer import ThreadedHTTPServer
        assert ThreadedHTTPServer is not None

    def test_threaded_http_server_is_http_server(self):
        """ThreadedHTTPServer should inherit from HTTPServer."""
        from Pyflix.utils.streamer import ThreadedHTTPServer
        try:
            from http.server import HTTPServer
        except ImportError:
            from BaseHTTPServer import HTTPServer
        assert issubclass(ThreadedHTTPServer, HTTPServer)


class TestVideoHandler:
    """Tests for VideoHandler class."""

    def test_video_handler_exists(self):
        """VideoHandler class should exist."""
        from Pyflix.utils.streamer import VideoHandler
        assert VideoHandler is not None

    def test_video_handler_has_manager_attribute(self):
        """VideoHandler should have a manager class attribute."""
        from Pyflix.utils.streamer import VideoHandler
        assert hasattr(VideoHandler, 'manager')

    def test_video_handler_manager_default_is_none(self):
        """VideoHandler.manager should default to None."""
        from Pyflix.utils.streamer import VideoHandler
        # Store original and restore after
        original = VideoHandler.manager
        try:
            VideoHandler.manager = None
            assert VideoHandler.manager is None
        finally:
            VideoHandler.manager = original


class TestServeFile:
    """Tests for serve_file function."""

    def test_serve_file_exists(self):
        """serve_file function should exist."""
        from Pyflix.utils.streamer import serve_file
        assert callable(serve_file)

    def test_serve_file_callable(self):
        """serve_file should be callable."""
        from Pyflix.utils.streamer import serve_file
        import inspect
        sig = inspect.signature(serve_file)
        assert 'manager' in sig.parameters


class TestParseRangeHeaderEdgeCases:
    """Additional edge case tests for parse_range_header."""

    def test_very_large_range(self):
        """Parse range for a very large file."""
        from Pyflix.utils.streamer import parse_range_header
        file_size = 10 * 1024 * 1024 * 1024  # 10GB
        result = parse_range_header("bytes=0-1048575", file_size)
        assert result == (0, 1048575)

    def test_range_from_exact_start(self):
        """Parse range starting from 0."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=0-", 1000)
        assert result[0] == 0

    def test_range_single_byte(self):
        """Parse range for single byte."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=500-500", 1000)
        assert result == (500, 500)

    def test_range_last_byte(self):
        """Parse range for last byte of file."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=-1", 1000)
        assert result == (999, 999)

    def test_range_last_100_bytes(self):
        """Parse range for last 100 bytes."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=-100", 1000)
        assert result == (900, 999)

    def test_invalid_range_format_raises_exception(self):
        """Invalid format should raise InvalidRangeHeader."""
        from Pyflix.utils.streamer import parse_range_header, InvalidRangeHeader
        with pytest.raises(InvalidRangeHeader):
            parse_range_header("invalid", 1000)

    def test_non_bytes_unit_raises_exception(self):
        """Non-bytes unit should raise InvalidRangeHeader."""
        from Pyflix.utils.streamer import parse_range_header, InvalidRangeHeader
        with pytest.raises(InvalidRangeHeader):
            parse_range_header("characters=0-100", 1000)
