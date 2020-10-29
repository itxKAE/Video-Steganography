# Credit: https://www.geeksforgeeks.org/image-based-steganography-using-python/
import re

from PIL import Image

# Global Variable
global frame_location

# Decode the data in the image
def decode(number):
    data = ''
    numbering = str(number)
    decoder_numbering = frame_location + "\\" + numbering + ".png"
    image = Image.open(decoder_numbering, 'r')
    imagedata = iter(image.getdata())
    while (True):
        pixels = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # string of binary data
        binstr = ''
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
        if re.match("[ -~]", chr(int(binstr,2))) is not None: # only decode printable data
            data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data

# Runtime
print("Please Enter Start and End Frame where Data is Hidden At")
frame_start = int(input("Start Frame: "))
frame_end = int(input("End Frame: "))
frame_location = input("Frames Location: ")
print("Extracting Data...")
decodedtextfile = open('output\decoded_frame.txt', 'a')
decodedtextfile.write('Decoded Text:\n')
for convnum in range(frame_start, frame_end + 1):
    try:
        decodedtextfile.write(decode(convnum))
        print("Data found in Frame %d" % convnum)
    except StopIteration:
        print("No data found in Frame %d" % convnum)
decodedtextfile.close()
print("\nExtraction Complete!")
