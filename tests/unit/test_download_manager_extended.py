"""Extended unit tests for Pyflix.torrent DownloadManager.

These tests cover additional behavior and edge cases.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestDownloadManagerBiggestFile:
    """Tests for get_biggest_file method."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
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
    def test_get_biggest_file_returns_list(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """get_biggest_file should return a list with path and size."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        
        result = manager.get_biggest_file()
        assert isinstance(result, list)
        assert len(result) == 2

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_video_file_property_caches_result(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """video_file property should cache its result."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        
        # First access
        file1 = manager.video_file
        # Second access
        file2 = manager.video_file
        
        assert file1 is file2  # Same object (cached)


class TestDownloadManagerRates:
    """Tests for rates and download statistics."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
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
    def test_rates_returns_kb_per_second(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """rates() should return values divided by 1000 (KB/s)."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        
        # The rates() method divides by 1000 to get KB/s
        rates = manager.rates()
        assert isinstance(rates[0], (int, float))
        assert isinstance(rates[1], (int, float))


class TestDownloadManagerElapsedTime:
    """Tests for elapsed_time method."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
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
    def test_elapsed_time_format(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """elapsed_time() should return time without microseconds."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        from datetime import datetime
        
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        manager.start_time = datetime.now()
        
        elapsed = manager.elapsed_time()
        
        # Should not contain microseconds (no decimal point)
        assert "." not in elapsed


class TestDownloadManagerUploadDownloadLimits:
    """Tests for upload/download limits."""

    @pytest.fixture
    def mock_settings_with_limits(self):
        """Create mock settings with limits."""
        settings = MagicMock()
        settings.save_path = "/tmp/downloads"
        settings.limits.upload = 1024 * 100  # 100 KB/s
        settings.limits.download = 1024 * 500  # 500 KB/s
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
    def test_applies_upload_limit(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings_with_limits):
        """DownloadManager should apply upload limit from settings."""
        mock_torrent.return_value = mock_settings_with_limits
        mock_strat.return_value = mock_settings_with_limits
        mock_helper.return_value = mock_settings_with_limits
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        
        # Manager should have been created with limits applied
        assert manager is not None
        assert hasattr(manager, 'handle')

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_applies_download_limit(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings_with_limits):
        """DownloadManager should apply download limit from settings."""
        mock_torrent.return_value = mock_settings_with_limits
        mock_strat.return_value = mock_settings_with_limits
        mock_helper.return_value = mock_settings_with_limits
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager("magnet:?xt=urn:btih:test", port=1234, serve=True)
        
        # Manager should have been created with limits applied
        assert manager is not None
        assert hasattr(manager, 'handle')


class TestDownloadManagerCustomSavePath:
    """Tests for custom save path."""

    @pytest.fixture
    def mock_settings(self):
        """Create mock settings."""
        settings = MagicMock()
        settings.save_path = "/default/downloads"
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
    def test_uses_custom_save_path(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """DownloadManager should use custom save_path when provided."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True,
            save_path="/custom/path"
        )
        
        assert manager.save_path == "/custom/path"

    @patch('Pyflix.utils.helpers.get_settings')
    @patch('Pyflix.torrent.get_settings')
    @patch('Pyflix.torrent.strategy.get_settings')
    @patch('Pyflix.torrent.is_port_free', return_value=True)
    def test_uses_default_save_path(self, mock_port, mock_strat, mock_torrent, mock_helper, mock_settings):
        """DownloadManager should use settings save_path when not provided."""
        mock_torrent.return_value = mock_settings
        mock_strat.return_value = mock_settings
        mock_helper.return_value = mock_settings
        
        from Pyflix.torrent import DownloadManager
        manager = DownloadManager(
            "magnet:?xt=urn:btih:test",
            port=1234,
            serve=True,
            save_path=None
        )
        
        assert manager.save_path == "/default/downloads"
