'''
Presiones
'''
import math


# Convertir velocidades de km/h a m/s
def kmh_to_ms(kmh):
    return float(kmh) * 1000 / 3600

def bernoulli(p1, p0, v1):
    return math.sqrt((2 * (float(p1) - float(p0) + 1 / 2 * rho * v1**2)) / (rho))

# Definir constantes
rho = 0.125  # Densidad del aire en kgf*s^2/m^4

# Pedir al usuario los datos necesarios
P0 = input("Presión en el punto 0 (kgf/m^2): ")
if not P0:
    P0 = 10330
P1 = input("Presión en el punto 1 (kgf/m^2): ")
P2 = float(input("Presión en el punto 2 (kgf/m^2): "))
v1 = float(input("V1 en (km/h): "))
v1 = kmh_to_ms(v1)
# Calcular v para el punto 0 usando la ecuación de Bernoulli
v0 = bernoulli(P1, P0, v1)
# Calcular v para el punto 0 usando la ecuación de Bernoulli
v2 = bernoulli(P1, P2, v1)

# Imprimir los resultados
print("La velocidad en el punto 0 es: ", v0, " m/s")
print("La velocidad en el punto 2 es: ", v2, " m/s")
