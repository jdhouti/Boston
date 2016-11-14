# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/12/2016
# This script just takes the input from the user and converts it.

from os.path import exists
import datetime as dt

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
                time = dt.datetime.today().strftime("%m/%d/%Y")     # stores the time as a string
                string = time + ": %s %s %s %s\n" % (a, b, c, d)
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

def get_pbf_average(name):
    fname = name + "DATA.txt"
    lineCount = line_count(fname)
    i, avg = 2, 0                                # starts the average at 0. i starts at 2 to skip the first two info lines

    with open(fname, 'r') as f:
        lines = f.readlines()                    # creates a list. Each element in this list is a line from the .txt file.

        while i < lineCount:                     # iterates until it has reached the last line in the file
            avg += float(lines[i][-11:-1])       # since lines is a list, line 3 is indicated as lines[2].
            i += 1                               # i increments by one so it can go to the next line.

    return avg / (lineCount - 2)

def get_a_list(name, beg, end):
    nlist, i = [], 2
    fname = name + "DATA.txt"
    lineCount = line_count(fname)

    with open(fname, 'r') as f:
        lines = f.readlines()

        while i < lineCount:
            nlist.append(float(lines[i][beg:end]))
            i += 1

    return nlist

def get_pbf_list(name):
    return get_a_list(name, -12, -1)            # returns the final list of all of the numbers found in the document at the end
                                                # of each line.

def get_date_list(name):
    return get_a_list(name, 0, 4)
