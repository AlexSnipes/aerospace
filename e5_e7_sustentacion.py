import math
'''
Calculo de sustentación y resistencia 2024.06.08
Ingenería Aeroespacial
Conocimientos Aeroespaciales I
'''

velocidad_sonido = 340  # Velocidad del sonido en m/s (constante)
angulo_cl = [(0, 0), (1, 0.5), (2, 0.8), (3, 1.05), (4, 1.2), (5, 1.23),
             (6, 1.25), (7, 1.23), (8, 1.2), (9, 1.15), (10, 1.1), (12, 1),
             (14, 0.9), (16, 0.8), (19, 0.5)]

angulo_cd = [(0, 0.2), (4, 0.04), (9, 0.065), (10, 0.075), (12, 0.1),
             (14, 0.13), (15, 0.15), (16, 0.17), (17, 0.195)]


# Convertir velocidades de km/h a m/s
def kmh_to_ms(kmh):
    return float(kmh) * 1000 / 3600


# Obtener CL basado en el ángulo de ataque
def obtener_coeficiente(datos, angulo):
    for i in range(len(datos)):
        if datos[i][0] == angulo:
            return datos[i][1]
        elif datos[i][0] > angulo:
            x0, y0 = datos[i - 1]
            x1, y1 = datos[i]
            return y0 + (y1 - y0) * ((angulo - x0) / (x1 - x0))
    return datos[-1][1]


# Pedir al usuario los datos necesarios
rho = input("Densidad: ")  # Densidad del aire en kgf*s^2/m^4
if not rho or rho == "0":
    rho = 0.125
else:
    rho = float(rho)

# El usuario debe ingresar el CL o el ángulo de ataque
S = input("Superficie (m^2): ")  # Superficie alar
if not S:
    cr = float(input("Cuerda del ala (m): "))
    b = float(input("Envergadura (m): "))
    ahusamiento = input("Ahusamiento: ")
    S = b * cr
    if ahusamiento:
        #Sw = Cp * b + 2 *(C ́ *b/2)
        ahusamiento = float(ahusamiento)
        cp = ahusamiento * cr
        S = S * ((1 + ahusamiento) / 2)
S = float(S)
angulo_ataque = ""
# El usuario debe ingresar el CL o el ángulo de ataque
CL = input("CL: ")  # Coeficiente de sustentación
if not CL:
    angulo_ataque = input("Angulo Ataque: ")  # Ángulo de ataque
    if angulo_ataque:
        CL = round(obtener_coeficiente(angulo_cl, float(angulo_ataque)), 3)
if CL:
    CL = float(CL)

# El usuario debe ingresar el CL o el ángulo de ataque
CD = input("CD: ")  # Coeficiente de sustentación
if not CD and angulo_ataque:
    CD = round(obtener_coeficiente(angulo_cd, float(angulo_ataque)), 3)
if not CD:
    ci = float(input("Ci: Coe. Res. inducida: "))
    if not ci:
        print("No se puede calcular CD sin Ci")
        exit()

    cfo = float(input("Cfo: Coe. res. forma: "))
    if not ci:
        print("No se puede calcular CD sin Cfo")
        exit()

    cfr = float(input("Cfr Coe res. friccion: "))
    if not ci:
        print("No se puede calcular CD sin Cfr")
        exit()
    #CDt = Ci + Cfo + Cfr
    CD = ci + cfo + cfr
CD = float(CD)

# El usuario debe ingresar la velocidad del avión o el número de mach
v = input("Vel. avion (m/s): ")
if not v:
    M = input("Numero Mach: ")  # Número de Mach
    if not M:
        print("Velocidad o Mach requerido")
        exit()
    v = float(M) * velocidad_sonido  # Velocidad del avión en m/s

# Calcular la sustentación
if CL:
    L = 0.5 * rho * float(v)**2 * S * CL
    print("L: 1/2 * rho *v^2 * S *CL")
    print("L: 1/2 *", S, "m^2 *", rho, "kgf*s^2/m^4 *", v, "m/s^2 *", CL)
    print("L: ", L, "kgf")

# Calcular la resistencia
D = 0.5 * rho * float(v)**2 * S * CD
print("D: 1/2 * rho *v^2 * S * CD")
print("D: 1/2 *", S, "m^2 *", rho, "kgf*s^2/m^4 *", v, "m/s^2 *", CD)
print("D: ", D, "kgf")
