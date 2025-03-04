import math
'''
1-3
A spacecraft's dry mass is 75,000 kg and the effective exhaust gas velocity
of its main engine is 3,100 m/s.  How much propellant must be carried if the
propulsion system is to produce a total v of 700 m/s?
'''
Mf = 75000 # dry mass
Ve = 3100 #  exhaust velocity
dV = 700 #  desired velocity

Mo = Mf * math.exp(dV / Ve)
print("Mo ", round(Mo, 2), "kg")
Mp = Mo - Mf
print("Mp ", round(Mp, 2), "kg")
