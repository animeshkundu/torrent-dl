"""Unit tests for Pyflix.utils.settings module.

These tests characterize the existing behavior of the settings module.
They capture BEHAVIOR, not correctness.
"""

import pytest


class TestSettings:
    """Tests for settings constants."""

    def test_debug_is_boolean(self):
        """DEBUG should be a boolean."""
        from Pyflix.utils.settings import DEBUG
        assert isinstance(DEBUG, bool)

    def test_debug_default_is_false(self):
        """DEBUG default value should be False."""
        from Pyflix.utils.settings import DEBUG
        assert DEBUG is False

    def test_default_port_is_integer(self):
        """DEFAULT_PORT should be an integer."""
        from Pyflix.utils.settings import DEFAULT_PORT
        assert isinstance(DEFAULT_PORT, int)

    def test_default_port_value(self):
        """DEFAULT_PORT should be 1149."""
        from Pyflix.utils.settings import DEFAULT_PORT
        assert DEFAULT_PORT == 1149

    def test_wait_for_it_is_numeric(self):
        """WAIT_FOR_IT should be a numeric type."""
        from Pyflix.utils.settings import WAIT_FOR_IT
        assert isinstance(WAIT_FOR_IT, (int, float))

    def test_wait_for_it_value(self):
        """WAIT_FOR_IT should be 0.3 seconds."""
        from Pyflix.utils.settings import WAIT_FOR_IT
        assert WAIT_FOR_IT == 0.3

    def test_skip_moov_is_boolean(self):
        """SKIP_MOOV should be a boolean."""
        from Pyflix.utils.settings import SKIP_MOOV
        assert isinstance(SKIP_MOOV, bool)

    def test_skip_moov_default_is_true(self):
        """SKIP_MOOV default value should be True."""
        from Pyflix.utils.settings import SKIP_MOOV
        assert SKIP_MOOV is True
