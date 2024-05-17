'''
Bernoulli
'''
# Convertir velocidades de km/h a m/s
def kmh_to_ms(kmh):
    return float(kmh) * 1000 / 3600
    
# Definir constantes
rho = 0.125  # Densidad del aire en kgf * s^2/m^4
P0 = 10330  # Presión atmosférica a nivel del mar en kg/m^2

# Pedir al usuario las velocidades en km/h
v0_kmh = input("Velocidad del perfil alar (km/h): ")
v_ext_kmh = input("Velocidad en el extradós (km/h): ")
v_int_kmh = input("Velocidad en el intradós (km/h): ")

# Convertir velocidades de km/h a m/s
v0 = float(v0_kmh) * 1000 / 3600
v_ext = float(v_ext_kmh) * 1000 / 3600
v_int = float(v_int_kmh) * 1000 / 3600

# Calcular presiones en el extradós y el intradós usando Bernoulli
P_ext = P0 + 0.5 * rho * (v0**2 - v_ext**2)
P_int = P0 + 0.5 * rho * (v0**2 - v_int**2)

# Imprimir los resultados
print("Presión en el extradós: ", round(P_ext, 2), " kg/m^2")
print("Presión en el intradós: ", round(P_int, 2), " kg/m^2")
