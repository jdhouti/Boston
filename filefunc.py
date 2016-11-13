# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/12/2016
# This script just takes the input from the user and converts it.

from os.path import exists

def create_file():                                   #Creates the file.
    target = open("DATA.txt", "w")
    target.write("# Please do not edit anything this file!\n")
    target.write("# height weight skm pbf")

def write_file(a, b, c, d):
    if exists("DATA.txt"):
        with open("DATA.txt", "a") as myfile:         #temporarily renames file to myfile
            string = "\n%s %s %s %s" % (a, b, c, d)
            myfile.write(string)                      #adds the given numbers to the file

def file_exists():
    if exists("DATA.txt"):                            #Checks if the file exists
        return True

    else:
        return False
