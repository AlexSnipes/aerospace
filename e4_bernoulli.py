import math

# Definir constantes
rho = 0.125  # Densidad del aire en kgf*s^2/m^4
P_s = 1.01325 * 10000  # Presión estática a nivel del mar en kgf/m^2

# Pedir al usuario la presión total
P_t_kgf_cm2 = float(input("Presión total (kgf/cm^2): "))

# Convertir presión total de kgf/cm^2 a kgf/m^2
P_t = P_t_kgf_cm2 * 10000

# Calcular la velocidad usando la ecuación del tubo pitot
v = math.sqrt(2 * (P_t - P_s) / rho)

# Imprimir el resultado
print("La velocidad del avión es: ", v, " m/s")
