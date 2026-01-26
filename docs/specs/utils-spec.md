# Spec: Utility Modules

## Overview

The utility modules (`Pyflix/utils/`) provide supporting functionality for the torrent download and streaming system.

## Architecture

```
Pyflix/utils/
├── __init__.py       # Empty package marker
├── constants.py      # State constants
├── decorators.py     # Function decorators
├── helpers.py        # General utilities
├── logger.py         # Logging setup
├── output.py         # Media player output
├── settings.py       # Configuration constants
├── settings.yaml     # Default settings file
└── streamer.py       # HTTP streaming (see http-streaming-spec.md)
```

## Modules

### constants.py

Defines torrent state names mapped to libtorrent state indices.

```python
STATES = [
    'Queued',           # 0
    'Checking',         # 1
    'Downloading torrent metadata',  # 2
    'Downloading',      # 3
    'Finished',         # 4
    'Seeding',          # 5
    'Allocating'        # 6
]
```

### settings.py

Global configuration constants.

```python
DEBUG = False       # Enable debug logging
DEFAULT_PORT = 1149 # Default HTTP server port
WAIT_FOR_IT = 0.3   # Polling interval (seconds)
SKIP_MOOV = True    # Skip moov atom checking
```

### decorators.py

Function decorators for common patterns.

#### `@with_config_dir`
Ensures the config directory exists before function execution.

```python
@with_config_dir
def my_function():
    # ~/.pyflix/ exists when this runs
    pass
```

### helpers.py

General utility functions.

#### Network Utilities

- **`get_free_port()`**: Find an available ephemeral port
- **`is_port_free(port)`**: Check if a specific port is available
- **`get_interface()`**: Get the primary network interface IP

#### Configuration

- **`get_settings()`**: Load settings from YAML file
- **`set_config_dir()`**: Create `~/.pyflix/` directory

#### Process Management

- **`is_process_running(pid)`**: Check if a process is running
- **`daemonize(args, callback)`**: Run callback as a daemon
- **`get_lock_diff()`**: Get time since lock file modified

### logger.py

Logging configuration.

#### `log_set_up(verbose=False)`
Configure logging handlers.

**Behavior:**
1. Create `~/.pyflix/save_path/pyflix.log` with rotation
2. Add console handler (with color if available)
3. Set level to DEBUG if verbose, else INFO

**Log Format:**
```
2024-01-20 15:30:45  pyflix.torrent        INFO     Starting download
```

### output.py

Media player integration.

#### `Output` (base class)
Abstract base for player outputs.

#### `VLCOutput`
Launches VLC player with stream URL.

```python
class VLCOutput(Output):
    def _player(self):
        return f"vlc {self.stream_url} -q"
```

### settings.yaml

Default settings file (copied to `~/.pyflix/settings.yaml`).

```yaml
save_path: /tmp/pyflix/downloads

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

## Dependencies

### External
- `altasetting`: YAML settings management
- `netifaces`: Network interface enumeration
- `daemon`: Unix daemon support
- `lockfile`: Process locking
- `ojota`: Data source management
- `blessings`: Terminal formatting
- `rainbow_logging_handler`: Colored logging (optional)

### Python Standard Library
- `socket`: Port checking
- `logging`: Logging infrastructure
- `os`: File/process operations
- `shutil`: File copying

## Testing Strategy

### Unit Tests (Implemented)
- Constants values and types
- Port utilities (free port, port checking)
- Process detection
- Settings loading
- Logger setup
- VLC output command generation

### Integration Tests (Future)
- Settings file creation/loading cycle
- Daemon process management

## Security Considerations

1. **Settings File**: Created with default permissions - may contain sensitive paths
2. **Lock Files**: Created in `/tmp` - writable by all users
3. **Daemon**: Runs with calling user's permissions

## Performance Considerations

1. **Port Checking**: Creates/destroys sockets - not for high-frequency use
2. **Settings Loading**: YAML parsing on every call - consider caching
3. **Logging**: Rotating file handler limits disk usage
