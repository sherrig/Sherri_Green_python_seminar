#Find E-field at point Q from location L
#Sherri Green
#2/21/15



from math import sqrt, pi
e0 = 8.854187817*10**-12 # If you installed the const module from class, try: from const import E0
k = 1.0 / (4.0*pi*e0)

#Create Point and Location Tuples

def f(Q,L):
   
    E = [None, None, None] #E-field at L from Q in J
    magr = sqrt ((Q[0]-L[0])**2 + (Q[1]-L[1])**2 + (Q[2]-L[2])**2) #magnitude of r vector between measured location and point charge

    E[0] = k * (Q[3]/magr**3)*(L[0]-Q[0]) # You can also initialize E to be empty and `append` elements to it
    E[1] = k * (Q[3]/magr**3)*(L[1]-Q[1]) # E = []
    E[2] = k * (Q[3]/magr**3)*(L[2]-Q[2]) # E.append(k * (Q[3]/magr**3)*(L[2]-Q[2]))

    magE = sqrt (E[0]**2 + E[1]**2 + E[2]**2)

    print "E = ", E[0], "i N/C ", E[1], "j N/C ", E[2], "k N/C" # I'm a fan of the hat notation.




Q = (0,-.5,0,-1/k)        # (x,y,z,q) in (m, m, m, C) # Ha! Clever normalizer trick.
L = (0,0,-0.5)            # (x,y,z) in m

f(Q, L)

# Logical process looks good.
# Results are correct. Pass.
# Comments:
#           You used a print statement to show your calculated electric field. This means
#           that you won't be able to use your new function later to calculate electric
#           fields as part of a larger operation. I would recommend you return the electric
#           field list at the end of the function so you can use the result.
