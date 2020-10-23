import tkinter as tk
from moviepy.editor import *
import sys
import os
from PIL import Image


def wrapper():
    """Wrapper function to call subfunction"""
    vf, base_filename = get_video_filename_base()
    video_object = VideoFileClip(vf)
    option = var.get()
    if option == 1:
        get_video(base_filename, video_object)
    elif option == 2:
        get_audio(base_filename, video_object)
    elif option == 3:
        af = get_audio_filename_base()
        audio_object = AudioFileClip(af)
        combine_audio_video(base_filename, video_object, audio_object)
    else:
        get_frames(video_object, base_filename)


def get_video_filename_base():
    """Returns filename and base filename"""
    vf = video_filename.get()
    return vf, os.path.splitext(os.path.basename(vf))[0]


def get_audio_filename_base():
    """Returns audio filename"""
    return audio_filename.get()

 
def get_video(base_filename, video_object):
    """Returns the video track only of a video clip"""
    video_object.write_videofile(filename=f'{base_filename}_video_only.mp4', audio=False)


def get_audio(base_filename, video_object):
    """Returns the audio track only of a video clip"""
    video_object.audio.write_audiofile(filename=f'{base_filename}_audio.wav')
    video_object.audio.write_audiofile(filename=f'{base_filename}_audio.mp3')

def combine_audio_video(base_filename, video_object, audio_object):
    """Combines an audio and a video object together"""
    video_object.set_audio(audio_object)
    video_object.write_videofile(filename=f'{base_filename}_combined.mp4')


def get_frames(video_object, base_filename):
    """Returns all frames in the video object"""
    directory = base_filename + '_frames/'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for index, frame in enumerate(video_object.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{directory}{index}.png')


def sel():
    """Helper function to handle radio button selection"""
    if var.get() == 3:
        audio_filename_widget.config(state=tk.NORMAL)
    else:
        audio_filename_widget.config(state=tk.DISABLED)


window_main = tk.Tk(className='budget vlc')
window_main.geometry("400x200")
window_main.grid_columnconfigure((0,1), weight=1)
 
video_filename = tk.StringVar()

video_label = tk.Label(window_main, text="Enter video filename: ")
video_label.grid(row=1, column=0)
 
video_filename_widget = tk.Entry(window_main, textvariable=video_filename)
video_filename_widget.grid(row=1, column=1)

audio_filename = tk.StringVar()

audio_label = tk.Label(window_main, text="Enter audio filename: ")
audio_label.grid(row=2, column=0)
 
audio_filename_widget = tk.Entry(window_main, textvariable=audio_filename, state=tk.DISABLED)
audio_filename_widget.grid(row=2, column=1)

var = tk.IntVar()
R1 = tk.Radiobutton(window_main, text="Get Video Only", variable=var, value=1, command=sel)
R1.grid(row=3, columnspan=2, sticky=tk.W)

R2 = tk.Radiobutton(window_main, text="Get Audio Only", variable=var, value=2, command=sel)
R2.grid(row=4, columnspan=2, sticky=tk.W)

R3 = tk.Radiobutton(window_main, text="Combine Audio and Video", variable=var, value=3, command=sel)
R3.grid(row=5, columnspan=2, sticky=tk.W)

R4 = tk.Radiobutton(window_main, text="Get Frames", variable=var, value=4, command=sel)
R4.grid(row=6, columnspan=2, sticky=tk.W)

run = tk.Button(window_main, text="Run", command=wrapper)
run.grid(row=7, columnspan=2, sticky=tk.N)
 
window_main.mainloop() 