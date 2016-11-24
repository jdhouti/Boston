# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/12/2016
# This is the main script. This is the script that should be executed to run
# the program.

import formatting
import filefunc

print "Enter the information for each user like the following..."
print "Information >> height, weight, skm, pbf"
print "Do not include units. Please include commas."

jesseDictInfo = formatting.askInfo("Jesse")
filefunc.write_file(jesseDictInfo)              # gives it a dictionary

charlieDictInfo = formatting.askInfo("Charlie")
filefunc.write_file(charlieDictInfo)

colinDictInfo = formatting.askInfo("Colin")
filefunc.write_file(colinDictInfo)

brianDictInfo = formatting.askInfo("Brian")
filefunc.write_file(brianDictInfo)
