##Sherri Green
##Homework 4
#Blanket and ball of charge calculate flux and force
#3/1/15

from math import sqrt, pi, cos, sin
from const import E0
k = 1.0 / (4 * pi * E0)

blanket = [(-1,-1,1), (1,-1,1), (-1,1,1), (1,1,1)] #Endpoints of blanket

blanketx = blanket[1][0] - blanket[0][0] #length of blanket in x direction
blankety = blanket[3][0] - blanket[2][0] #length of blanket in y direction

dx = 1.0e-3
dy = 1.0e-3

dflux_list = []
dforcex_list = []
dforcey_list = []
dforcez_list = []

for j in xrange (int(blankety/dy)):
    for i in xrange (int(blanketx/dx)):
        posx = blanket[0][0] + i*dx
        posy = blanket [0][1] + j*dy
        dflux = dx*dy*(1/((posx**2 + posy**2 + 1)**(1.5)))    #flux = Integral of E dot dA. Only care about k direction of E-field, which is kqz/(x^2+y^2+z^2)^(3/2) where z = 1
        dflux_list.append (dflux)

        dforcex = dx*dy*((posx)/((posx**2 + posy**2 + 1)**(1.5)))  #force in x = (k*q*sigma*x)/(x^2+y^2+z^2)^(3/2) i hat
        dforcex_list.append (dforcex)
        dforcey = dx*dy*((posy)/((posx**2 + posy**2 + 1)**(1.5)))  #force in y = (k*q*sigma*y)/(x^2+y^2+z^2)^(3/2) j hat
        dforcey_list.append (dforcey) 
        dforcez = dflux                                             # force in z =  (k*q*sigma*z)/(x^2+y^2+z^2)^(3/2) k hat, where z = 1, so since I'm taking out the constants until the end, this gives the same value as the dflux
        dforcez_list.append (dforcez)

flux = sum(dflux_list)*k*10.0e-6   #Multiply by kq -- took constants out of integral

forcex = sum(dforcex_list)*k*10.0e-6*10.0e-3
forcey = sum(dforcey_list)*k*10.0e-6*10.0e-3
forcez = sum(dforcez_list)*k*10.0e-6*10.0e-3

vectorforce = [forcex, forcey, forcez]

print "Flux =", flux, "Nm^2/C"
print "Force =", vectorforce, "N"


# if mass of blanket is is not ridiculously heavy, then yes, the blanket will not fall -- the force in the z direction seems extremely large, but 10^-3 C is a lot of charge, so maybe it's reasonable.



