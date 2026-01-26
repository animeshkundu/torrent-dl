"""Unit tests for Pyflix.utils.constants module.

These tests characterize the existing behavior of the constants module.
They capture BEHAVIOR, not correctness.
"""

import pytest


class TestStates:
    """Tests for STATES constant."""

    def test_states_is_list(self):
        """STATES should be a list."""
        from Pyflix.utils.constants import STATES
        assert isinstance(STATES, list)

    def test_states_length(self):
        """STATES should have 7 items."""
        from Pyflix.utils.constants import STATES
        assert len(STATES) == 7

    def test_states_values(self):
        """STATES should contain specific values in order."""
        from Pyflix.utils.constants import STATES
        expected = [
            'Queued', 'Checking', 'Downloading torrent metadata', 'Downloading',
            'Finished', 'Seeding', 'Allocating'
        ]
        assert STATES == expected

    def test_states_are_strings(self):
        """All STATES values should be strings."""
        from Pyflix.utils.constants import STATES
        for state in STATES:
            assert isinstance(state, str)

    def test_queued_state_index(self):
        """Queued should be at index 0."""
        from Pyflix.utils.constants import STATES
        assert STATES[0] == 'Queued'

    def test_downloading_state_index(self):
        """Downloading should be at index 3."""
        from Pyflix.utils.constants import STATES
        assert STATES[3] == 'Downloading'

    def test_seeding_state_index(self):
        """Seeding should be at index 5."""
        from Pyflix.utils.constants import STATES
        assert STATES[5] == 'Seeding'
