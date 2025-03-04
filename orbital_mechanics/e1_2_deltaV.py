import math
'''
1-2
The spacecraft in problem 1.1 has an initial mass of 30,000 kg.  What is the
change in velocity if the spacecraft burns its engine for one minute?
V = Ve × LN[ M / (M - qt) ]

'''
M = 30000
q = 30 #  engine ejects mass
Ve = 3100 #  exhaust velocity
Pe = 5  #  pressure at the nozzle exit
Ae = 0.7 #  exit area
Pa = 0 
t = 60
qt = q * t
Pe = 5*1000 #N
dV = Ve * math.log(M/(M-qt)) 
print("dV", round(dV, 3), "m/s")
