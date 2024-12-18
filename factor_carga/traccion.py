import math
'''
Resolución de ejercicios TP3 - Factor de Carga

v = 2024.10.29 18:21
Calcular la tracción necesaria de un avión que vuela a nivel del mar en condiciones de atmósfera estándar si el mismo realizo un vuelo en ascenso con una actitud de 14° y un ángulo de trayectoria de 2° con los siguientes datos:
V= 491 km/h; w=33 Tn; b=25m; e=0,94; CdFricción=0,0012; Cdforma= 0,0019; Cdi=0,0069
'''

def calcular_trepada(D, W, angulo):
  angulo_radian = angulo * 3.14159 / 180
  print("T=", D, "+", W, "* sin(", angulo, ")")
  return D + W * math.sin(angulo_radian)


def calcular_descenso(D, W, angulo):
  angulo_radian = angulo * 3.14159 / 180
  print("T=", D, "-", W, "* sin(", angulo, ")")
  return D - W * math.sin(angulo_radian)


def calcular_alargamiento(CL, e, cdi):
  print("A=", CL, "**2", "/", math.pi, "*", e, "*", cdi)
  return (CL**2) / (math.pi * e * cdi)


def calcular_cdi(CL, e, a):
  print("cdi =", CL, "**2 / (", 3.14, e, "*", a, ")")
  return (CL**2) / (math.pi * e * a)


def calcular_S(b, A):
  return b**2 / A


def calcular_CL(w, densidad, v, S):
  return (2 * w) / (densidad * v**2, S)


# Pedir al usuario los datos necesarios
rho = input("Densidad: ")  # Densidad del aire en kgf*s^2/m^4
if not rho or rho == "0":
  rho = 0.125
else:
  rho = float(rho)

# El usuario debe ingresar la velocidad del avión o el número de mach
#v = 163.89
v = input("Vel. avion (m/s): ")
if v:
  v = float(v)
  print("v", round(v, 3))
CL = input("CL: ")  # Coeficiente de sustentación
if CL:
  CL = float(CL)

CD = input("CD: ")  # Coeficiente de resistencia
if CD:
  CD = float(CD)
if not CD:
  cdi = input("Ci Res. inducida: ")
  #cdi = 0.0059
  if (cdi):
    cdi = float(cdi)
  Cdp = input("Cfo Res. forma: ")
  #Cdp = 0.0029
  if (Cdp):
    Cdp = float(Cdp)
  cfr = input("Cfr Res. friccion: ")
  # cfr = 0.001
  if (cfr):
    cfr = float(cfr)
  #Coeficiente de resistencia es igual a la suma de los coeficientes de resistencia (inducida, forma y fricción)
  if (cdi and Cdp and cfr):
    CD = cdi + Cdp + cfr
  elif (Cdp and cfr):
    Cdp = Cdp + cfr

print(CD, "CD")
b = input("Envergadura (b) (m): ")
if (b):
  b = float(b)
S = input("Superficie (S) (m^2): ")  # Superficie alar
if S:
  S = float(S)
if not S and CL and CD:
  e = input("Eficiencia: ")
  if e:
    e = float(e)
  A = input("Alargamiento (A): ")
  if (A):
    A = float(A)
  if not (A) and e and CD and cdi:
    A = calcular_alargamiento(CL, e, cdi)
if not A and b:
  A = input("Alargamiento (A): ")
  A = b**2 / S

print(round(A, 2), "A")
if A and b and not S:
  S = b**2 / A
#Si no se conoce el coeficiente de sustencia se puede calcular utilizando la carga alar (w)

w = input("Peso (tnf): ")  #Carga alar
if w:
  w = float(w) * 1000
  print("CL: (2 * ", w, ") / (", rho, " * ", v, "**2 * ", S, ")")
  if not CL and S and v:
    CL = (2 * w) / (S * rho * v**2)

angulo_ataque = input("Angulo Ataque: ")  # Ángulo de ataque
if angulo_ataque:
  angulo_ataque = float(angulo_ataque)
# Calcular la resistencia
if CD:
  D = 0.5 * rho * float(v)**2 * S * CD
  print("D: 1/2 * rho *v^2 * S * CD")
  print("D: 1/2 *", S, "m^2 *", rho, "kgf*s^2/m^4 *", round(v, 3), "m/s^2 *",
        round(CD, 4))
  print("D: ", round(D, 4), "kgf")

  T = calcular_trepada(D, w, angulo_ataque)
  print("T", T)
