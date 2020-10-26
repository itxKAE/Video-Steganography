from PIL import Image
import re
# Decode the data in the image
def decode(number):
    data = ''
    numbering = str(number)
    decoder_numbering = numbering + ".png"
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
a_number = int(input("How many frames to decode?\n"))
decodedtextfile = open('decoded.txt', 'a')
decodedtextfile.write('Decoded Text:\n')
for convnum in range(a_number+1):
    decodedtextfile.write(decode(convnum))
decodedtextfile.close()
