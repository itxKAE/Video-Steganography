# Contribution: Kae Chuan

import matplotlib.pyplot as plt
import numpy

from PIL import Image

# Global Variables
detection = 0 # Detection Flag
steg_frames = [] # To Store Frames with Steganography Present

# Image Steganography Detection Function
def analyse(file):
	block_size = 100
	img = Image.open(file)
	(width, height) = img.size # Get Image Resolution
	print(">> Frame Resolution: %d x %d Pixels" % (width, height))
	converted_data = img.convert("RGBA").getdata() # Obtain Red Green Blue Alpha Channel Information
	
	lsb_r = []	# Red Channel LSB Holder
	lsb_g = []	# Green Channel LSB Holder
	lsb_b = []	# Blue Channel LSB Holder
	for height_for in range(height):
		for width_for in range(width):
			(r, g, b, a) = converted_data.getpixel((width_for, height_for)) # Obtain Pixel Data from Each Channel
			lsb_r.append(r & 1)
			lsb_g.append(g & 1)
			lsb_b.append(b & 1)

	lsb_r_avg = [] # Average Red Channel LSB Holder
	lsb_g_avg = [] # Average Green Channel LSB Holder
	lsb_b_avg = [] # Average Blue Channel LSB Holder
	for i in range(0, len(lsb_r), block_size): # Calulating Averages
		lsb_r_avg.append(numpy.mean(lsb_r[i:i + block_size]))
		lsb_g_avg.append(numpy.mean(lsb_g[i:i + block_size]))
		lsb_b_avg.append(numpy.mean(lsb_b[i:i + block_size]))

	# <<<<< To be used for documentation >>>>>
	# numBlocks = len(lsb_r_avg)
	# blocks = [i for i in range(0, numBlocks)]
	# plt.axis([0, len(lsb_r_avg), 0, 1]) # Graph Creation
	# plt.ylabel("Average LSB Per Block")
	# plt.xlabel("Block Number")
	# plt.plot(blocks, lsb_r_avg, "ro") # Plot Values for Red
	# plt.plot(blocks, lsb_g_avg, "go") # Plot Values for Green
	# plt.plot(blocks, lsb_b_avg, "bo") # Plot Values for Blue
	# plt.show()

	global detection
	for i in range(0, 10): # To Check If LSB Steganography Exists (Will be further explained in documentation on why 0.5 was selected)
		if lsb_r_avg[i] == 0.5:
			detection = 1
		if lsb_g_avg[i] == 0.5:
			detection = 1
		if lsb_b_avg[i] == 0.5:
			detection = 1

	if detection == 1: # Output
		print(">> Steganography Detected!\n")
	else:
		print(">> No Steganography Detected!\n")

# Multi-Frame Iterations Function
def iterations(num_frames, file_type, file_location):
	global steg_frames, detection	
	current = 0 # Initial Frame
	while current != num_frames:
		print("\nAnalysing Frame %d..." % current)
		analyse(str(file_location) + "\\" + str(current) + "." + file_type)
		if detection == 1:
			steg_frames.append(current)
			detection = 0
		current += 1
	results()

# Final Output Function
def results():
	if not steg_frames:
		print(">> No Steganography Detected in the Frames Provided!")
	else:
		print(">> Steganography Detected in Frame:")
		print(">> " + str(steg_frames)[1:-1])

# Runtime
file_location = input("Directory of Frame(s): ")
num_frames = int(input("Number of Frame(s): "))
file_type = input("File Type: ")
iterations(num_frames, file_type, file_location)
