#################################
# Title: Lecture 6              #
# Lesson: Conductors/Capacitors #
# Filename: lecture_6.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 1/27/2014	#
# Last Editor: Joe Griffin	#
#################################

# This script is meant to define capacitor subclasses for nested spheres and
#   spheres at a distance much greater than their radii.
from group_6 import *
from math import log

class nested_sphere_cap(capacitor):
    def __init__(self, bigRad, smallRad, ref):
        self.bigRad = bigRad
        self.smallRad = smallRad
        coeff = 4 * pi * E0                                 # We'll lose access to coeff &
        geom = smallRad * bigRad / float(bigRad - smallRad) #   geom when init finishes
        self.capacitance = coeff * geom                     # We keep access to self
        self.ref = ref
        self.q = 0.0

    def charge(self, voltage):
        capacitor.charge(self, voltage)
        self.ref[self] = self.q

class nested_cyl_cap(capacitor):
    def __init__(self, bigRad, smallRad, length, ref):
        self.bigRad = bigRad
        self.smallRad = smallRad
        self.length = length
        self.ref = ref
        self.q = q
        numerator = 2 * pi * E0 * length
        denominator = log(bigRad / float(smallRad))
        self.capacitance = numerator / denominator

    def charge(self, voltage):
        capacitor.charge(self, voltage)
        self.ref[self] = self.q

class sep_sphere_cap(capacitor):
    def __init__(self, rad, sep, ref):
        self.rad = rad
        self.sep = sep
        self.capacitance = rad / (2 * 4 * pi * E0)
        self.ref = ref
        self.q = 0.0

    def charge(self, voltage):
        capacitor.charge(self, voltage)
        self.ref[self] = self.q
