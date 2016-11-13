# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/11/2016
# This script just takes the input from the user and converts it.

import os	# not yet needed
import filefunc
from sys import argv

#def cls():
#    os.system('cls' if os.name=='nt' else 'clear') # checks which os is running

#sscript, filename = argv

def formatInfo(string):
	listInfo = string.split(', ')
	height = float(listInfo[0])
	weight = float(listInfo[1])
	skm = float(listInfo[2])
	pbf = float(listInfo[3])

	return height, weight, skm, pbf

def calculatePDJ(skm, w, bdf):
	return ((skm / weight) * 100) - bdf

def askInfo(name):
	print "\nUser >> %s" % name
	while True:
		try:
			info = raw_input("Information >> ")
			height, weight, skm, pbf = formatInfo(info)
			break

		except:
			print "Input error!\n"
			continue

	return height, weight, skm, pbf

#clear()
print "Enter the information for each user like the following..."
print "Information >> height, weight, skm, pbf"
print "Do not include units. Please include commas."

u1Height, u1Weight, u1Skm, u1pbf = askInfo("Jesse")
#u2Height, u2Weight, u2Skm, u2pbf = askInfo("Charlie")
#u3Height, u3Weight, u3Skm, u3pbf = askInfo("Colin")
#u4Height, u4Weight, u4Skm, u4pbf = askInfo("Brian")

if filefunc.file_exists():
	filefunc.write_file(u1Height, u1Weight, u1Skm, u1pbf)

else:
	filefunc.create_file()
	filefunc.write_file(u1Height, u1Weight, u1Skm, u1pbf)
