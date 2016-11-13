# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/11/2016
# This script just takes the input from the user and converts it.

import filefunc
from sys import argv

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

def format_decimal(n):
	value = 10 - (len(str(n))) + 1

	return format(n, '.' + value + 'f')
