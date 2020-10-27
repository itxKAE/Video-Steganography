## ICT2202 - Video-Steganography

## Description
**This python script allows user to hide secret text file on to media files such as image files, audio files, and video files.**

## Table of Contents
* [Getting Started](#getting-started)
  * [Manual Installation Required Dependencies](#manual-installation-required-dependencies)
    * [Installing Pillow](#installing-pillow)
    * [Installing Tkinter](#installing-tkinter)
    * [Installing OpenCV](#installing-opencv)
    * [Installing Moviepy](#installing-moviepy)
* [Running Application](#running-application)
    * [How to run the application](#how-to-run-the-application)
    * [GUI](#gui)
    * [Extraction and Combining](#extraction-and-combining)
    * [Hiding and Recover data in or from wave audio file](#hiding-and-recover-data-in-or-from-wave-audio-file)
    * [Hide or Recover Text file data in/from image file](#hide-or-recover-text-file-data-in-or-from-image-file)
    * [Detection](#detection)
* [Application Demo Video](#application-demo-video)
* [Developed With](#developed-with)
* [Project Details](#project-details)
* [Collaborators](#collaborators)

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

#### How to run the application

     Run the python file "RunStartHere.py"

#### GUI
1. It will launch the command-line based GUI for the user to select their desired option.

	![Main Gui](/images/maingui.PNG)

2. If user wants to prepare the video file for steganography, select option 1: Video Splitter and Combiner.
3. User would then be presented with a Tkinter GUI in order to insert their file paths, select options and such.

	![Avi Gui](/images/avigui.PNG)

#### Extraction and Combining

4. Select the desired options and fill in the file paths

* 4.1 If the user desired to extract video without audio, the desired output will be shown on the output folder with filename_video_only.mp4
1st Picture
radio button with filename.mp4
	
* 4.2 If the user desired to extract audio without video, the desired output will be shown on the output folder with <filename>_audio.wav
2nd Picture
radio button with <filename>.mp4
	
* 4.3 If the user desired to extract audio without video, the desired output will be shown on the output folder with <filename>_audio.mp3
3rd Picture
radio button with <filename>.mp4
	
* 4.4 If the user desired to extract frames of video, the desired output will be shown on the output folder with <filename>_frames
4th Picture
radio button with <filename>.mp4
	
* 4.5 If the user desired to combined Audio and Video, the user need to enter the Video file and audio file, then the desired output will be shown on the output folder with <filename>_combined_video_audio.mkv
5th Picture
radio button with two filenames

#### Hiding and Recover data in or from wave audio file

5. Select 2 or 3 in order to hide or recover text file in a wave audio file.
* 5.1 If the user press 2 and user desired was to hide text file in a wave audio file.

	![Hide Audio](/images/hideaud.png)

* 5.2 If the user press 3 and user desired was to recover text file in a wave audio file. Image Below

6. Fill in the desired file paths and desired LSB to hide/recover the text file. The input name of the output file will be produced. 
* 6.1 The output for the hiding the text file in a wave audio file. Image Below

* 6.2 The output for the recover the text file in a wave audio file. Image below

#### Hide or Recover Text file data in or from image file

7. Select 4 or 5 in order to hide or recover text file in to the image file.
* 7.1 If the user choose number 4 and desired to hide text file in to the image. Image Below

* 7.2 If the user choose number 5 and desired to recover data in the frames. Image below

* 7.3 The output for 7.1 and 7.2

#### Detection

8. Select 6 in order to detect steganography in images done in selection 4
* 8.1 The user selects option number 6 and choose file path / file directory for selection after hide text file or before recover the data. Images Below
* 8.2 Image below after hide text file
* 8.3 Image below before recover the data

## Application Demo Video

[![Watch the video](<!--Link from github, screenpic--> "Click here to watch the video")](<!-- Youtube Link)

## Developed With

* [Python 3.7](https://docs.python.org/3.7/)
* [FFmpeg](https://ffmpeg.org/download.html#build-windows)

## Project Details

* [X] **Splitting Video**
* [X] **Steganography Frames or Audio**
* [X] **Combination of Frames and Audio into Video**
* [X] **Play Video to Ensure it is okay**
* [X] **Splitting Video**
* [X] **Extract from Audio**
* [X] **Detect Which Frames Data are Hidden**
* [X] **Extract From Frames**

## Collaborators
**TEAM AEGIS** 

1. **Tan Kae Chuan** | [@itxKAE](https://github.com/itxKAE)
1. **Mirza Haziq Bin Mohammed Yusoff** [@m1rzyq](https://github.com/m1rzyq) 
1. **Muhammad Syaifulnizar Bin Izam** | [@syaifulnizarrr](https://github.com/syaifulnizarrr)
1. **Christopher Gwee Soon Chai** | [@ManOCoolture](https://github.com/ManOCoolture)
1. **Ong Xing Hao** | [@XinhaoSITICT](https://github.com/XinhaoSITICT)
