# ASCII Image & Video to Text Art Converter (Windows Edition)

Turn your images **and** videos into expressive ASCII art directly in *Command Prompt* or *Windows Terminal* — complete with optional 24‑bit colour.

---

## ✨ Key Features

* **Drag‑and‑drop GUI** built with **Tkinter** – no command‑line needed for quick conversions.
* **CLI mode** for scripting and batch jobs.
* Handles common image formats *(PNG, JPG, BMP, GIF)* and popular video containers *(MP4, AVI, MOV, MKV)*.
* **True‑colour** output with the `--color` flag (requires a modern terminal).
* Adjustable output width that preserves aspect ratio.

---

## 📋 Prerequisites

| Dependency                              | Install Method                                                                                                                                     |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Windows 10 / 11**                     | 64‑bit recommended                                                                                                                                 |
| **Python 3.8 – 3.12 (64‑bit)**          | [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) <br>⚠️ Ensure “Add Python to PATH” is checked during setup. |
| **Pillow**                              | `pip install pillow`                                                                                                                               |
| **OpenCV‑Python**                       | `pip install opencv-python`                                                                                                                        |
| **NumPy**                               | `pip install numpy` *(auto‑installed by OpenCV but listed for clarity)*                                                                            |
| **Tkinter**                             | Bundled with the official Python installer                                                                                                         |
| **FFmpeg** (optional, for extra codecs) | 1. Chocolatey: `choco install ffmpeg` <br>2. Or download static build from [https://ffmpeg.org/](https://ffmpeg.org/) and add `bin` folder to PATH |

> **Note:** Colour output is best viewed in **Windows Terminal** or **PowerShell** (v5 +). Traditional *cmd.exe* supports ANSI colours only on Windows 10 v1703 or newer.

---

## ⚙️ Installation

1. **Download the script**

   ```pwsh
   # Example using PowerShell
   Invoke-WebRequest -Uri "https://example.com/ascii_converter.py" -OutFile "ascii_converter.py"
   ```

2. *(Optional but recommended)* **Create a virtual environment**

   ```cmd
   py -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Python packages**

   ```cmd
   pip install pillow opencv-python numpy
   ```

4. **(Optional) Install FFmpeg** for wider video codec support (see *Prerequisites*).

That's it! You’re ready to convert.

---

## 🚀 Quick Start

### GUI Mode

```cmd
py ascii_converter.py
```

1. A file dialog appears – select an image or video.
2. Set output width (characters) and tick **Enable Color** if desired.
3. Click **Convert**. ASCII art streams in your terminal.

### Command‑Line Mode

```cmd
py ascii_converter.py --input "C:\path\to\file.jpg" --width 120 --color
```

| Flag      | Purpose                       | Default |
| --------- | ----------------------------- | ------- |
| `--input` | Path to image/video           | –       |
| `--width` | Output width in characters    | `100`   |
| `--color` | Enable true‑colour ANSI codes | *off*   |

Example converting a video:

```cmd
py ascii_converter.py --input "demo.mp4" --width 80 --color
```

---

## 💡 Tips & Tricks

* **Performance:** Large widths + colour can be heavy. Reduce `--width` if playback stutters.
* **Interrupt:** Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to stop video playback.
* **Custom glyphs:** Edit the `ASCII_CHARS` array near the top of `ascii_converter.py` to change the character set.

---

## 🐞 Troubleshooting

| Problem                              | Solution                                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| *Module Not Found* errors            | Verify you activated the virtual environment and installed dependencies.                                                                          |
| Rainbow blocks instead of characters | Ensure you’re using Windows Terminal or enable VT processing in legacy console: `reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1`. |
| Video fails to open                  | Install FFmpeg and confirm file extension/codecs are supported. Try transcoding to H.264 MP4.                                                     |

---

## 🤝 Contributing

PRs are welcome! Please run **black** and target Windows compatibility.

---

## 📝 License

MIT License – see `LICENSE`.

---

> Crafted for Windows enthusiasts. Enjoy your ASCII adventures! 🚀
