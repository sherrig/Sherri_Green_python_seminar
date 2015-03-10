#################################
# Title: Lecture 6 Group Script #
# Lesson: Conductors/Capacitors #
# Filename: group_6.py	        #
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/27/2014	#
# Last Editor: Joe Griffin	#
#################################

# This script is meant to define capacitor classes for a number of different capacitors so
#   they can be used to calculate total circuit capacitance.
from math import pi
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__(self, capacitance):
        self.capacitance = float(capacitance)               # This will be in Farads
        self.q = 0.0

    def charge(self, voltage):
        self.q = self.capacitance * voltage                 # This will be in Coulombs

class ll_plate_cap(capacitor):
    def __init__(self, area, sep):
        self.area = float(area)
        self.sep = float(sep)
        self.capacitance = E0 * area / sep
        self.q = 0.0
