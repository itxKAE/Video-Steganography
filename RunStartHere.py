import os

#Start
print("\n1: Hide data in audio\n2: Recover data in audio")

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

    else:
        print("\nInvalid Input! Application will exit!\n")
        quit()

except ValueError:
    print("Non integer input entered. Application will end!")


