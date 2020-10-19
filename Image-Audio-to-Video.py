from moviepy.editor import *
import os
import sys


def convert_frames_to_video(frames_folder):
    """Converts all frames to a video"""
    

    extension = ".png" #can be replace in others jpeg
    lengthExt = len(extension) # the length is 4

    # 0 to -4 in the folder, the -4 you delete off the from the extension/ then this will ilterate and get all the values of the files. 0-839
    listofframes = [img[0:-lengthExt] for img in os.listdir(frames_folder) if img.endswith(extension)]
    listofframes.sort(key = int) #sort them in terms of values. 0-839
    newFrameslist = ["{0}\{1}{2}".format(frames_folder,img,extension) for img in listofframes] # tidy up the frames. and rearrange it nicely.
    video_object = ImageSequenceClip(newFrameslist, fps=30) #can change the fps based on the video
    return video_object


def combine_audio_video(video_object, audio_object, base_filename):
    """Combines an audio and a video object together"""
    with_audio = video_object.set_audio(audio_object)
    with_audio.write_videofile(filename=f'{base_filename}_combined.mp4')


def main():
    try:
        frames_folder, audio_filename = sys.argv[1], sys.argv[2]
        # print(frames_folder, audio_filename)
        base_filename = os.path.splitext(os.path.basename(audio_filename))[0]
        video_object = convert_frames_to_video(frames_folder)
        convert_frames_to_video(frames_folder)
        audio_object = AudioFileClip(audio_filename)
        combine_audio_video(video_object, audio_object, base_filename)
    except ValueError:
        print("Invalid filenames!")

if __name__ == '__main__':
    main()