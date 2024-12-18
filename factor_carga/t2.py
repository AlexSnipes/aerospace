import math
'''
Resolución de ejercicios TP3 - Factor de Carga
Ing. Aeroespacial 
v = 2024.11.04 00:44
Una Aeronave realiza una restablecida luego de picada a nivel del mar. Se pide determinar la V de vuelo para esa maniobra. Indique si la maniobra puede ser realiza con éxito a la V vuelo que tiene el avión.
Datos n= 2,5; W: 1630 KG; Sw: 16,20 m**2; Clmax: 1,40; R=250m
'''
# # Datos del avión
g=9.81
r = input("r (m) ")
if (r):
  r = float(r)

w = input("Peso (kg) ")
if (w):
  w = float(w)

n = input("FC (n) ")
if (n):
  n = float(n)

s = input("Superficie (s) ")
if (s):
  s = float(s)

cl = input("Clmax ")
if (cl):
  cl= float(cl)
#Calcular N
def calcular_velocidad_restablecida_luego_picada(n, g, r):
  print("1+((v**2)/(g*r))")
  #print("1+((",v,"**2)/(g*",r,"))")
  return math.sqrt((n-1) * (g * r))


#Calcular Trepada
def calcular_velocidad_restablecida_luego_trepada(n, g, r):
  print("1-((v**2)/(g*r))")
  #print("1-((",v,"**2)/(g*",r,")")
  return math.sqrt((n+1) * (g * r))


#Calcular viraje
def calcular_viraje(w, angulo):
  print("L=w/cos(angulo)")
  angulo_radian = angulo * 3.14159 / 180
  L = w / math.cos(angulo_radian)
  return L / w


#Calcular aterrizaje
def calcular_aterrizaje(rd, g, i):
  print("(r/d)**2 / (2*g*i)")
  return (rd**2) / (2 * g * i)

def calcular_velocidad_peridad(s, w, cl):
  return math.sqrt(w / (0.5 * 0.125 * s * cl))

#Factor de carga en restablecida luego de picada:
print("Picada")
n1 = calcular_velocidad_restablecida_luego_picada(n, g, r)
print("vp: ", round(n1, 2), "m/s")
#Factor de carga en Restablecida luego de trepada:
print("Trepada")
n4 = calcular_velocidad_restablecida_luego_trepada(n, g, r)
print("vt", round(n4, 2), "m/s")
print("VS")
vs = calcular_velocidad_peridad(s, w, cl)
print("Vs ", vs, "m/s")
print ("VM", math.sqrt(n) * vs, "m/s")
