## ICT2202 - Video-Steganography

## Description
### This python script allows user to hide secret text file on to media files such as image files, audio files, and video files.

## Table of Contents
* [Getting Started](#getting-started)
  * [Manual Installation Required Dependencies](#manual-installation-required-dependencies)
    * [Installing Pillow](#installing-pillow)
    * [Installing Tkinter](#installing-tkinter)
    * [Installing OpenCV](#installing-opencv)
    * [Installing Moviepy](#installing-moviepy)
* [Running Application](#running-application)
* [Application Demo Video](#application-demo-video)
* [Developed With](#developed-with)
* [Project Details](#project-details)
* [Collaborators With Contributions](#collaborators-with-contributions)

## Getting Started

### Manual Installation
In order to run our program, you need to install these individual required dependencies in your directory path. In your terminal tab: 

#### Installing Pillow

     pip install pillow

#### Installing Tkinter

     pip install tkinter
     
#### Installing OpenCV

     pip install opencv-python
     
#### Installing Moviepy

     pip install moviepy


## Running Application

**How to run the application:**

     Run the python file "RunStartHere.py"
     
1. It will launch the command-line based GUI for the user to select their desired option.

	![Main Gui](/images/maingui.PNG)

2. If user wants to prepare the video file for steganography, select option 1: Video Splitter and Combiner.
3. User would then be presented with a Tkinter GUI in order to insert their file paths, select options and such.

	![Avi Gui](/images/avigui.PNG)

4. Select the desired options and fill in the file paths
4.1 If the user desired to extract video without audio, the desired output will be shown on the output folder with <filename>_video_only.mp4
	1st Picture
	radio button with <filename>.mp4
4.2. If the user desired to extract audio without video, the desired output will be shown on the output folder with <filename>_audio.wav
	2nd Picture
	radio button with <filename>.mp4
4.3. If the user desired to extract audio without video, the desired output will be shown on the output folder with <filename>_audio.mp3
	3rd Picture
	radio button with <filename>.mp4
4.4. If the user desired to extract frames of video, the desired output will be shown on the output folder with <filename>_frames
	4th Picture
	radio button with <filename>.mp4
4.5. If the user desired to combined Audio and Video, the user need to enter the Video file and audio file, then the desired output will be shown on the output folder with <filename>_combined_video_audio.mkv
	5th Picture
	radio button with two filenames
	
5. Select 2 or 3 in order to hide or recover text file in a wave audio file.

	![Hide Audio](/images/hideaud.png)

6. Fill in the desired file paths and desired LSB to hide/recover the text file. The input name of the output file will be produced. 
7. Select 4 or 5 in order to hide or recover text file in to the image file.
8. Fill in the desired file paths
9. Select 6 in order to detect steganography in images done in selection 4

## Application Demo Video

[![Watch the video](<!--Link from github, screenpic--> "Click here to watch the video")](<!-- Youtube Link)

## Developed With

* [Python 3.7](https://docs.python.org/3.7/)
* [FFmpeg](https://ffmpeg.org/download.html#build-windows)

## Project Details

* [X] **Splitting Video**
* [X] **Steganograph Frames or Audio **
* [X] **Combination of Frames and Audio into Video**
* [X] **Play Video to Ensure it is okay**
* [X] **Splitting Video**
* [X] **Extract from Audio**
* [X] **Detect Which Frames Data are Hidden**
* [X] **Extract From Frames**

## Collaborators with Contributions
**TEAM AEGIS** 

1. **Tan Kae Chuan** | [@itxKAE](https://github.com/itxKAE)
   * Test
   * Test
1. **Mirza Haziq Bin Mohammed Yusoff** [@m1rzyq](https://github.com/m1rzyq) 
   * Test
1. **Muhammad Syaifulnizar Bin Izam** | [@syaifulnizarrr](https://github.com/syaifulnizarrr)
   * Test
1. **Christopher Gwee Soon Chai** | [@ManOCoolture](https://github.com/ManOCoolture)
   * Test
1. **Ong Xing Hao** | [@XinhaoSITICT](https://github.com/XinhaoSITICT)
   * Test
