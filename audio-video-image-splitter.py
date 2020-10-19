import moviepy.editor
import sys
import os
from moviepy.editor import *
from PIL import Image


def get_video(video_object, base_filename):
    """Returns the video track only of a video clip"""
    video_object.write_videofile(filename=f'{base_filename}_video_only.mp4', audio=False)


def get_audio(video_object, base_filename):
    """Returns the audio track only of a video clip"""
    video_object.audio.write_audiofile(filename=f'{base_filename}_audio.mp3')
    video_object.audio.write_audiofile(filename=f'{base_filename}_audio.wav')

def get_frames(video_object, base_filename):
    """Returns the frame at a particular timestamp of a video clip"""
    directory = base_filename + '_frames/'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for index, frame in enumerate(video_object.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{directory}{index}.png')

def main():
    try:
        filename = sys.argv[1]
        base_filename = os.path.splitext(os.path.basename(filename))[0]
        if os.path.isfile(filename):
            video_object = VideoFileClip(filename)
            get_video(video_object, base_filename)
            get_audio(video_object, base_filename)
            get_audio(video_object, base_filename)
            get_frames(video_object, base_filename)
    except ValueError:
        print("Invalid filename or path not found!")


if __name__ == '__main__':
    main()