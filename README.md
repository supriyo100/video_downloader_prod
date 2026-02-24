# Video Downloader & Converter

A production-ready, modular solution to download segmented video files (.ts) and merge them into MP4.

## Features

- ✅ **Automatic 404 Detection** - Stops when segment not found (normal completion)
- ✅ **Flexible Input** - Single URL, multiple URLs, or URLs from file
- ✅ **Robust Error Handling** - Proper exceptions, warnings, and logging
- ✅ **Modular Architecture** - 8 independent, testable components
- ✅ **Production Ready** - Timeout handling, retry logic, progress bars
- ✅ **Comprehensive Logging** - Console and file output with proper levels

## Installation

### Requirements

- Python 3.8+
- FFmpeg
- Internet connection

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/video_downloader_prod.git
cd video_downloader_prod

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x main.py
```

## Usage

### Command Line

```bash
# Basic usage
python main.py -u "https://example.com/segment_{:03d}.ts" -o video.mp4  #for segment_00i.ts 

# Multiple URLs
python main.py -u "https://server1.com/part_{}.ts" -o video.mp4

# From file
python main.py -u urls.txt -o video.mp4

# Keep segments
python main.py -u "https://..." -o video.mp4 --keep-segments

# With options
python main.py \
  -u "https://...og_{}.ts" \
  -o my_video.mp4 \
  --timeout 60 \
  --keep-segments \
  --debug
```

### Options

```
Required:
  -u, --url           URL template or file path with URLs

Optional:
  -o, --output        Output filename (default: output.mp4)
  --download-dir      Segment download directory
  --temp-dir          Temporary directory
  --timeout           Download timeout in seconds
  --keep-segments     Keep .ts files after merge
  --keep-temp         Keep temporary files
  --log-file          Log file path
  --debug             Enable debug mode
  -h, --help          Show help
```

## URL Format

Your URL must have a placeholder `{}` for the segment index:

```
✓ Correct:
  https://example.com/segment_{}.ts
  https://example.com/og_{}.ts
  https://example.com/part_{}.mp4

✗ Wrong:
  https://example.com/segment_0.ts
  https://example.com/video.ts
```

## Project Structure

```
video_downloader_prod/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore patterns
├── README.md              # This file
├── src/
│   └── core/
│       ├── __init__.py
│       ├── logger.py      # Logging
│       ├── config.py      # Configuration
│       ├── input_validator.py  # Input validation
│       ├── ffmpeg_checker.py   # FFmpeg check
│       ├── downloader.py  # Segment download
│       ├── merger.py      # Video merge
│       ├── cleanup.py     # File cleanup
│       └── pipeline.py    # Main orchestrator
├── tests/                 # Unit tests
├── scripts/               # Utility scripts
└── docs/                  # Documentation
```

## Module Overview

### Logger
Centralized logging with console and file output. Supports info, debug, warning, error, and success levels.

### Config
Configuration management with validation. Handles paths, timeouts, and retry settings.

### InputValidator
Validates and parses user input. Supports single URL, list of URLs, and file paths.

### FFmpegChecker
Checks FFmpeg installation and availability.

### SegmentDownloader
Downloads video segments starting from index 0. Stops on 404 error or consecutive failures.

### VideoMerger
Merges downloaded segments using FFmpeg concat demuxer.

### FileCleanup
Manages cleanup of temporary and downloaded files.

### VideoPipeline
Orchestrates the complete pipeline - validation, download, merge, cleanup.

## Error Handling

- **404 Error**: Graceful stop (normal completion)
- **Network Timeout**: Retry up to 2 times
- **Consecutive Failures**: Stop after 3 failures
- **File Exists**: Raises FileExistsError
- **Missing FFmpeg**: Shows installation instructions
- **Invalid URL**: Raises ValueError

## Logging

All operations are logged to:
- **Console**: INFO level and above
- **File** (`video_downloader.log`): DEBUG level and above

Example output:
```
2024-01-15 10:30:45 - INFO - ============================================================
2024-01-15 10:30:45 - INFO - VIDEO DOWNLOADER & CONVERTER
2024-01-15 10:30:45 - INFO - ✓ FFmpeg available
2024-01-15 10:30:46 - INFO - Validating inputs...
2024-01-15 10:30:46 - INFO - ✓ Parsed 1 URL(s)
2024-01-15 10:30:47 - INFO - Starting download...
2024-01-15 10:31:00 - INFO - Segment 034 not found (404) - Download complete
2024-01-15 10:31:00 - INFO - ✓ Downloaded 34 segments
2024-01-15 10:31:20 - INFO - ✓ Created video.mp4 (2048.50 MB)
2024-01-15 10:31:21 - INFO - ✓ COMPLETED IN 35.2 SECONDS
```

## Performance

- **Download**: 1-30 minutes (depends on file size & network)
- **Merge**: 10-30 seconds
- **Total**: 10-45 minutes
- **Disk Usage**: 1-3 GB

## Troubleshooting

### FFmpeg not found

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### "File already exists"

Use different filename or delete existing file.

### No segments downloaded

- Check URL format (must have `{}`)
- Verify internet connection
- Check server accessibility
- Review logs: `cat video_downloader.log`

### URL not working

- Verify `{}` placeholder exists
- Test URL in browser
- Check if server is accessible

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Style

```bash
# Format code
black src/ main.py

# Lint
pylint src/ main.py

# Type check
mypy src/ main.py
```

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## Support

For issues and questions:
1. Check the logs: `video_downloader.log`
2. Review troubleshooting section
3. Create an issue on GitHub

## Version

- **Version**: 1.0.0
- **Status**: Production Ready
- **Last Updated**: 2026-02-26

---

**Ready to use! Install, configure, and start downloading.** 🚀
