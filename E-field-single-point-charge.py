#Find E-field at point Q from location L
#Sherri Green
#2/21/15



from math import sqrt, pi
e0 = 8.854187817*10**-12
k = 1.0 / (4.0*pi*e0)

#Create Point and Location Tuples

def f(Q,L):
   
    E = [None, None, None] #E-field at L from Q in J
    magr = sqrt ((Q[0]-L[0])**2 + (Q[1]-L[1])**2 + (Q[2]-L[2])**2) #magnitude of r vector between measured location and point charge

    E[0] = k * (Q[3]/magr**3)*(L[0]-Q[0])
    E[1] = k * (Q[3]/magr**3)*(L[1]-Q[1])
    E[2] = k * (Q[3]/magr**3)*(L[2]-Q[2])

    magE = sqrt (E[0]**2 + E[1]**2 + E[2]**2)

    print "E = ", E[0], "i N/C ", E[1], "j N/C ", E[2], "k N/C"

    

    
Q = (0,-.5,0,-1/k)        # (x,y,z,q) in (m, m, m, C)
L = (0,0,-0.5)            # (x,y,z) in m

f(Q, L)
