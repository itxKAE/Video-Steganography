import tkinter as tk
import sys
import os
import cv2

from PIL import Image
from moviepy.editor import *

def wrapper():
    """Wrapper function to call subfunction"""
    vf, base_filename = get_video_filename_base()
    option = var.get()
    if option == 1:
        video_object = VideoFileClip(vf)
        get_video(base_filename, video_object)
    elif option == 2:
        video_object = VideoFileClip(vf)
        get_audio(base_filename, video_object)
    elif option == 3:
        video_file = video_filename.get()
        audio_file = audio_filename.get()
        og_file = og_filename.get()
        combine_audio_video(video_file, audio_file, og_file)
    else:
        video_object = VideoFileClip(vf)
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
    video_object.write_videofile(filename=f'output\\{base_filename}_video_only.mp4', audio=False)

def get_audio(base_filename, video_object):
    """Returns the audio track only of a video clip"""
    video_object.audio.write_audiofile(filename=f'output\\{base_filename}_audio.wav')
    video_object.audio.write_audiofile(filename=f'output\\{base_filename}_audio.mp3')

def combine_audio_video(video_path, audio_path, og_path):
    """Combines an audio and a video object together"""
    capture = cv2.VideoCapture(og_path) # Stores OG Video into a Capture Window
    fps = capture.get(cv2.CAP_PROP_FPS) # Extracts FPS of OG Video

    video_path_real = video_path + "\\%d.png" # To Get All Frames in Folder

    os.system("ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg -framerate %s -i \"%s\" -codec copy output\\combined_video_only.mkv" % (str(int(fps)), video_path_real)) # Combining the Frames into a Video
    os.system("ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg -i output\\combined_video_only.mkv -i \"%s\" -codec copy output\\combined_video_audio.mkv" % audio_path) # Combining the Frames and Audio into a Video

    print("Combining Complete!")

def get_frames(video_object, base_filename):
    """Returns all frames in the video object"""
    directory = "output\\" + base_filename + '_frames\\'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for index, frame in enumerate(video_object.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{directory}{index}.png')

def sel():
    """Helper function to handle radio button selection"""
    if var.get() == 3:
        audio_filename_widget.config(state=tk.NORMAL)
        og_filename_widget.config(state=tk.NORMAL)
    else:
        audio_filename_widget.config(state=tk.DISABLED)
        og_filename_widget.config(state=tk.DISABLED)

window_main = tk.Tk()
window_main.title('AVI-Extractor')
window_main.geometry("400x200")
window_main.grid_columnconfigure((0,1), weight=1)
 
video_filename = tk.StringVar()

video_label = tk.Label(window_main, text="Video File/Frame Path: ")
video_label.grid(row=1, column=0)
 
video_filename_widget = tk.Entry(window_main, textvariable=video_filename)
video_filename_widget.grid(row=1, column=1)

audio_filename = tk.StringVar()

audio_label = tk.Label(window_main, text="Audio File: ")
audio_label.grid(row=2, column=0)
 
audio_filename_widget = tk.Entry(window_main, textvariable=audio_filename, state=tk.DISABLED)
audio_filename_widget.grid(row=2, column=1)

og_filename = tk.StringVar()

og_label = tk.Label(window_main, text="Original Video File: ")
og_label.grid(row=3, column=0)
 
og_filename_widget = tk.Entry(window_main, textvariable=og_filename, state=tk.DISABLED)
og_filename_widget.grid(row=3, column=1)

var = tk.IntVar()
R1 = tk.Radiobutton(window_main, text="Extract Video Without Audio", variable=var, value=1, command=sel)
R1.grid(row=4, columnspan=2, sticky=tk.W)

R2 = tk.Radiobutton(window_main, text="Extract Audio Without Video", variable=var, value=2, command=sel)
R2.grid(row=5, columnspan=2, sticky=tk.W)

R3 = tk.Radiobutton(window_main, text="Combine Audio and Video", variable=var, value=3, command=sel)
R3.grid(row=6, columnspan=2, sticky=tk.W)

R4 = tk.Radiobutton(window_main, text="Get Frames of Video", variable=var, value=4, command=sel)
R4.grid(row=7, columnspan=2, sticky=tk.W)

run = tk.Button(window_main, text="Run", command=wrapper)
run.grid(row=7, columnspan=2, sticky=tk.N)
 
window_main.mainloop() 