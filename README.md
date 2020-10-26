Video-Steganography

#Description
This python script allows user to hide secret text file
on to media files such as image files, audio files, and video files.

## Table of Contents <! -- TOC of Using it -->
* [Getting Started](#getting-started)
  * [Manual Installation](#manual-installation)
    * [Installing Pillow](#installing-pillow)
    * [Installing Tkinter](#installing-tkinter)
    * [Installing OpenCV](#installing-opencv)
    * [Installing Moviepy](#installing-moviepy)
* [Steps](#Steps)
* [Getting Started](#getting-started)
* [Running Application](#running-application)
* [Application Demo Video](#application-demo-video)

## Getting Started

### Manual Installation
Install libraries/dependencies into directory path

#### Installing Pillow

     pip install pillow

#### Installing Tkinter
#### Installing OpenCv
#### Installing Moviepy

## Steps
1) Run the RunStartHere.py in order to run the program.
   It will launch the command-line based GUI for the user to select their desired option.

	![Main Gui](/images/maingui.PNG)

2) If user wants to prepare the video file for steganography, select option 1: Video Splitter and Combiner.
3) User would then be presented with a Tkinter GUI in order to insert their file paths, select options and such.

	![Avi Gui](/images/avigui.PNG)

4) Select the desired options and fill in the file paths.
5) Run the selections and an output file would be produced.
6) Select 2 or 3 in order to hide or recover text file in a wave audio file.

	![Hide Audio](/images/hideaud.png)

7) Fill in the desired file paths and desired LSB to hide/recover the text file. The input name of the output file will be produced. 
8) Select 4 or 5 in order to hide or recover text file in to the image file.
9) Fill in the desired file paths
10) Select 6 in order to detect steganography in images done in selection 4
