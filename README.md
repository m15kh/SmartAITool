# SmartAITool

A smart AI tool package for Python that provides useful utilities for terminal output formatting, data processing, and video manipulation.

## Installation

```bash
pip install SmartAITool
```

*You can download the package by running the above command.*

## Usage

### Colored Terminal Output

```python
from SmartAITool import core

# Print with colored output
core.cprint("Success message", "green")
core.cprint("Error message", "red")
core.cprint("Warning message", "yellow")
core.cprint("Information message", "blue")
```

### Video Processing

```python
from SmartAITool import video

# Get video information
video_info = video.get_video_info("input_video.mp4")
print(f"FPS: {video_info['fps']}, Resolution: {video_info['width']}x{video_info['height']}")

# Extract frames from a video
video.extract_frames("input_video.mp4", "output_frames_dir", start_frame=0, end_frame=100)

# Create a video from frames
video.create_video("frames_directory", "output_video.mp4", fps=30)
```

## Features

- **Colored Terminal Output**: Easy-to-use colored text printing in terminal
- **Support for 8 Colors**: black, red, green, yellow, blue, magenta, cyan, white
- **Simple API**: Intuitive and straightforward functions
- **Video Processing**: Tools for extracting frames and creating videos

## Development

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/m15kh/SmartAITool.git
cd SmartAITool

# Install development dependencies
pip install -r requirements-dev.txt

# WARNING: Error during upload
# Retry with the --verbose option for more details.

# Install the package in development mode
pip install -e .
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
