# Julien Dhouti
# Part of the Jesse Boston Project
# Started 11/11/2016
# This script builds the graph.

import matplotlib.pyplot as plt

def get_pbf_data():
    jesseData = get_pbf_list("Jesse")
    colinData = get_pbf_list("Colin")
    charlieData = get_pbf_list("Charlie")
    brianData = get_pbf_list("Brian")

    return jesseData, colinData, charlieData, brianData

def get_date():


def graph():
    x1, x2, x3, x4 = get_pbf_data()
