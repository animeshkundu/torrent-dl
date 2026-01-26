"""Unit tests for Pyflix.utils.streamer module - range header parsing.

These tests characterize the existing behavior of the HTTP streaming components.
They capture BEHAVIOR, not correctness.
"""

import pytest


class TestParseRangeHeader:
    """Tests for parse_range_header function."""

    def test_returns_tuple(self):
        """parse_range_header should return a tuple."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=0-100", 1000)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_none_header_returns_none_tuple(self):
        """None header should return (None, None)."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header(None, 1000)
        assert result == (None, None)

    def test_empty_header_returns_none_tuple(self):
        """Empty string header should return (None, None)."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("", 1000)
        assert result == (None, None)

    def test_simple_range(self):
        """Parse a simple byte range like 'bytes=0-100'."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=0-100", 1000)
        assert result == (0, 100)

    def test_range_from_zero(self):
        """Parse range starting from zero."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=0-499", 1000)
        assert result == (0, 499)

    def test_range_middle(self):
        """Parse range in the middle of file."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=500-999", 1000)
        assert result == (500, 999)

    def test_range_open_ended(self):
        """Parse open-ended range like 'bytes=500-'."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=500-", 1000)
        assert result == (500, 999)

    def test_range_suffix(self):
        """Parse suffix range like 'bytes=-100' (last 100 bytes)."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=-100", 1000)
        assert result == (900, 999)

    def test_invalid_range_not_bytes(self):
        """Non-bytes range should raise InvalidRangeHeader."""
        from Pyflix.utils.streamer import parse_range_header, InvalidRangeHeader
        with pytest.raises(InvalidRangeHeader):
            parse_range_header("words=0-100", 1000)

    def test_invalid_range_both_empty(self):
        """Range with both values empty should raise InvalidRangeHeader."""
        from Pyflix.utils.streamer import parse_range_header, InvalidRangeHeader
        with pytest.raises(InvalidRangeHeader):
            parse_range_header("bytes=-", 1000)

    def test_large_file_range(self):
        """Parse range for a large file (1GB)."""
        from Pyflix.utils.streamer import parse_range_header
        file_size = 1024 * 1024 * 1024  # 1GB
        result = parse_range_header("bytes=0-1023", file_size)
        assert result == (0, 1023)

    def test_range_near_end_of_file(self):
        """Parse range near the end of a file."""
        from Pyflix.utils.streamer import parse_range_header
        result = parse_range_header("bytes=900-", 1000)
        assert result == (900, 999)


class TestInvalidRangeHeader:
    """Tests for InvalidRangeHeader exception."""

    def test_is_exception(self):
        """InvalidRangeHeader should be an Exception."""
        from Pyflix.utils.streamer import InvalidRangeHeader
        assert issubclass(InvalidRangeHeader, Exception)

    def test_can_be_raised(self):
        """InvalidRangeHeader can be raised and caught."""
        from Pyflix.utils.streamer import InvalidRangeHeader
        with pytest.raises(InvalidRangeHeader):
            raise InvalidRangeHeader("test error")

    def test_message_preserved(self):
        """InvalidRangeHeader should preserve its message."""
        from Pyflix.utils.streamer import InvalidRangeHeader
        try:
            raise InvalidRangeHeader("custom message")
        except InvalidRangeHeader as e:
            assert "custom message" in str(e)
