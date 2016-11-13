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

u1Height, u1Weight, u1Skm, u1pbf = formatting.askInfo("Jesse")
filefunc.write_file(u1Height, u1Weight, u1Skm, u1pbf, "Jesse")

u2Height, u2Weight, u2Skm, u2pbf = formatting.askInfo("Charlie")
filefunc.write_file(u2Height, u2Weight, u2Skm, u2pbf, "Charlie")

u3Height, u3Weight, u3Skm, u3pbf = formatting.askInfo("Colin")
filefunc.write_file(u3Height, u3Weight, u3Skm, u3pbf, "Colin")

u4Height, u4Weight, u4Skm, u4pbf = formatting.askInfo("Brian")
filefunc.write_file(u4Height, u4Weight, u4Skm, u4pbf, "Brian")
