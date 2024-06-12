import math
'''
@Author Alejandro Sánchez (github.com/AlexSnipes)
@Version 2024.06.12 13:00
Continuidad MicroPython
Ingeniería Aeroespacial
Conocimientos Aeroespaciales I
'''

densidad_fluido = ""
v1 = ""
p1 = ""
a1 = ""
a2 = ""
v2 = ""
p2 = ""

#Calcular contiunidad
def continuidad(a1, a2, v1, v2):
    if (a1 == ""):
        return a2 * v2 / v1
    if (a2 == ""):
        return a1 * v1 / v2
    if (v1 == ""):
        return a2 * v2 / a1
    if (v2 == ""):
        return a1 * v1 / a2


# Area de entrada
a1 = input("A1: ")
if (a1):
    a1 = float(a1)
# Velocidad de salida
a2 = input("A2: ")
if (a2):
    a2 = float(a2)
# Velocidad de entrada
v1 = input("V1 (m/s): ")
if (v1):
    v1 = float(v1)
# Velocidad de salida
v2 = input("V2 (m/s): ")
if (v2):
    v2 = float(v2)

if not a1:
    a1 = continuidad(a1, a2, v1, v2)
print ("A1 ", round(a1, 2), "")
if not a2:
    a2 = continuidad(a1, a2, v1, v2)
print ("A2 ", round(a2, 2), "")
if not v1:
    v1 = continuidad(a1, a2, v1, v2)
print ("V1 ", round(v1, 2), 2), "(m/s)")
if not v2:
    v2 = continuidad(a1, a2, v1, v2)
print ("V2 ", round(v2, 2), "(m/s)")
