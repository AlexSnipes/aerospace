import math
#Calcular los valores de VA y VH de acuerdo a la norma FAR25
#A = 10
#b = 16
#clMax = 1.1
#clMin = -1.3
#W = 7200 #KG
S = ""
vh = ""
vs = ""
A = input("A (m2): ")
if A:
  A = float(A)
b = input("B (m2): ")
if b:
  b = float(b)
clMax = input("clMax: ")
if (clMax):
  clMax = float(clMax)
clMin = input("clMin: ")
if (clMin):
  clMin = float(clMin)
W = input("W (kg): ")
if W:
  W = float(W)
#rho = input("rho (kg*m2/s4): ")
#if not rho:
rho = 0.125
va = input("vA (m/s)")
if (va):
  va = float(va)

vs = input("vS (m/s)")
if (vs):
  vs = float(vs)

vc = input("vC (m/s)")
if (vc):
  vc = float(vc)

vd = input("vD (m/s)")
if (vd):
  vd = float(vd)

print("n = L/w")
print("n = 0.5 * vs**2 *ClMax * S / W")
print("va = math.sqrt(2 * n * W / (rho * ClMax * S))")
print("a = b**2/S")
print("S = b**2 / A")
if (A and b):
  S = b**2 / A
if not S:
  S = input("S (m2):")
  if (S):
    S = float(S)
print("\nS = ", S, "m**2")

print("\nFAR25")
print("n = 2.1 + (24000 / (W + 10000))")
nMax = input("nMax")
if (nMax):
  nMax = float(nMax)
if (not W and nMax):
  n = nMax - 2.1
  print("W = (13000/", n, ")")
  W = (13000 / n)
  print("W = (", W, "/2.2lbs)")
  W = round(W / 2.2, 3)
  print("W=", W, "kg")

if (not nMax):
  print("\nn = 2.1 + (24000 / (W + 10000))")
  nMax = 2.1 + (24000 / (W + 10000))
  print("n = ", round(nMax, 3))
  
if (not vs and clMax):
  print("\nvs = math.sqrt((2 * 1 * W) / (rho * clMax * S))")
  vs = math.sqrt((2 * 1 * W) / (rho * clMax * S))
  print("vs = ", round(vs, 3), "m/s")

if (not vh and clMin):
  print("\nvh = math.sqrt((2 * -1 * W) / (rho * clMin * S))")
  vh = math.sqrt((2 * -1 * W) / (rho * clMin * S))
  print("vh = ", round(vh, 3), "m/s")

if (not va and vs):
  print("\nva = math.sqrt(n) * vs")
  va = math.sqrt(nMax) * vs
  print("va = ", round(va, 3), "m/s")

if (not vs and va):
  print("va = math.sqrt(n) * vs")
  print("vs = va/math.sqrt(nMax)")
  vs = round(va/math.sqrt(nMax), 3)
  print("vs", round(vs, 3), "m/s")

clMax = (2 * W) / (rho * (vs**2) * S)
print("clMax = (2 * W) / (rho * vs**2 * S)")
print("clMax = (2 *", W,") / (",rho," * ",round(vs, 3),"**2 *", S,")")
print("\nclMax: ", round(clMax, 3))
