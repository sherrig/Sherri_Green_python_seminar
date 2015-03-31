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
	# We rather hoped you'd perform the integral with Python, instead of by hand. See the solution code when it's published.


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

    
    def charge(self, voltage1, voltage2): # If you're strictly adhering to the definition of series, you can't charge the
        self.cap1.q = self.cap1.capacitance * voltage1 # caps individually. The charge method should take only the 
        self.cap2.q = self.cap2.capacitance * voltage2 # voltage applied to the super-cap as an argument, not the sub-caps.

        if self.parallel == True:
            self.q = self.cap1.q + self.cap2.q  #charge on equivalent capacitor is sum of charges on both capacitors 
        else:
            self.q = self.cap1.q    #charge on equivalent capacitor is same as charge on either capacitor (series connected capacitors have same charge)
	# This last part is correct analytically, but, as stated above, we wanted you to charge the sub-caps with a net charge
	# on the super-cap, not the other way around. The solution code includes a neat trick in which it's possible to charge
	# trees of capacitors recursively. Imagine a super-cap with super-caps as its components. We'd like the charge method 
	# of the top-level cap to charge its sub-caps, and the sub-caps to charge their own sub-caps, all with only one call
	# to a charge method. To do that, we need to charge top-down, not bottom-up.
