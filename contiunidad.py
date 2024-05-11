'''
Ecuación de continunidad para MicroPython
Resolución de ejercicios Unidad 2 Aerodinámica
Ing. Aeroespacial 
'''
import math


# Convertir diametro a radio
def diametro_a_radio(diametro):
    diametro = float(diametro)
    radio = diametro / 2 / 100  # Convertimos a metros
    print("CONV: diametro a radio en m", radio)
    return radio


# Convertir radio a diametro
def radio_a_diametro(radio):
    return radio * 2 * 100  # Convertimos a centímetros


def calcular_area_seccion_transversal(radio):
    return math.pi * radio**2


#Ecuación de continunidad
def calcular_area1(diametro_salida, v1, v2):
    radio = diametro_a_radio(diametro_salida)
    # Área de la sección transversal del tubo de entrada
    A2 = calcular_area_seccion_transversal(radio)
    return A2 * v2 / v1


#Ecuación de continunidad
def calcular_area2(diametro_entrada, v1, v2):
    radio_entrada = diametro_a_radio(diametro_entrada)
    # Área de la sección transversal del tubo de entrada
    A1 = calcular_area_seccion_transversal(radio_entrada)
    # Convertimos el radio del tubo de salida a diámetro (en centímetros)
    return A1 * v1 / v2

def comprobar_contuinidad(a1, a2, v1, v2):
    return a1 * v1 == a2 * v2


diametro_entrada = input("Diametro de entrada (cm): ")
if (diametro_entrada == ""):
    diametro_salida = input("Diametro de salida (cm): ")
    if (diametro_salida == ""):
        print("No se puede calcular el área de la sección transversal")
        exit()
    radio_salida = diametro_a_radio(diametro_salida)

v1 = input("Vel. entrada (m/s): ")
if (v1 != ""):
    v1 = float(v1)
v2 = input("Vel. salida (m/s): ")
if (v2 != ""):
    v2 = float(v2)

#if (diametro_entrada != 0 and v2 == ""):
    

if (diametro_entrada):
    A2 = calcular_area2(diametro_entrada, v1, v2)
    radio_salida = math.sqrt(A2 / math.pi)
    diametro_salida = radio_salida * 2 * 100  # Convertimos a centímetros
    print("Diámetro salida", round(diametro_salida, 2), "cm")
elif (diametro_salida != ""): 
    A1 = calcular_area1(diametro_salida, v1, v2)
    radio_entrada = math.sqrt(A1 / math.pi)
    diametro_entrada = radio_entrada * 2 * 100  # Convertimos a centímetros
    print("Diámetro entrada", round(diametro_entrada, 2), "cm")
