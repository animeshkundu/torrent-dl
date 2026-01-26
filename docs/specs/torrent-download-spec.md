# Spec: Torrent Download Module

## Overview

The torrent download module (`Pyflix/torrent/`) provides the core torrent downloading functionality using libtorrent-rasterbar. It manages magnet link processing, piece downloading, and streaming preparation.

## Architecture

```
Pyflix/torrent/
├── __init__.py      # DownloadManager class
├── strategy.py      # DefaultStrategy for piece prioritization
└── moov.py          # MP4 moov atom detection
```

## Core Components

### DownloadManager (`__init__.py`)

The main orchestrator class that manages the download lifecycle.

**Responsibilities:**
- Parse and validate magnet links
- Initialize libtorrent session and handle
- Manage download state and progress
- Coordinate with strategy for piece prioritization
- Start HTTP streaming server when ready
- Launch media player

**Constructor Parameters:**
- `magnet` (str): Magnet URI to download
- `port` (int, optional): HTTP server port (default: 1149)
- `serve` (bool, optional): If True, only serve without launching player
- `player` (str, optional): Player to use (default: "vlc")
- `save_path` (str, optional): Directory for downloaded files

**Key Methods:**
- `start()`: Begin download, blocking main loop
- `stream()`: Start HTTP streaming server
- `get_biggest_file()`: Find the largest file in the torrent
- `get_video_path()`: Get full path to video file
- `rates()`: Get download/upload rates in KB/s
- `elapsed_time()`: Get formatted elapsed time

**State Properties:**
- `status`: Current torrent status from libtorrent
- `video_file`: Path and size of the largest file
- `streaming`: Whether HTTP server is running

### DefaultStrategy (`strategy.py`)

Implements piece prioritization for streaming optimization.

**Strategy:**
1. Download first N pieces (configurable) at high priority
2. Download last N pieces for MP4 moov atom
3. Once moov atom is available, switch to sequential or adaptive mode
4. When playback requests a specific block, prioritize nearby pieces

**Key Methods:**
- `initial()`: Set up initial piece priorities
- `master()`: Main loop strategy update
- `block_requested(block)`: Handle playback block requests
- `move_strategy(first_block)`: Shift priority window
- `reset_priorities()`: Reset all pieces to normal priority

### moov Atom Handler (`moov.py`)

Detects whether an MP4 file has its moov atom available for streaming.

**Function: `have_moov(video_file)`**
- Returns `True` if moov atom is downloaded and positioned for streaming
- Returns `(True, "after_mdat")` if moov is after mdat (needs fast-start)
- Returns `False` if moov is not yet available

## Dependencies

### External
- `libtorrent`: Python bindings for libtorrent-rasterbar
- `blessings`: Terminal formatting
- `colorama`: Cross-platform colored terminal text
- `guessit`: Media file name parsing
- `qtfaststart`: MP4 atom detection

### Internal
- `Pyflix.utils.helpers`: Port utilities, settings
- `Pyflix.utils.constants`: State names
- `Pyflix.utils.settings`: Configuration constants
- `Pyflix.utils.streamer`: HTTP streaming server
- `Pyflix.utils.output`: VLC player integration

## Configuration

Settings are loaded from `~/.pyflix/settings.yaml`:

```yaml
save_path: /tmp/pyflix
limits:
  upload: null
  download: null
strategy:
  piece_st: 10
  last_piece_st: 5
  chunks_strat: 10
  always_sequential: false
players:
  default: vlc
```

## Error Handling

- Network errors: Handled by libtorrent internally
- File system errors: Logged, may cause graceful shutdown
- Player launch errors: Logged, download continues
- KeyboardInterrupt: Graceful shutdown with HTTP server cleanup

## Testing Strategy

### Unit Tests (Implemented)
- Test `DownloadManager` initialization with mocked libtorrent
- Test `DefaultStrategy` piece prioritization logic
- Test `have_moov` atom detection with various file states

### Integration Tests (Future)
- Test full download cycle with test torrent
- Test HTTP streaming with simulated video file
- Test player integration

## Security Considerations

- Downloads from untrusted sources should be sandboxed
- File paths should be sanitized to prevent directory traversal
- HTTP server binds to 0.0.0.0 (all interfaces) - consider localhost-only option

## Performance Considerations

- Piece prioritization reduces time to playback
- Large torrents may consume significant memory for piece tracking
- HTTP server uses threading for concurrent connections
