# PIL to extract and modify image pixels
from PIL import Image
import math
 
# Convert encoding data into 8-bit binary ASCII
def generateData(data):
 
        # list of binary codes
        # of given data
        newdata = []
 
        for i in data:
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
        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pixel[j]% 2 != 0):
                pixel[j] -= 1
            elif (datalist[i][j] == '1' and pixel[j] % 2 == 0):
                if(pixel[j] != 0):
                    pixel[j] -= 1
                else:
                    pixel[j] += 1
        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
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
 
# Encode data into image
def encode(number, filename):
#Recursively encode a textfile content into multiple frames, and content will be equally distributed among frames
    with open(filename) as fileinput: 
        filedata = fileinput.read() 
        #print(len(filedata))
        #print(int(len(filedata)))
    datapoints = math.ceil(len(filedata) / number)
    counter = -1
    for convnum in range(number+1):
    
        numbering = str(convnum)
        #zero_filled_number = numbering.zfill(5)#zerofill depending on image extraction
        #zero_filled_number += ".png"
        numbering += ".png"
        #print(zero_filled_number)
        encodetext = filedata[counter+1:(datapoints*(convnum+1))]
        #print(encodetext)
        counter +=datapoints 
        image = Image.open(numbering, 'r')
        newimage = image.copy()
        encoder(newimage, encodetext)
        new_img_name = "m" + numbering #zero_filled_number
        newimage.save(new_img_name, str(new_img_name.split(".")[1].upper()))

a_number = int(input("How many frames to encode?\n"))
filename = input("Enter the name of your document(including extension): ")
encode(a_number, filename)





 