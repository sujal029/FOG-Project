# Video Editing Project

This project provides a script to create a short video with dynamic font size text overlays and background music from a longer video. The final video is cropped to a 9:16 aspect ratio and adjusted to a specified duration.

## Files

- `longshortvideo.py`: Contains the function to create a short video with dynamic font size text overlays.
- `main.py`: Example usage of the function provided in `longshortvideo.py`.

## Requirements

- Python 3.x
- moviepy
- ImageMagick

You can install the required Python packages using pip:

```sh
pip install moviepy
```

### Installing ImageMagick

1. Download ImageMagick from the [official website](https://imagemagick.org/script/download.php).
2. Follow the installation instructions for your operating system.
3. Ensure that ImageMagick is added to your system's PATH.

## Usage

### Example Usage in `main.py`

1. Set the path to your input video, output video, and background music.
2. Define the interesting clips with their start and end times.
3. Define the text overlays with their display time, content, and position.
4. Run the script to create the short video.

```python
# Example usage
# Enter Your Large video path
input_video = "long.mp4"

# Set your output video path to be saved
output_video = "short_video_9x16.mp4"

# Enter Background music path
music_path = "background.mp3"

# Set clips start and end time
interesting_clips = [(5, 10), (15, 22), (30, 35)]  # Ensure total duration >= 30 seconds

# Overlay text with (display time, content, position) 
text_overlays = [
    (0, "Exciting Start!", "center"),
    (8, "Keep Watching!", "bottom"),
    (22, "Epic Ending!", "center"),
]

# Create a short video
create_short_video_dynamic_fontsize(input_video, output_video, interesting_clips, music_path, text_overlays)
```

### Function in `longshortvideo.py`

The function `create_short_video_dynamic_fontsize` takes the following parameters:

- `input_video_path`: Path to the input video file.
- `output_video_path`: Path to save the output video file.
- `interesting_clips`: List of tuples for clip start and end times.
- `music_path`: Path to the background music file.
- `text_overlays`: List of tuples (time, text, position) for text overlays.
- `final_duration`: Desired final video duration in seconds (default is 30 seconds).

## License

This project is licensed under the MIT License.
