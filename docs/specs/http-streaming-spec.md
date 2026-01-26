# Spec: HTTP Streaming Module

## Overview

The HTTP streaming module (`Pyflix/utils/streamer.py`) provides a threaded HTTP server that serves video content to media players while the torrent is still downloading.

## Architecture

```
Pyflix/utils/streamer.py
├── ThreadedHTTPServer      # Threaded HTTP server
├── VideoHandler            # Request handler for video serving
├── InvalidRangeHeader      # Exception for invalid HTTP Range headers
├── serve_file()            # Server startup function
└── parse_range_header()    # HTTP Range header parser
```

## Core Components

### ThreadedHTTPServer

A mixin of `ThreadingMixIn` and `HTTPServer` that handles concurrent connections.

**Purpose:**
- Allow multiple clients to stream simultaneously
- Non-blocking response handling

### VideoHandler

Custom HTTP request handler for serving video content.

**Endpoints:**
- `GET /` - Serve video content with range support
- `GET /status` - JSON status endpoint

**Status Response:**
```json
{
  "file": ["video.mp4", 1073741824],
  "elapsed": "00:05:32",
  "rates": [512.5, 128.3],
  "state": "Downloading",
  "peers": 15,
  "streaming": true
}
```

**Range Support:**
- Full HTTP Range header support (RFC 7233)
- Serves partial content (206) when Range header present
- Falls back to full content (200) without Range header

### Key Functions

#### `serve_file(manager)`
Starts the HTTP server on the manager's configured port.

**Parameters:**
- `manager`: DownloadManager instance

**Behavior:**
1. Creates `ThreadedHTTPServer` on `0.0.0.0:port`
2. Assigns manager reference to `VideoHandler`
3. Starts `serve_forever()` loop

#### `parse_range_header(range_header, total_length)`
Parses HTTP Range headers into byte positions.

**Parameters:**
- `range_header` (str): The Range header value
- `total_length` (int): Total file size in bytes

**Returns:**
- `(start, end)`: Byte range tuple
- `(None, None)`: If no range specified

**Examples:**
```python
parse_range_header("bytes=0-100", 1000)    # → (0, 100)
parse_range_header("bytes=500-", 1000)     # → (500, 999)
parse_range_header("bytes=-100", 1000)     # → (900, 999)
parse_range_header(None, 1000)             # → (None, None)
```

## HTTP Response Flow

### Standard Video Request
```
1. Client requests GET /
2. Handler checks for Range header
3. If Range present:
   a. Parse range bounds
   b. Send 206 Partial Content
   c. Set Content-Range header
4. Else:
   a. Send 200 OK
   b. Set Accept-Ranges: bytes
5. Set Content-Type from guessit
6. Stream content, waiting for pieces as needed
```

### Piece Waiting
```
1. Calculate blocks needed for range
2. For each block:
   a. Check if available (downloaded)
   b. If not, notify strategy
   c. Wait until available
   d. Mark block as served
3. Read and send data
```

## Dependencies

### External
- `http.server`: Python HTTP server classes
- `socketserver`: Threading mixin

### Internal
- `Pyflix.utils.constants`: State names
- `Pyflix.utils.settings`: Wait timing

## Configuration

| Constant | Value | Description |
|----------|-------|-------------|
| `WAIT_FOR_IT` | 0.3s | Polling interval for piece availability |

## Error Handling

### InvalidRangeHeader
Raised when Range header cannot be parsed.

**Cases:**
- Non-bytes unit (e.g., "characters=0-100")
- Empty range ("bytes=-")
- Malformed syntax

## Testing Strategy

### Unit Tests (Implemented)
- `parse_range_header()` - All range formats
- `InvalidRangeHeader` exception handling
- Class existence and inheritance

### Integration Tests (Future)
- Full HTTP request/response cycle
- Range header handling with real files
- Concurrent request handling

## Security Considerations

1. **Path Traversal**: Video path comes from torrent metadata - sanitize before serving
2. **Binding**: Server binds to `0.0.0.0` - accessible on all interfaces
3. **Resource Exhaustion**: Thread per connection - consider limits

## Performance Considerations

1. **Buffering**: Uses piece-aligned reads for efficiency
2. **Thread Pool**: No limit on concurrent threads
3. **Polling**: Busy-wait loop for piece availability (0.3s interval)

## Future Improvements

1. Add localhost-only binding option
2. Implement connection limits
3. Add HTTPS support for secure streaming
4. Consider asyncio for better concurrency
