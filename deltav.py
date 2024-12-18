import math
'''
v = 2024.11.02 12
Hallar AV ideal de un cohete si su impulso específico es igual a 300 segundos, la masa de la estructura es de 9150Tn, la carga útil es de 1100kg y la masa del propulsante es de 92tn. 
'''

g = 9.8
def calcular_deltav(isp, m0, mf):
  print("300*9.8*log(m0/mf)")
  print(isp, "*", "9.8", "* log(", m0, "/", mf, ")")
  return isp * g * math.log(m0/mf)

isp = input("ISP (s)")
if (isp):
  isp = float(isp)

mest = input("Dry mass (kg) ")
mprop = input("Masa prop (kg) ")
payload = input("Payload (kg) ")

deltav = calcular_deltav(isp, float(mest) + float(mprop) + float(payload), float(mest) + float(payload))
print("DeltaV", float(deltav))
