# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/11/2016
# This script just takes the input from the user and converts it.

import filefunc
from sys import argv
import time

def formatInfo(string):
	date = str(time.strftime("%H:%M:%S"))
	listInfo = string.split(', ')
	height = float(listInfo[0])
	weight = float(listInfo[1])
	skm = float(listInfo[2])
	pbf = float(listInfo[3])

	return date, height, weight, skm, pbf

def calculatePDJ(skm, w, bdf):
	return ((skm / weight) * 100) - bdf

def askInfo(name):
	print "\nUser >> %s" % name
	while True:
		try:
			info = raw_input("Information >> ")
			date, height, weight, skm, pbf = formatInfo(info)	# feeds info to formatInfo and assigns
			break												# all of the returns variables to those variables

		except:
			print "Input error!\n"
			continue

	return format_dictionary(date, name, height, weight, skm, pbf)		# makes a dictionary with all of that information

# not used atm
def format_decimal(n):
	n = str(float(n))
	i = len(n)

	while i <= 10:
		n = n + '0'
		i += 1

	return n

def format_dictionary(date, name, a, b, c, d):
	dictInfo = {'date': date,'name': name, 'height': a, 'weight': b, 'skm': c, 'pbf': d}

	return dictInfo
