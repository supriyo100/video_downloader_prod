---

# 🎬 Video Downloader & Converter

A **production-ready, modular Python solution** to download segmented video files (`.ts`) and merge them into a single `.mp4` file using FFmpeg.

Designed with clean architecture, robust error handling, and production-level logging.

---

## 🚀 Features

* ✅ **Automatic 404 Detection** — Stops gracefully when segments end
* ✅ **Flexible Input** — Single URL, multiple URLs, or URLs from file
* ✅ **Robust Error Handling** — Timeout, retry logic, safe termination
* ✅ **Modular Architecture** — 8 independent, testable components
* ✅ **Production Ready** — Logging, validation, pipeline orchestration
* ✅ **Comprehensive Logging** — Console + file output
* ✅ **FFmpeg Integration** — Safe concat demuxer merging

---

## 📦 Installation

### Requirements

* Python 3.8+
* FFmpeg installed and accessible in PATH
* Internet connection

---

### Setup

```bash
# Clone repository
git clone https://github.com/supriyo100/video_downloader_prod.git
cd video_downloader_prod

# Install dependencies
pip install -r requirements.txt

# Make executable (Linux/macOS)
chmod +x main.py
```

---

## ▶️ Usage

### Basic Command

```bash
python main.py -u "https://example.com/segment_{:03d}.ts" -o video.mp4
```

Example for `segment_001.ts`, `segment_002.ts`, etc.

---

### Multiple URLs

```bash
python main.py -u "https://server1.com/part_{}.ts" -o video.mp4
```

---

### From File

If you have multiple URL templates:

```bash
python main.py -u urls.txt -o video.mp4
```

---

### Keep Downloaded Segments

```bash
python main.py -u "https://example.com/og_{}.ts" -o video.mp4 --keep-segments
```

---

### Advanced Usage

```bash
python main.py \
  -u "https://example.com/og_{}.ts" \
  -o my_video.mp4 \
  --timeout 60 \
  --keep-segments \
  --debug
```

---

## ⚙️ CLI Options

### Required

```
-u, --url           URL template or file containing URLs
```

### Optional

```
-o, --output        Output filename (default: output.mp4)
--download-dir      Segment download directory
--temp-dir          Temporary working directory
--timeout           Download timeout (seconds)
--keep-segments     Keep downloaded .ts files
--keep-temp         Keep temporary files
--log-file          Custom log file path
--debug             Enable debug mode
-h, --help          Show help message
```

---

## 🌐 URL Format

Your URL **must contain a placeholder `{}`** for the segment index.

### ✅ Correct

```
https://example.com/segment_{}.ts
https://example.com/og_{:03d}.ts
https://example.com/part_{}.mp4
```

### ❌ Incorrect

```
https://example.com/segment_0.ts
https://example.com/video.ts
```

---

## 🏗 Project Structure

```
video_downloader_prod/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   └── core/
│       ├── logger.py
│       ├── config.py
│       ├── input_validator.py
│       ├── ffmpeg_checker.py
│       ├── downloader.py
│       ├── merger.py
│       ├── cleanup.py
│       └── pipeline.py
├── tests/
├── scripts/
└── docs/
```

---

## 🧠 Module Overview

### 🔹 Logger

Centralized logging system (console + file) with proper severity levels.

### 🔹 Config

Validates configuration parameters such as timeouts and paths.

### 🔹 InputValidator

Parses and validates user inputs.

### 🔹 FFmpegChecker

Ensures FFmpeg is installed before execution.

### 🔹 SegmentDownloader

Downloads sequential segments starting from index 0.
Stops on:

* HTTP 404 (normal termination)
* 3 consecutive failures

### 🔹 VideoMerger

Uses FFmpeg concat demuxer for fast and reliable merging.

### 🔹 FileCleanup

Handles temporary and optional file removal.

### 🔹 VideoPipeline

Main orchestrator controlling full execution flow.

---

## 🛑 Error Handling

| Scenario             | Behavior                          |
| -------------------- | --------------------------------- |
| 404 Error            | Graceful stop (download complete) |
| Network Timeout      | Retry (default: 2 attempts)       |
| Consecutive Failures | Stop after 3 failures             |
| Output Exists        | Raises `FileExistsError`          |
| Missing FFmpeg       | Shows install instructions        |
| Invalid URL          | Raises `ValueError`               |

---

## 📜 Logging

### Console

* INFO level and above

### File (`video_downloader.log`)

* DEBUG level and above

### Sample Output

```
2026-02-26 10:30:45 - INFO - VIDEO DOWNLOADER & CONVERTER
2026-02-26 10:30:45 - INFO - ✓ FFmpeg available
2026-02-26 10:30:46 - INFO - Starting download...
2026-02-26 10:31:00 - INFO - Segment 034 not found (404) - Download complete
2026-02-26 10:31:00 - INFO - ✓ Downloaded 34 segments
2026-02-26 10:31:20 - INFO - ✓ Created video.mp4 (2048.50 MB)
2026-02-26 10:31:21 - INFO - ✓ COMPLETED IN 35.2 SECONDS
```

---

## ⚡ Performance

| Stage    | Time          |
| -------- | ------------- |
| Download | 1–30 minutes  |
| Merge    | 10–30 seconds |
| Total    | 10–45 minutes |

Disk usage: 1–3 GB (depending on video size)

---

## 🔧 Troubleshooting

### FFmpeg Not Found

**macOS**

```bash
brew install ffmpeg
```

**Ubuntu/Debian**

```bash
sudo apt-get install ffmpeg
```

**Windows**
Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

---

### File Already Exists

Use a different output filename or delete the existing file.

---

### No Segments Downloaded

* Ensure `{}` placeholder exists
* Test URL in browser
* Check internet connectivity
* Review logs:

  ```bash
  cat video_downloader.log
  ```

---

## 🧪 Development

### Run Tests

```bash
python -m pytest tests/
```

### Format Code

```bash
black src/ main.py
```

### Lint

```bash
pylint src/ main.py
```

### Type Check

```bash
mypy src/ main.py
```

---

## 📄 License

MIT License

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit changes
4. Push to branch
5. Open Pull Request

---

## 📌 Version

* Version: 1.0.0
* Status: Production Ready
* Last Updated: 2026-02-26

---

# 🎉 Ready to Use

Install, configure, and start downloading segmented videos safely and efficiently.

**Happy downloading! 🚀**
