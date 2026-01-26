"""Unit tests for Pyflix.utils.output module.

These tests characterize the existing behavior of the output module.
They capture BEHAVIOR, not correctness.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestOutput:
    """Tests for Output base class."""

    def test_output_class_exists(self):
        """Output class should exist."""
        from Pyflix.utils.output import Output
        assert Output is not None

    def test_output_stores_stream_url(self):
        """Output should store the stream URL."""
        from Pyflix.utils.output import Output
        parent = MagicMock()
        output = Output("http://localhost:8080", parent)
        assert output.stream_url == "http://localhost:8080"

    def test_output_stores_parent(self):
        """Output should store the parent reference."""
        from Pyflix.utils.output import Output
        parent = MagicMock()
        output = Output("http://localhost:8080", parent)
        assert output.parent is parent

    def test_player_returns_empty_string(self):
        """Base Output._player() should return empty string."""
        from Pyflix.utils.output import Output
        parent = MagicMock()
        output = Output("http://localhost:8080", parent)
        assert output._player() == ""


class TestVLCOutput:
    """Tests for VLCOutput class."""

    def test_vlc_output_class_exists(self):
        """VLCOutput class should exist."""
        from Pyflix.utils.output import VLCOutput
        assert VLCOutput is not None

    def test_vlc_output_inherits_from_output(self):
        """VLCOutput should inherit from Output."""
        from Pyflix.utils.output import Output, VLCOutput
        assert issubclass(VLCOutput, Output)

    def test_vlc_player_command_format(self):
        """VLCOutput._player() should return VLC command."""
        from Pyflix.utils.output import VLCOutput
        parent = MagicMock()
        output = VLCOutput("http://localhost:8080", parent)
        command = output._player()
        assert "vlc" in command.lower()
        assert "http://localhost:8080" in command

    def test_vlc_player_includes_quiet_flag(self):
        """VLCOutput._player() should include -q flag."""
        from Pyflix.utils.output import VLCOutput
        parent = MagicMock()
        output = VLCOutput("http://localhost:8080", parent)
        command = output._player()
        assert "-q" in command
