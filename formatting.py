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
	pbf = format_decimal(float(listInfo[3]))

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
	n = str(float(n))
	i = len(n)

	while i <= 10:
		n = n + '0'
		i += 1

	return n
