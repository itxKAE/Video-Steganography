# Credit: https://www.geeksforgeeks.org/image-based-steganography-using-python/

import math

from PIL import Image
 
# Convert encoding data into 8-bit binary ASCII
def generateData(data):
    newdata = []
    for i in data: # list of binary codes of given data
        newdata.append(format(ord(i), '08b'))
    return newdata
 
# Pixels modified according to encoding data in generateData
def modifyPixel(pixel, data):
    datalist = generateData(data)
    lengthofdata = len(datalist)
    imagedata = iter(pixel)
    for i in range(lengthofdata):
        # Extracts 3 pixels at a time
        pixel = [value for value in imagedata.__next__()[:3] + imagedata.__next__()[:3] + imagedata.__next__()[:3]]
        # Pixel value should be made odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pixel[j]% 2 != 0):
                pixel[j] -= 1
            elif (datalist[i][j] == '1' and pixel[j] % 2 == 0):
                if(pixel[j] != 0):
                    pixel[j] -= 1
                else:
                    pixel[j] += 1
        # Eighth pixel of every set tells whether to stop ot read further. 0 means keep reading; 1 means thec message is over.
        if (i == lengthofdata - 1):
            if (pixel[-1] % 2 == 0):
                if(pixel[-1] != 0):
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
        else:
            if (pixel[-1] % 2 != 0):
                pixel[-1] -= 1
        pixel = tuple(pixel)
        yield pixel[0:3]
        yield pixel[3:6]
        yield pixel[6:9]
 
def encoder(newimage, data):
    w = newimage.size[0]
    (x, y) = (0, 0)
 
    for pixel in modifyPixel(newimage.getdata(), data):
 
        # Putting modified pixels in the new image
        newimage.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
 
# Improved Encoding Function
# Instead of performing Steganography on all the frames, the function will now instead perform Steganography on selected range of frames
def encode(start, end, filename, frame_loc):
    total_frame = end - start + 1
    try:
        with open(filename) as fileinput: # Store Data to be Encoded
            filedata = fileinput.read()
    except FileNotFoundError:
        print("\nFile to hide not found! Exiting...")
        quit()
    datapoints = math.ceil(len(filedata) / total_frame) # Data Distribution per Frame
    counter = start
    print("Performing Steganography...")
    for convnum in range(0, len(filedata), datapoints):
        numbering = frame_loc + "\\" + str(counter) + ".png"
        encodetext = filedata[convnum:convnum+datapoints] # Copy Distributed Data into Variable
        try:
            image = Image.open(numbering, 'r') # Parameter has to be r, otherwise ValueError will occur (https://pillow.readthedocs.io/en/stable/reference/Image.html)
        except FileNotFoundError:
            print("\n%d.png not found! Exiting..." % counter)
            quit()
        newimage = image.copy() # New Variable to Store Hiddend Data
        encoder(newimage, encodetext) # Steganography
        new_img_name = numbering # Frame Number
        newimage.save(new_img_name, str(new_img_name.split(".")[1].upper())) # Save as New Frame
        counter += 1
    print("Complete!\n")

# Runtime
while True:
    try:
        print("Please Enter Start and End Frame where Data will be Hidden At")
        frame_start = int(input("Start Frame: "))
        frame_end = int(input("End Frame: "))
        if frame_start < frame_end:
            break
        else:
            print("\nStarting Frame must be larger than ending Frame! Please try again...")
    except ValueError:
        print("\nInteger expected! Please try again...")
frame_location = input("Frames Location: ")
filename = input("File to Hide (inc. extension): ")
encode(frame_start, frame_end, filename, frame_location)