import math
'''
1-6

A rocket engine produces a thrust of 1,000 kN at sea level with a propellant
flow rate of 400 kg/s.  Calculate the specific impulse.


'''
g = 9.81
q = 400 #kg/s
F = 1000000 #N
isp = F/(q*g)
print("ISP", round(isp, 3), "s")
