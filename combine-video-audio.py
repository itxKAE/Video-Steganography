from moviepy.editor import *
import os
import sys


def combine_audio_video(video_object, audio_object, base_filename):
    """Combines an audio and a video object together"""
    with_audio = video_object.set_audio(audio_object)
    with_audio.write_videofile(filename=f'{base_filename}_combined.mp4')


def main():
    try:
        video_filename, audio_filename = sys.argv[1], sys.argv[2]
        print(video_filename, audio_filename)
        base_filename = os.path.splitext(os.path.basename(video_filename))[0]
        video_object = VideoFileClip(video_filename)
        audio_object = AudioFileClip(audio_filename)
        combine_audio_video(video_object, audio_object, base_filename)
    except ValueError:
        print("Invalid filenames!")

if __name__ == '__main__':
    main()