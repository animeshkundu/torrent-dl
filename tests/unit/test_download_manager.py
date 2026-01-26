"""Unit tests for Pyflix.torrent DownloadManager.

These tests characterize the existing behavior of the DownloadManager class.
They capture BEHAVIOR, not correctness.
"""

import pytest
from unittest.mock import patch, MagicMock, PropertyMock


class TestDownloadManager:
    """Tests for DownloadManager class."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings object."""
        settings = MagicMock()
        settings.save_path = "/tmp/downloads"
        settings.limits.upload = None
        settings.limits.download = None
        settings.players.default = "vlc"
        settings.strategy = MagicMock()
        settings.strategy.piece_st = 10
        settings.strategy.last_piece_st = 5
        settings.strategy.chunks_strat = 10
        settings.strategy.always_sequential = False
        return settings

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_download_manager_exists(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager class should exist and be instantiable."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert manager is not None

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_stores_magnet_link(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should store the magnet link."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        magnet = "magnet:?xt=urn:btih:abcdef1234567890"
        manager = DownloadManager(magnet, port=1234, serve=True)
        assert manager.magnet == magnet

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_stores_port(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should store the port number."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=8888,
            serve=True
        )
        assert manager.port == 8888

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_uses_default_port_when_none(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should use DEFAULT_PORT when port is None."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        from Pyflix.utils.settings import DEFAULT_PORT
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=None,
            serve=True
        )
        assert manager.port == DEFAULT_PORT

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=False)
    @patch('Pyflix.torrent.get_free_port', return_value=9999)
    def test_gets_free_port_when_occupied(self, mock_free_port, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should get free port when requested port is occupied."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert manager.port == 9999

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_stores_serve_flag(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should store the serve flag."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert manager.serve is True

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_stores_player(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should store the player."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True,
            player="vlc"
        )
        assert manager.player == "vlc"

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_uses_default_player_when_none(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should use default player when player is None."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True,
            player=None
        )
        assert manager.player == "vlc"

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_initializes_video_file_as_none(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should initialize _video_file as None."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert manager._video_file is None

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_initializes_streaming_as_false(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should initialize streaming as False."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert manager.streaming is False

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_has_strategy(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should have a strategy attribute."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        from Pyflix.torrent.strategy import DefaultStrategy
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert hasattr(manager, 'strategy')
        assert isinstance(manager.strategy, DefaultStrategy)

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_has_session(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should have a libtorrent session."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert hasattr(manager, 'session')

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_has_handle(self, mock_port_free, mock_strat_settings, mock_get_settings, mock_helper_settings, mock_settings):
        """DownloadManager should have a torrent handle."""
        mock_get_settings.return_value = mock_settings
        mock_strat_settings.return_value = mock_settings
        mock_helper_settings.return_value = mock_settings
        from Pyflix.torrent import DownloadManager
        
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True
        )
        assert hasattr(manager, 'handle')


class TestDownloadManagerMethods:
    """Tests for DownloadManager methods."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings object."""
        settings = MagicMock()
        settings.save_path = "/tmp/downloads"
        settings.limits.upload = None
        settings.limits.download = None
        settings.players.default = "vlc"
        settings.strategy = MagicMock()
        settings.strategy.piece_st = 10
        settings.strategy.last_piece_st = 5
        settings.strategy.chunks_strat = 10
        settings.strategy.always_sequential = False
        return settings

    @pytest.fixture
    def manager(self, mock_settings):
        """Create a DownloadManager instance for testing."""
        with patch('Pyflix.utils.helpers.get_settings', return_value=mock_settings):
            with patch('Pyflix.torrent.get_settings', return_value=mock_settings):
                with patch('Pyflix.torrent.strategy.get_settings', return_value=mock_settings):
                    with patch('Pyflix.torrent.is_port_free', return_value=True):
                        from Pyflix.torrent import DownloadManager
                        return DownloadManager(
                            "magnet:?xt=urn:btih:test",
                            port=1234,
                            serve=True
                        )

    def test_status_property(self, manager):
        """status property should return handle status."""
        status = manager.status
        assert status is not None

    def test_rates_returns_tuple(self, manager):
        """rates() should return a tuple of download and upload rates."""
        rates = manager.rates()
        assert isinstance(rates, tuple)
        assert len(rates) == 2

    def test_rates_values_are_numeric(self, manager):
        """rates() should return numeric values."""
        rates = manager.rates()
        assert isinstance(rates[0], (int, float))
        assert isinstance(rates[1], (int, float))

    def test_get_video_path(self, manager):
        """get_video_path should return path combining save_path and video_file."""
        # Set up the video file
        manager._video_file = ["test.mp4", 1000]
        path = manager.get_video_path()
        assert "test.mp4" in path

    def test_block_served(self, manager):
        """block_served should mark a block as served."""
        manager._served_blocks = [False] * 10
        manager.block_served(5)
        assert manager._served_blocks[5] is True

    def test_guess_returns_dict(self, manager):
        """guess should return a dictionary."""
        result = manager.guess("/path/to/video.mp4")
        assert isinstance(result, dict)

    def test_guess_is_cached(self, manager):
        """guess should cache its result."""
        result1 = manager.guess("/path/to/video.mp4")
        result2 = manager.guess("/path/to/video.mp4")
        assert result1 is result2
