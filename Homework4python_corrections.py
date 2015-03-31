##Sherri Green
##Homework 4
#Blanket and ball of charge calculate flux and force
#3/1/15


###         GOOD JOB!!!!!!
###         SEE NOTES


from math import sqrt, pi, cos, sin
from const import E0
k = 1.0 / (4 * pi * E0)
q = 1e-6                #Note 2: define constants to make the program easier to follow 
sigma = 1e-3            #Note 3:  1e-3 =0.001 and 10.e-3 = 0.01 BE CAREFUL!!

print sigma, 10.0e-3
blanket = [(-1,-1,1), (1,-1,1), (-1,1,1), (1,1,1)] #Endpoints of blanket

blanketx = blanket[1][0] - blanket[0][0] #length of blanket in x direction
blankety = blanket[3][0] - blanket[2][0] #length of blanket in y direction


print "k", k, "Q/6E0", q/(6*E0)

dx = 1.0e-3
dy = 1.0e-3

dflux_list = []
dforcex_list = []
dforcey_list = []
dforcez_list = []
flux2 = 0.
for j in xrange (int(blankety/dy)+1):      #NOTE 1:add 1     
    for i in xrange (int(blanketx/dx)+1):  #NOTE 1: add 1 
        posx = blanket[0][0] + i*dx
        posy = blanket [0][1] + j*dy
        dflux = dx*dy*(1/( ( posx**2 + posy**2 + 1 )**(1.5)) )    #flux = Integral of E dot dA. Only care about k direction of E-field, which is kqz/(x^2+y^2+z^2)^(3/2) where z = 1
        dflux_list.append (dflux)
		
        dforcex = dx*dy*((posx)/((posx**2 + posy**2 + 1)**(1.5)))  #force in x = (k*q*sigma*x)/(x^2+y^2+z^2)^(3/2) i hat
        dforcex_list.append (dforcex)
        dforcey = dx*dy*((posy)/((posx**2 + posy**2 + 1)**(1.5)))  #force in y = (k*q*sigma*y)/(x^2+y^2+z^2)^(3/2) j hat
        dforcey_list.append (dforcey) 
        dforcez = dflux                                             # force in z =  (k*q*sigma*z)/(x^2+y^2+z^2)^(3/2) k hat, where z = 1, so since I'm taking out the constants until the end, this gives the same value as the dflux
        dforcez_list.append (dforcez)



flux = sum(dflux_list)*k*q   #Multiply by kq -- took constants out of integral
                             # you had 10.0e-6 instead of q

forcex = sum(dforcex_list)* k * q* sigma     # You had: 10.0e-6*10.0e-3
forcey = sum(dforcey_list)* k * q* sigma
forcez = sum(dforcez_list)* k * q* sigma

vectorforce = [forcex, forcey, forcez]

print "Flux =", flux, "Nm^2/C"
print "Force =", vectorforce, "N"
print "flux2", flux2*k*q, flux2*k*q*6*E0

# if mass of blanket is is not ridiculously heavy, then yes, the blanket will not fall -- the force in the z direction seems extremely large, but 10^-3 C is a lot of charge, so maybe it's reasonable.

# NOTE 1: you need to add 1 so you have the end of the blanket included in the
#         calculation. If it is not included the x and y component of the force
#         is not zero. Due to the symmetry, we expect Fx=Fy=0

# Note 2: try to always define the constants to use in the expressions at
#         the beginning of the script. For two reasons: 
#          1st- it is a more readable script
#          2nd- if you want to change the value of the constant you change it only once!!!!!!
#         


# Note 3: because you will not be using the different lists that you have created
#         you could have obtained the same result by adding the values calculated in each time step
#         Example: flux = flux + k * q * dx*dy*(1/( ( posx**2 + posy**2 + 1 )**(1.5)) ) , etc