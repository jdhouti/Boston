# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/12/2016
# This script just takes the input from the user and converts it.

from os.path import exists
import datetime as dt
import ast

def create_file(myDictionary):
    filename = myDictionary['name'] + "DATA.txt" # Creates the file.
    target = open(filename, "w")
    target.write("# Please do not edit anything this file!\n")
    target.write("# height weight skm pbf\n")

def write_file(myDictionary):                    # this creates the file
    filename = myDictionary['name'] + "DATA.txt"

    while True:
        if exists(filename):
            with open(filename, "a") as myfile:  # temporarily renames file to myfile
                myfile.write("\n" + str(myDictionary))          # adds the given numbers to the file
            break
        else:
            create_file(myDictionary)
            continue

def line_count(fname):                           # counts the amount of lines in file
    with open(fname) as filename:                # temporarily renames the given file to filename.
        for c, i in enumerate(filename):         # enumerate will go through every line and add 1 to c starting at 0
            pass                                 # since c is updated regardless, nothing needs to happen here.

    return c + 1                                 # adds one to C because count starts @ 0.

def get_pbf_average(name):
    fname = name + "DATA.txt"
    lineCount = line_count(fname)
    i, total = 2, 0                              # starts the average at 0. i starts at 2 to skip the first two info lines

    with open(fname, 'r') as f:
        lines = f.readlines()                    # creates a list. Each element in this list is a line from the .txt file.

        while i < lineCount:                     # iterates until it has reached the last line in the file
            total += ast.literal_eval(lines[i])['pbf']          # since lines is a list, line 3 is indicated as lines[2].
            i += 1                               # i increments by one so it can go to the next line.

    return total / (lineCount - 2)               # computes the average and returns it.

# the kind must be a 'string'
def get_a_list(name, kind):                      # beg -> the beginning of the wanted string. end -> the end
    nlist, i = [], 3                             # i here is used iterate through the lines in the .txt files
    fname = name + "DATA.txt"
    lineCount = line_count(fname)                # line_count counts the amount of lines in a .txt file.

    with open(fname, 'r') as f:
        lines = f.readlines()                    # the readlines() method returns a list.

        while i < lineCount:
            nlist.append(ast.literal_eval(lines[i])[kind])      # the i represents the line, beg -> beginning part of the line, end -> the end
            i += 1                               # increments the number of lines so the method can go to the next line everytime.

    return nlist

def get_pbf_list(name):                          # uses the get_a_list method to get a list of the last numbers of each line.
    return get_a_list(name, 'pbf')

def get_date_list(name):
    return get_a_list(name, 'date')
