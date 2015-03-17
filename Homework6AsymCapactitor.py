#Sherri Green
#3/16/15
#Homework 6

#Calculate the capacitance of conducting cylinder and conducting sphere

from math import pi, log
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__ (self, capacitance, ref):
        self.capacitance = float(capacitance)
        self.q = 0.0

    def charge (self, voltage):
        self.q = self.capacitance * voltage
        self.ref[self] = self.q

class asymm_capacitor(capacitor):
    def __init__ (self, rcyl, hcyl, rsph, sep, ref):    #name, radius of cylinder, height of cylinder, radius of sphere, distance between them, ref
        self.rcyl = float(rcyl)
        self.hcyl = float(hcyl)
        self.rsph = float(rsph)
        self.sep = float (sep)
        self.q = 0.0
        self.capacitance = abs(1/ ((k/(sep - rcyl)) - (k/rsph) - (log((sep-rsph)/rcyl))/(2*pi*hcyl*E0)))

    
class super_capacitor:
    def __init__ (self, cap1, cap2, parallel):      #parallel = true means parallel, false means series
        self.cap1 = cap1
        self.cap2 = cap2
        self.parallel = parallel
        if parallel == True:
            self.capacitance = cap1.capacitance + cap2.capacitance
        else:
            self.capacitance = ((cap1.capacitance * cap2.capacitance)/
                                 (cap1.capacitance + cap2.capacitance))

    
    def charge(self, voltage1, voltage2):
        self.cap1.q = self.cap1.capacitance * voltage1
        self.cap2.q = self.cap2.capacitance * voltage2

        if self.parallel == True:
            self.q = self.cap1.q + self.cap2.q  #charge on equivalent capacitor is sum of charges on both capacitors 
        else:
            self.q = self.cap1.q    #charge on equivalent capacitor is same as charge on either capacitor (series connected capacitors have same charge)
            
        
