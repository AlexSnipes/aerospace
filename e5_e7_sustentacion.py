import math

# Definir constantes
#rho = 0.125  # Densidad del aire en kgf*s^2/m^4
#v = 0.6 * 340  # Velocidad del avión en m/s (M0.6)
#c = 2.10  # Cuerda del ala en m
#b = 25.70  # Envergadura del ala en m
#S = b * c  # Área alar en m^2
#CL = 1.2  # Coeficiente de sustentación típico

velocidad_sonido = 340  # Velocidad del sonido en m/s (constante)
angulo_cl = [(0, 0), (1, 0.5), (2, 0.8), (3, 1.05), (4, 1.2), (5, 1.23),
             (6, 1.25), (7, 1.23), (8, 1.2), (9, 1.15), (10, 1.1), (12, 1),
             (14, 0.9), (16, 0.8), (19, 0.5)]


# Convertir velocidades de km/h a m/s
def kmh_to_ms(kmh):
    return float(kmh) * 1000 / 3600


# Obtener CL basado en el ángulo de ataque
def obtener_CL(angulo):
    for i in range(len(angulo_cl)):
        if angulo_cl[i][0] == angulo:
            return angulo_cl[i][1]
        elif angulo_cl[i][0] > angulo:
            x0, y0 = angulo_cl[i - 1]
            x1, y1 = angulo_cl[i]
            return y0 + (y1 - y0) * ((angulo - x0) / (x1 - x0))
    return angulo_cl[-1][1]


# Pedir al usuario los datos necesarios
rho = input("Densidad del aire: ")  # Densidad del aire en kgf*s^2/m^4
if not rho:
    rho = 0.125
else:
    rho = float(rho)

# El usuario debe ingresar el CL o el ángulo de ataque
S = input("Superficie alar (m^2): ")  # Superficie alar
if not S:
    c = float(input("Cuerda del ala en m: "))
    b = float(input("Envergadura del ala en m: "))
    S = b * c  # Área alar en m^2
S = float(S)

# El usuario debe ingresar el CL o el ángulo de ataque
CL = input("Coeficiente de sustentación (CL): ")  # Coeficiente de sustentación
if not CL:
    angulo_ataque = input("Ángulo de ataque °: ")  # Ángulo de ataque
    if angulo_ataque:
        CL = round(obtener_CL(float(angulo_ataque)), 2)
CL = float(CL)

# El usuario debe ingresar la velocidad del avión o el número de mach
v = input("Velocidad del avión (m/s): ")
if not v:
    M = input("Número de Mach: ")  # Número de Mach
    if not M:
        print("Velocidad o Mach requerido")
        exit()
    v = float(M) * velocidad_sonido  # Velocidad del avión en m/s

# Calcular la sustentación
L = 0.5 * rho * float(v)**2 * S * CL

# Mostrar el resultado y los valores utilizados
print("L: 1/2 * rho *v^2 * S *CL")
print("L: 1/2 *", S, "m^2 *", rho, "kgf*s^2/m^4 *", v, "m/s^2 *", CL)
print("L: ", L, "kgf")
