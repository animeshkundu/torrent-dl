# torrent-dl System Architecture

## Overview

torrent-dl is a Python application for watching and downloading torrents simultaneously. It combines torrent downloading capabilities with media streaming functionality.

## High-Level Architecture

```mermaid
graph TB
    subgraph "User Interface"
        CLI[CLI Entry Point<br/>torrent-dl]
    end

    subgraph "Core Application"
        Main[Main Module<br/>Pyflix.__init__]
        Args[Argument Parser]
        Logger[Logger Utility]
    end

    subgraph "Torrent Engine"
        DM[Download Manager<br/>Pyflix.torrent]
        Strategy[Download Strategy]
        Moov[MOOV Atom Handler]
    end

    subgraph "Utilities"
        Helpers[Helpers]
        Settings[Settings]
        Constants[Constants]
        Decorators[Decorators]
    end

    subgraph "Streaming"
        Streamer[Media Streamer]
        Output[Output Handler]
    end

    subgraph "External Dependencies"
        LibTorrent[libtorrent-rasterbar]
        VLC[VLC Player]
    end

    CLI --> Main
    Main --> Args
    Main --> Logger
    Main --> DM

    DM --> Strategy
    DM --> Moov
    DM --> LibTorrent

    DM --> Streamer
    Streamer --> VLC
    Streamer --> Output

    DM --> Helpers
    DM --> Settings
    Main --> Constants
    DM --> Decorators
```

## Component Descriptions

### User Interface Layer

| Component | File | Purpose |
|-----------|------|---------|
| CLI Entry Point | `torrent-dl` | Command-line executable |

### Core Application Layer

| Component | File | Purpose |
|-----------|------|---------|
| Main Module | `Pyflix/__init__.py` | Application entry, argument parsing |
| Logger | `Pyflix/utils/logger.py` | Logging configuration |

### Torrent Engine Layer

| Component | File | Purpose |
|-----------|------|---------|
| Download Manager | `Pyflix/torrent/__init__.py` | Orchestrates torrent downloads |
| Strategy | `Pyflix/torrent/strategy.py` | Download prioritization logic |
| MOOV Handler | `Pyflix/torrent/moov.py` | MP4 atom manipulation for streaming |

### Utilities Layer

| Component | File | Purpose |
|-----------|------|---------|
| Helpers | `Pyflix/utils/helpers.py` | General utility functions |
| Settings | `Pyflix/utils/settings.py` | Configuration management |
| Constants | `Pyflix/utils/constants.py` | Application constants |
| Decorators | `Pyflix/utils/decorators.py` | Function decorators |

### Streaming Layer

| Component | File | Purpose |
|-----------|------|---------|
| Streamer | `Pyflix/utils/streamer.py` | HTTP streaming server |
| Output | `Pyflix/utils/output.py` | Console output formatting |

## Data Flow

```mermaid
sequenceDiagram
    participant User
    participant CLI
    participant Main
    participant DM as Download Manager
    participant LT as libtorrent
    participant Streamer
    participant VLC

    User->>CLI: torrent-dl <magnet>
    CLI->>Main: main()
    Main->>Main: Parse arguments
    Main->>DM: Create DownloadManager
    DM->>LT: Initialize session
    DM->>LT: Add magnet URI
    
    loop Download Progress
        LT-->>DM: Piece downloaded
        DM->>DM: Update strategy
    end

    DM->>Streamer: Start HTTP server
    Streamer->>VLC: Open stream URL
    
    loop Streaming
        VLC->>Streamer: Request data
        Streamer->>DM: Get piece data
        DM-->>Streamer: Return data
        Streamer-->>VLC: Stream data
    end
```

## External Dependencies

### libtorrent-rasterbar

- **Purpose**: BitTorrent protocol implementation
- **Integration**: Python bindings via `python-libtorrent`
- **Key Features**: Piece prioritization, sequential download

### VLC Player

- **Purpose**: Media playback
- **Integration**: Launched as subprocess
- **Features**: Streaming playback from HTTP server

## Configuration

Configuration is managed through:
- Command-line arguments (primary)
- `settings.yaml` (defaults)
- Environment variables (optional)

## Future Considerations

- Plugin architecture for additional players
- Web-based UI alternative
- Multiple simultaneous downloads
- Download queue management
