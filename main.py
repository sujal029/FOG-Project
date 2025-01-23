import moviepy.editor as mpe
from moviepy.video.fx import crop


def create_short_video_dynamic_fontsize(
    input_video_path,
    output_video_path,
    interesting_clips,  # List of tuples for clip start and end times
    music_path,
    text_overlays,  # List of tuples (time, text, position)
    final_duration=30,  # Desired final video duration in seconds
):
    # Load the input video
    video = mpe.VideoFileClip(input_video_path)

    # Calculate dynamic font size based on video height
    font_size = int(video.h * 0.05)  # 5% of video height

    # Ensure 9:16 aspect ratio by cropping
    clips = []
    for start, end in interesting_clips:
        clip = video.subclip(start, end)
        # Crop to 9:16 (e.g., 720x1280 or center the content)
        height = clip.h
        width = int(height * (9 / 16))  # Adjust width for 9:16
        x_center = clip.w // 2  # Center horizontally
        cropped_clip = crop.crop(
            clip, width=width, height=height, x_center=x_center, y_center=clip.h // 2
        )
        clips.append(cropped_clip)

    # Concatenate the cropped clips
    short_video = mpe.concatenate_videoclips(clips, method="compose")

    # Adjust duration to ensure it's exactly 30 seconds
    if short_video.duration > final_duration:
        short_video = short_video.subclip(0, final_duration)
    elif short_video.duration < final_duration:
        factor = short_video.duration / final_duration
        short_video = short_video.fx(mpe.vfx.speedx, factor=factor)

    # Add text overlays with dynamic font size
    text_clips = []
    for time, text, position in text_overlays:
        txt_clip = (
            mpe.TextClip(
                text,
                fontsize=font_size,  # Use dynamic font size
                color="white",
                stroke_color="black",
                stroke_width=1,
            )
            .set_position(position)
            .set_start(time)
            .set_duration(3)  # Text duration
        )
        text_clips.append(txt_clip)

    # Add text overlays to the video
    short_video = mpe.CompositeVideoClip([short_video] + text_clips)

    # Add background music
    music = mpe.AudioFileClip(music_path).set_duration(short_video.duration)
    short_video = short_video.set_audio(music)

    # Export the final video in 9:16 ratio
    short_video.write_videofile(
        output_video_path,
        codec="libx264",
        audio_codec="aac",
        fps=24,
        threads=4,
    )


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