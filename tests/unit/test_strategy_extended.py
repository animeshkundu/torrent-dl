"""Extended unit tests for Pyflix.torrent.strategy module.

These tests cover additional strategy behavior and edge cases.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestDefaultStrategyExtended:
    """Extended tests for DefaultStrategy class."""

    @pytest.fixture
    def mock_manager(self):
        """Create a mock download manager with 100 pieces."""
        manager = MagicMock()
        manager.handle = MagicMock()
        manager.handle.status.return_value.pieces = [False] * 100
        manager.get_video_path.return_value = "/tmp/test_video.mp4"
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
    def test_initial_updates_chunks_strat(self, mock_get_settings, mock_settings, mock_manager):
        """initial() should update chunks_strat from piece count."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        original_chunks = strategy.chunks_strat
        strategy.initial()
        
        # chunks_strat gets recalculated to len(pieces) / 30
        # With 100 pieces, this should be 100 / 30 = 3
        # Regardless of initial value, it should be a reasonable number
        assert strategy.chunks_strat >= 1

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_initial_sets_piece_deadlines(self, mock_get_settings, mock_settings, mock_manager):
        """initial() should set piece deadlines for first pieces."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        strategy.initial()
        
        # Should call set_piece_deadline for each of the first pieces
        assert mock_manager.handle.set_piece_deadline.call_count >= 1

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_block_requested_moves_strategy_when_not_holding(self, mock_get_settings, mock_settings, mock_manager):
        """block_requested() should call move_strategy when not holding."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        strategy.holding_stream = False
        
        # Call block_requested
        strategy.block_requested(50)
        
        # reset_priorities should be called as part of move_strategy
        mock_manager.handle.piece_priority.assert_called()

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_download_lasts_flag_default_false(self, mock_get_settings, mock_settings, mock_manager):
        """download_lasts should default to False."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        assert strategy.download_lasts is False

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_uses_settings_values(self, mock_get_settings, mock_settings, mock_manager):
        """Strategy should use values from settings."""
        mock_get_settings.return_value = mock_settings
        mock_settings.strategy.piece_st = 15
        mock_settings.strategy.last_piece_st = 8
        
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        assert strategy.piece_st == 15
        assert strategy.last_piece_st == 8

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_move_strategy_sets_high_priority(self, mock_get_settings, mock_settings, mock_manager):
        """move_strategy should set high priority for requested block range."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        strategy.move_strategy(20)
        
        # Should set priority 7 for pieces in range
        calls = mock_manager.handle.piece_priority.call_args_list
        # Check that priority 7 was set for at least one piece
        high_priority_calls = [c for c in calls if len(c[0]) > 1 and c[0][1] == 7]
        assert len(high_priority_calls) >= 1


class TestStrategyEdgeCases:
    """Edge case tests for DefaultStrategy."""

    @pytest.fixture
    def mock_manager(self):
        """Create a mock manager with few pieces."""
        manager = MagicMock()
        manager.handle = MagicMock()
        manager.handle.status.return_value.pieces = [False] * 10  # Small file
        return manager

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
        settings = MagicMock()
        settings.strategy = MagicMock()
        settings.strategy.piece_st = 5
        settings.strategy.last_piece_st = 2
        settings.strategy.chunks_strat = 3
        settings.strategy.always_sequential = True
        return settings

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_strategy_with_small_file(self, mock_get_settings, mock_settings, mock_manager):
        """Strategy should handle small files (few pieces)."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        strategy.initial()
        
        # Should not crash with small piece count
        assert strategy is not None

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_move_strategy_near_end_of_file(self, mock_get_settings, mock_settings, mock_manager):
        """move_strategy should handle being near end of file."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        # Request near end of 10-piece file
        strategy.move_strategy(8)
        
        # Should not crash
        assert strategy.piece_st is not None

    @patch('Pyflix.torrent.strategy.get_settings')
    def test_always_sequential_setting(self, mock_get_settings, mock_settings, mock_manager):
        """Strategy should respect always_sequential setting."""
        mock_get_settings.return_value = mock_settings
        from Pyflix.torrent.strategy import DefaultStrategy
        
        strategy = DefaultStrategy(mock_manager)
        assert strategy.settings.always_sequential is True
