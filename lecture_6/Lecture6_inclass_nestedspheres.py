#Sherri Green
#Lecture 6 in class script
#3/10/15

#Define capacitor class for nested spheres

from math import pi
from const import E0
from group_6 import capacitor

k = 1 / (4 * pi * E0)

class nested_sphere_cap(capacitor):
    def __init__(self, inner_radius, outer_radius, ref):
        self.inner_radius = float(inner_radius)
        self.outer_radius = float(outer_radius)
        self.ref = ref
        self.capacitance = (outer_radius * inner_radius)/(k * (inner_radius - outer_radius))
        self.q = 0.0
