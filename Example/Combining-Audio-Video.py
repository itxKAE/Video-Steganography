# Contribution: Syaiful, Kae Chuan

import os
import sys
import cv2

# Combiner Function
def combine_audio_video(video_object, audio_object, og_object):
    capture = cv2.VideoCapture(og_object) # Stores OG Video into a Capture Window
    fps = capture.get(cv2.CAP_PROP_FPS) # Extracts FPS of OG Video

    video_path = video_object + "%d.png" # To Get All Frames in Folder

    os.system("ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg -framerate \"%s\" -i %s -codec copy output\\combined_video_only.mkv" % (str(int(fps)), video_path)) # Combining the Frames into a Video
    os.system("ffmpeg-4.3.1-2020-10-01-full_build\\bin\\ffmpeg -i output\\combined_video_only.mkv -i \"%s\" -codec copy output\\combined_video_audio.mkv" % audio_object) # Combining the Frames and Audio into a Video

    print("Combining Complete!")

# Runtime
def main():
    try:
        video_filename, audio_filename, og_filename = sys.argv[1], sys.argv[2], sys.argv[3]
        combine_audio_video(video_filename, audio_filename, og_filename)
    except ValueError:
        print("Invalid File(s)!")

# Link
if __name__ == '__main__':
    main()