# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/12/2016
# This script just takes the input from the user and converts it.

from os.path import exists

def create_file(name):
    filename = name + "DATA.txt"                  #Creates the file.
    target = open(filename, "w")
    target.write("# Please do not edit anything this file!\n")
    target.write("# height weight skm pbf\n")

def write_file(a, b, c, d, name):
    filename = name + "DATA.txt"

    while True:
        if exists(filename):
            with open(filename, "a") as myfile:           #temporarily renames file to myfile
                string = "%s %s %s %s\n" % (a, b, c, d)
                myfile.write(string)                      #adds the given numbers to the file

                break
        else:
            create_file(name)

            continue

def line_count(fname):                          # counts the amount of lines in file
    with open(fname) as filename:               # temporarily renames the given file to filename.
        for c, i in enumerate(filename):        # enumerate will go through every line and add 1 to c starting at 0
            pass                                # since c is updated regardless, nothing needs to happen here.

    return c + 1

def getAverage(name):
    fname = name + "DATA.txt"
    lineCount = line_count(fname)

    with open(fname, 'r') as f:
        i, avg = 2, 0
        lines = f.readlines()

        while i < lineCount:
            avg += float(lines[i][-11:-1])
            i += 1

    return avg / (lineCount - 2)
