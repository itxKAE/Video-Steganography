import os

#Start
print("\n1: Hide data in audio\n2: Recover data in audio\n3: Steganography Detection in Images\n4: Encoder\n5: Decoder")
print("6: Video Splitter and Combiner")
#print("6: Video Splitter\n7: Video + Audio Combiner:\n8: Image Frames + Audio Combiner")

try:
    start_step = int(input("\nChoose what to do:"))

    #Selection Options
    if start_step == 1:
        file_text = str(input("\nText file to hide:"))
        file_audioOld = str(input("Wav file name:"))
        file_audioNew = str(input("Name of output file:"))
        bits_int = str(input("LSB bits:"))
        line_string = ("python wav-steg.py -h -d " + file_text + " -s " + file_audioOld + " -o " + file_audioNew + " -n " + bits_int)
        os.system(line_string)

    elif start_step == 2:
        audio_file = str(input("\nFile to recover from:"))
        text_New = str(input("\nOutput text file name:"))
        no_of_lsb_bits = str(input("LSB bits:"))
        no_of_bytes = str(input("Number of bytes:"))
        line_string = ("python wav-steg.py -r -s " + audio_file + " -o " + text_New + " -n " + no_of_lsb_bits + " -b " + no_of_bytes)
        os.system(line_string)

    elif start_step == 3:
        steg_det = str(input("\nSteganograhpy Image Detection"))
        os.system("python analysis.py")

    elif start_step == 4:
        os.system("python Encoder.py")

    elif start_step == 5:
        os.system("python Decoder.py")

    elif start_step == 6:
        os.system("python aviGUI.py")

    #elif start_step == 6:
     #   vid_file = str(input("\nVideo File Name:"))
     #   line_string = ("python audio-video-image-splitter.py " + vid_file)
     #   os.system(line_string)

    #elif start_step == 7:
     #   vid_file = str(input("\nVideo File Name(no audio):"))
     #   aud_file = str(input("\nAudio File Name:"))
      #  line_string = ("python Combining-Audio-Video.py " + vid_file + " " + aud_file)
      #  os.system(line_string)

   # elif start_step == 8:
    #    image_folder = str(input("\nImage Folders:"))
     #   aud_file = str(input("\nAudio File Name:"))
    #    line_string = ("python Image-Audio-to-Video.py " + image_folder + " " + aud_file)
     #   os.system(line_string)



    else:
        print("\nInvalid Input! Application will exit!\n")
        quit()

except ValueError:
    print("Non integer input entered. Application will end!")


