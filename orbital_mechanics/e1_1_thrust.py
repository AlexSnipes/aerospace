'''
1-1
A spacecraft's engine ejects mass at a rate of 30 kg/s with an exhaust velocity
of 3,100 m/s.  The pressure at the nozzle exit is 5 kPa and the exit area is
0.7 m2.  What is the thrust of the engine in a vacuum?
'''
q = 30 #  engine ejects mass
Ve = 3100 #  exhaust velocity
Pe = 5  #  pressure at the nozzle exit
Ae = 0.7 #  exit area
Pa = 0 

# F = q × Ve + (Pe - Pa) × Ae
Pe = 5*1000 #N
F = q * Ve + (Pe - Pa) * Ae #  thrust of the engine in a vacuum
print("F", F, "N")
