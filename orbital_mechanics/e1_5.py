import math
'''
1-5
A rocket engine burning liquid oxygen and kerosene operates at a mixture ratio
of 2.26 and a combustion chamber pressure of 50 atmospheres.  If the nozzle is
expanded to operate at sea level, calculate the exhaust gas velocity relative
to the rocket.
where k is the specific heat ratio, R* is the universal gas constant (8,314.4621 J/kmol-K in SI units, or 49,720 ft-lb/(slug-mol)-oR in U.S. units), Tc is the combustion temperature, M is the average molecular weight of the exhaust gases, Pc is the combustion chamber pressure, and Pe is the pressure at the nozzle exit.
'''
k = 1.221
Pc = 50 # atm
M = 21.40 # kg/mol
Tc =3470 #k
Pe = 1 # atm
of = 2.26 # mixture ratio kg/mol
R = 8314.46 # J/mol-K

#     Ve = SQRT[ (2 × k / (k - 1)) × (R* × Tc / M) × (1 - (Pe / Pc)**(k-1)/k) ]
Ve = math.sqrt( (2 * k / (k - 1)) * (R * Tc / M) * (1 - (Pe / Pc) ** ((k - 1) / k)) )
print("Ve", round(Ve, 2), "m/s")
