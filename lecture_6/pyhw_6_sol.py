#################################
# Title: Py Homework 6 Solution #
# Lesson: Capacitors            #
# Filename: pyhw_6_sol.py	#
# Original Author: Joe Griffin	#
# Most Recent Edit: 2/5/2015	#
# Last Editor: Joe Griffin     	#
#################################

# We will create a "super-capacitor" class that will connect capacitors in a circuit and
#   calculate the capacitance arbitrarily.

import numpy as np
from lecture_6 import *

class asymmetric_cap(capacitor):
    def __init__(self, s, l, sRad, cRad, ref):              # Assume the sphere is halfway
        self.sep = float(s)                                 #   along the cylinder axis
        self.length = float(l)
        self.sRad = float(sRad)
        self.cRad = float(cRad)
        self.ref = ref
        self.q = 0.0                                        # Integrate electric field from
##        testV = 0.0                                         #   one conductor to another for
##        dx = 1e-3                                           #   capacitance on initialization
##        testQ = 1.0
##        numIters = int((s - sRad - cRad) / dx) + 1
##        for i in xrange(numIters):
##            x = (dx * i) + sRad
##            sphereE = k * testQ / (x**2)
##            cylE = testQ / (2 * pi * (s - x) * l * E0)
##            testV += (sphereE + cylE) * dx
##        self.capacitance = testQ / testV
        testQ = 1.0
        dx = 1e-5
        numIters = int((s - sRad - cRad) / dx) + 1
        x = (dx * np.arange(numIters)) + sRad
        sphereE = k * testQ / np.square(x)
        cylE = testQ / (2 * pi * (s - x) * l * E0)
        testV = dx * sum(sphereE + cylE)
        self.capacitance = testQ / testV

class super_cap(capacitor):
    def __init__(self, cap1, cap2, parallel):
        self.parallel = parallel
        self.cap1 = cap1
        self.cap2 = cap2
        cap1.charge(0.0)
        cap2.charge(0.0)
        self.q = 0.0
        c1 = cap1.capacitance
        c2 = cap2.capacitance
        if parallel:
            self.capacitance = c1 + c2
        else:
            inverse = (1.0 / c1) + (1.0 / c2)
            self.capacitance = 1.0 / inverse

    def charge(self, voltage):
        self.q = self.capacitance * voltage
        if self.parallel:
             self.cap1.charge(voltage)
             self.cap2.charge(voltage)
        else:
             c1 = self.cap1.capacitance
             c2 = self.cap2.capacitance
             self.cap1.charge(self.q / c1)
             self.cap2.charge(self.q / c2)
