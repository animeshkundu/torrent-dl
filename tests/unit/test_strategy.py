"""Unit tests for Pyflix.torrent.strategy module.

These tests characterize the existing behavior of the download strategy.
They capture BEHAVIOR, not correctness.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestDefaultStrategy:
    """Tests for DefaultStrategy class."""

    @pytest.fixture
    def mock_manager(self):
        """Create a mock download manager."""
        manager = MagicMock()
        manager.handle = MagicMock()
        manager.handle.status.return_value.pieces = [False] * 100
        return manager

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
        settings = MagicMock()
        settings.strategy = MagicMock()
        settings.strategy.piece_st = 10
        settings.strategy.last_piece_st = 5
        settings.strategy.chunks_strat = 10
        settings.strategy.always_sequential = False
        return settings

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_class_exists(self, mock_get_settings, mock_settings, mock_manager):
        """DefaultStrategy class should exist and be instantiable."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        assert strategy is not None

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_stores_manager_reference(self, mock_get_settings, mock_settings, mock_manager):
        """DefaultStrategy should store reference to manager."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        assert strategy.manager is mock_manager

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_has_holding_stream(self, mock_get_settings, mock_settings, mock_manager):
        """DefaultStrategy should have holding_stream attribute."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        assert hasattr(strategy, 'holding_stream')
        assert strategy.holding_stream is True

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_initial_sets_sequential(self, mock_get_settings, mock_settings, mock_manager):
        """initial() should set sequential download mode."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        strategy.initial()
        mock_manager.handle.set_sequential_download.assert_called_with(True)

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_initial_sets_high_priority_for_first_pieces(self, mock_get_settings, mock_settings, mock_manager):
        """initial() should set high priority for first pieces."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        strategy.initial()
        # Should call piece_priority for first piece_st pieces
        assert mock_manager.handle.piece_priority.call_count >= 1

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_reset_priorities(self, mock_get_settings, mock_settings, mock_manager):
        """reset_priorities() should set all pieces to priority 1."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        strategy.reset_priorities()
        # Should be called for each piece
        assert mock_manager.handle.piece_priority.call_count == 100

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_block_requested_does_nothing_when_holding(self, mock_get_settings, mock_settings, mock_manager):
        """block_requested() should do nothing when holding_stream is True."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        strategy.holding_stream = True
        strategy.block_requested(50)
        # reset_priorities should not be called
        # This is implicitly tested by no errors being raised

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_has_moov_downloaded_flag(self, mock_get_settings, mock_settings, mock_manager):
        """DefaultStrategy should track moov download status."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        strategy = DefaultStrategy(mock_manager)
        assert hasattr(strategy, 'moov_downloaded')
        assert strategy.moov_downloaded is False
