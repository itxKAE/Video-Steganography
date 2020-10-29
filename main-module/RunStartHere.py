import os

# Checks if output Directory Exists, otherwise Create It
if not os.path.exists('output'):
    os.makedirs('output')

# Menu
print("\n1: Video Splitter and Combiner")
print("2: Hide Data in Audio")
print("3: Recover Data in Audio")
print("4: Hide Data in Frames")
print("5: Recover Data in Frames")
print("6: Steganography Detection in Images")

# User Selection
try:
    start_step = int(input("\nSelect the Program to Run: "))

    if start_step == 1:
        print("Starting Program...\n")
        os.system("python aviGUI.py")

    if start_step == 2:
        print("Starting Program...\n")
        print("=== Hide Data in Audio ===")
        file_text = input("Text File to Hide: ")
        file_audioOld = input("Original Audio File (inc. extension): ")
        bits_int = str(input("LSB Bits: "))
        line_string = ("python wav-steg.py -h -d \"" + file_text + "\" -s \"" + file_audioOld + "\" -o  output\steg_audio.wav" + " -n " + bits_int)
        os.system(line_string)

    elif start_step == 3:
        print("Starting Program...\n")
        print("=== Recover Data in Audio ===")
        audio_file = input("File to Recover From (inc. extension): ")
        no_of_lsb_bits = str(input("LSB Bits: "))
        no_of_bytes = str(input("Number of Bytes: "))
        line_string = ("python wav-steg.py -r -s \"" + audio_file + "\" -o output\decoded_audio.txt" + " -n " + no_of_lsb_bits + " -b " + no_of_bytes)
        os.system(line_string)

    elif start_step == 4:
        print("Starting Program...\n")
        print("=== Hide Data in Frames ===")
        os.system("python Encoder.py")

    elif start_step == 5:
        print("Starting Program...\n")
        print("=== Recover Data in Frames ===")
        os.system("python Decoder.py")

    elif start_step == 6:
        print("Starting Program...\n")
        print("=== Steganograhpy Image Detection ===")
        os.system("python analysis.py")

    else:
        print("\nInvalid Input! Exiting...\n")
        quit()

except ValueError:
    print("Non-Integer Input Entered. Exiting...\n")
except KeyboardInterrupt:
	print("\nUser canceled, exiting...")
	quit()


