# This file is a list of constants for convenient use in calculation.
# The first line of each comment identifies the constant.
# The values listed here are for SI, and units are noted.

# Local gravitational constant
# g = 9.8 m*s^-2
g = 9.8

# Universal gravitational constant
# G = 6.67384e-11 m^3*kg^-1*s^-2
G = 6.67384e-11

# Electron charge
# q = 1.60217657e-19 C
q = 1.60217657e-19

# Electron mass
# me = 9.10938291e-31 kg
me = 9.10938291e-31

# Proton mass
# mp = 1.67262178e-27 kg
mp = 1.672621777e-27

# Permittivity of free space
# E0 = 8.85418782e-12 F*m^-1
E0 = 8.854187817e-12

# Magnetic constant
# mu0 = 1.2566370614359173e-06 N*A^-2
mu0 = 1.2566370614359173e-06

# Light Speed
# c = 2.99792458e+8 m*s^-1
c = 2.99792458e+8

# Avogadro's Number
# mol = 6.0221413e+23
mol = 6.0221413e+23

# Planck's constant
# h = 6.62606957e-34 J*s
h = 6.62606957e-34

# Boltzmann constant
# kB = 1.3806488e-23 J*K^-1
kB = 1.3806488e-23

# Silicon Permitivity
# Es = 11.68 * E0
Es = 11.68 * E0

# Oxide Permittivity
# Eox = 3.9*E0
Eox = 3.9*E0

# Thermal Voltage at 300K
# Vth = kB*T/q
Vth = kB*300/q

# Define parallel for n args
def ll(*args):
    inverse = 0
    for i in args:
        inverse += 1.0/i
    return 1.0/inverse
