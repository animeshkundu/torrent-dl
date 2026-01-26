"""Unit tests for Pyflix.torrent.moov module.

These tests characterize the existing behavior of the MP4 moov atom handling.
They capture BEHAVIOR, not correctness.
"""

import pytest
from unittest.mock import patch, MagicMock, mock_open


class TestHaveMoov:
    """Tests for have_moov function."""

    @patch('Pyflix.torrent.moov.SKIP_MOOV', True)
    def test_returns_true_when_skip_moov_enabled(self):
        """have_moov should return True when SKIP_MOOV is True."""
        from Pyflix.torrent.moov import have_moov
        result = have_moov("/fake/path/video.mp4")
        assert result is True

    @patch('Pyflix.torrent.moov.SKIP_MOOV', False)
    @patch('Pyflix.torrent.moov.get_index')
    @patch('builtins.open', new_callable=mock_open)
    def test_opens_video_file(self, mock_file, mock_get_index, tmp_path):
        """have_moov should open the video file in binary mode."""
        from Pyflix.torrent.moov import have_moov
        # Create mock atoms with required attributes
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 100
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [mock_atom_moov, mock_atom_mdat, mock_atom_ftyp, mock_atom_free]
        
        video_path = "/tmp/test_video.mp4"
        have_moov(video_path)
        mock_file.assert_called_once_with(video_path, 'rb')

    @patch('Pyflix.torrent.moov.SKIP_MOOV', False)
    @patch('Pyflix.torrent.moov.get_index')
    @patch('builtins.open', new_callable=mock_open)
    def test_moov_before_mdat_returns_true(self, mock_file, mock_get_index):
        """have_moov should return True when moov is before mdat."""
        from Pyflix.torrent.moov import have_moov
        
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 100
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [mock_atom_moov, mock_atom_mdat, mock_atom_ftyp, mock_atom_free]
        
        result = have_moov("/tmp/test.mp4")
        assert result is True

    @patch('Pyflix.torrent.moov.SKIP_MOOV', False)
    @patch('Pyflix.torrent.moov.get_index')
    @patch('builtins.open', new_callable=mock_open)
    def test_moov_after_mdat_returns_tuple(self, mock_file, mock_get_index):
        """have_moov should return (True, 'after_mdat') when moov is after mdat."""
        from Pyflix.torrent.moov import have_moov
        
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 300  # After mdat
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 100
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [mock_atom_moov, mock_atom_mdat, mock_atom_ftyp, mock_atom_free]
        
        result = have_moov("/tmp/test.mp4")
        assert result == (True, "after_mdat")

    @patch('Pyflix.torrent.moov.SKIP_MOOV', False)
    @patch('Pyflix.torrent.moov.get_index')
    @patch('builtins.open', new_callable=mock_open)
    def test_faststart_exception_returns_false(self, mock_file, mock_get_index):
        """have_moov should return False on FastStartException."""
        from Pyflix.torrent.moov import have_moov
        from qtfaststart.exceptions import FastStartException
        
        mock_get_index.side_effect = FastStartException("test error")
        
        result = have_moov("/tmp/test.mp4")
        assert result is False
