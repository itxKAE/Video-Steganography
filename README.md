# Video Steganography Tool User Guide
This python script allows user to hide secret text file on media files such as image, audio, and video. It also allows Steganalysis of frames to identify Steganography-ed frames.

---

## Features
* Spliting Video into Audio and Frames
* Combining Audio and Frames into Video
* Hiding and Retrieving Data from Frames (Image Steganography)
* Hiding and Retrieving Data from Audio (Audio Steganography)
* Steganalysis of Frames

---

**Note 1: This tool only works with video file that has audio within them**

**Note 2: If you wish to view the changes in LSB Bits for Frames Steganography, uncomment line 1 and line 47 to 55 of analysis.py. Do remember to install matplotlib for the code to work**

---

## Table of Contents
* [Required Dependencies](#required-dependencies)
    * [Pillow](#installing-pillow)
    * [Tkinter](#installing-tkinter)
    * [OpenCV](#installing-opencv)
    * [Moviepy](#installing-moviepy)
    * [Matplotlib](#installing-matplotlib)
* [General Flow](#general-flow)
* [User Manual](#user-manual)
    * [Running the Application](#running-the-application)
    * [Main Menu](#main-menu)
    * [Splitting the Video](#splitting-the-video)
    * [Combining the Video](#combining-the-video)
    * [Hiding Data in wave Audio File](#hiding-data-in-wave-audio-file)
    * [Recovering Data in wave Audio File](#recovering-data-in-wave-audio-file)
    * [Hiding Data within Frames](#hiding-data-within-frames)
    * [Recovering Data within Frames](#recovering-data-within-frames)
    * [Detection of Frames with Hidden Data](#detection-of-frames-with-hidden-data)
    * [Output Folder](#output-folder)
* [Application Demo](#application-demo)
* [Softwares Used](#softwares-used)
* [Collaborators](#collaborators)

---

## Required Dependencies
The program requires the following dependencies to run. In the terminal tab: 
### Installing Pillow
     pip install pillow
### Installing Tkinter
     pip install tkinter
### Installing OpenCV
     pip install opencv-python
### Installing Moviepy
     pip install moviepy
### Installing Matplotib
     pip install matplotlib

---

## General Flow
![flowchart](/images/flowchart.png)

---

## User Manual

### Running the Application
     python file RunStartHere.py

---

### Main Menu

![Main Menu](/images/main.png)

1. The initial screen upon boot up
2. User can select the function to run by keying in the number 

---

### Splitting the Video

![Main Menu](/images/mainmenu_1.png)

1. Key in '1' and press enter


#### Getting the Video Frames

![Main Menu_1](/images/menu.PNG)

2. Select the 4th radio button
3. Key in the path to the video file on the first textbox (e.g. C://path/filename.mp4)
4. Click 'Run'
5. Extracted frames will be stored in /output/filename_frames folder (e.g. C://path/output/filename_frames/)

----

#### Getting the Audio

![audio_menu](/images/audio_menu.png)

2. Select the 2nd radio button
3. Key in the path to the video file on the first textbox (e.g. C://path/filename.mp4)
4. Click 'Run'
5. Extracted audio will be stored in /output folder as filename_audio.wav (e.g. C://path/output/filename_audio.wav)

---

### Combining the Video

![Main Menu](/images/mainmenu_1.png)

1. Key in '1' and press enter

![combine](/images/combine.png)

2. Select the 3rd radio button
3. Key in the path to the video frames on the first textbox (e.g. C://path/output/filename_frames)
4. Key in the path to the audio file on the second textbox (e.g. C://path/output/filename_audio.wav)
5. Key in the path to the original video file on the first textbox (e.g. C://path/filename.mp4)
6. Click 'Run'
7. Combined video will be stored in /output folder as combined_video_audio.mkv (e.g. C://path/output/combined_video_audio.mkv)

---

### Hiding Data in wave Audio File

![Main Menu](/images/mainmenu_2.png)

1. Key in '2' and press enter

![hide_audio1](/images/hide_audio1.png)

2. Key in the path of the text file to be hidden (e.g.  C://path/filename.txt)
3. Key in the path of the audio file (e.g. C://path/output/filename_audio.wav)
4. Key in the LSB Bits to hide data at (e.g. 3)

**Note: Value should be between 1 to 8**

5. System will inform of how many bytes are used to store the data

**Note: The entered LSB Bits and shown Bytes will be used for retrieval of data**

6. New audio file with the hidden data will be stored at /output folder as steg_audio.wav (e.g. C://path/output/steg_audio.wav)

---

### Recovering Data in wave Audio File

![Main Menu](/images/mainmenu_3.PNG)

1. Key in '3' and press enter

![recover_audio](/images/recover_audio.png)

2. Key in the path of the audio file to recover from (e.g. C://path/output/steg_audio.wav)
3. Key in the LSB Bits (e.g. 3)

**Note 1: Value should be between 1 to 8**

**Note 2: Value should be the same as the one entered during hiding**

4. Key in the number of bytes used to store the data (e.g. 380)

**Note: Value can be obtained from the system output during hiding**

5. Retrieved data will be stored at /output folder as decoded_audio.txt (e.g. C://path/output/decoded_audio.txt)

**Note 1: Incorrect LSB Bits entered leads to random data retrieved**

**Note 2: Lower bytes value entered leads to partial data retrieved**

**Note 3: Higher bytes value entered leads to full data retrieved with random data**

---

### Hiding Data within Frames

![Main Menu](/images/mainmenu_4.PNG)

1. Key in '4' and press enter

![hide_frame](/images/hide_frame.png)

2. Key in the initial frame to hide the data (e.g. 3)
3. Key in the last frame to hide the data (e.g. 6)

**Note 1: User can store the data within any range of the frame as long as the size of the frame can hold the data**

**Note 2: If the data stored is significantly small and a wide range of frames have been selected, this may lead to random data to be retrieved during recovery process**

**Note 3: Hiding a data over frames that has hidden data previously, may results in corruption of data **

4. Key in the path to the frames folder (e.g. C://path/output/filename_frames)
5. Key in the path to the text file to hide (e.g. C://path/filename.txt)
6. System informs that the data has been hidden

---

### Recovering Data within Frames

![Main Menu](/images/mainmenu_5.PNG)

1. Key in '5' and press enter

![recover_frame](/images/recover_frame_1.png)

2. Key in the initial frame to where data is hidden (e.g. 3)
3. Key in the last frame to where data data (e.g. 6)

**Note 1: The initial and last frame refers to a range of frames (e.g. initial = 3 | last = 8 | range = frame 3 to frame 8)**

**Note 2: If the data stored is significantly small and a wide range of frames have been selected, this may lead to random data to be retrieved during recovery process**

4. Key in the path to the frames folder (e.g. C://path/output/filename_frames)
5. Retrieved data will be stored in /output folder as decoded_frames.txt (e.g. C://path/output/decoded_frames.txt)

---

### Detection of Frames with Hidden Data

![Main Menu](/images/mainmenu_6.PNG)

1. Key in '6' and press enter

![detection_1](/images/detection_1.png)

2. Key in the path to the frames folder (e.g. C://path/output/filename_frames)
3. Key in the number of frames to perform Steganalysis on (e.g. 30)
4. Key in the file extension (e.g. png)

![detection_2](/images/detection_2.png)

5. System outputs the frames where Steganography has been detected

**Note 1: False-positive may occur if small amount of hidden data exists within the frame**

**Note 2: Despite missing some frames, the detection for image steganography are detected as accurate as possible**

---

### Output Folder

![output_circle](/images/output_circle.png)

This folder will be created upon launching the tool. The image above shows where the output folder will be located.

![output_folder](/images/output_folder.png)

Within the folder, these are all the files that have been created using this tool. The filename used for this example is 'test'.

---

## Application Demo

[![Watch the video](/images/video_thumbnail.png "Click here to watch the video")](https://www.youtube.com/watch?v=pIkr9EqpNRc)

---

## Softwares Used

* [Python 3.7](https://docs.python.org/3.7/)
* [FFmpeg](https://ffmpeg.org/download.html#build-windows)

---

## Collaborators
**TEAM AEGIS** 

1. **Tan Kae Chuan** | [@itxKAE](https://github.com/itxKAE)
1. **Mirza Haziq Bin Mohammed Yusoff** [@m1rzyq](https://github.com/m1rzyq) 
1. **Muhammad Syaifulnizar Bin Izam** | [@syaifulnizarrr](https://github.com/syaifulnizarrr)
1. **Christopher Gwee Soon Chai** | [@ManOCoolture](https://github.com/ManOCoolture)
1. **Ong Xing Hao** | [@XinhaoSITICT](https://github.com/XinhaoSITICT)
