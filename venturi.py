'''
Tube de Venturi
'''
import math

def calculate_velocity():
    # Pedir al usuario los datos
    r1_input = input("Radio de la sección de entrada (cm): ")
    A2_input = input("Área de la sección de salida (cm²): ")
    v1_input = input("Velocidad en la sección de entrada (m/s): ")
    v2_input = input("Velocidad en la sección de salida (m/s): ")

    # Convertir las entradas a valores numéricos si se proporcionaron
    r1 = float(r1_input) / 100 if r1_input else None
    A2 = float(A2_input) / 10000 if A2_input else None
    v1 = float(v1_input) if v1_input else None
    v2 = float(v2_input) if v2_input else None

    # Calcular el área de la sección de entrada si r1 fue proporcionado
    A1 = math.pi * r1**2 if r1 else None

    # Determinar la variable faltante y calcularla
    if r1 and A2 and v2 and not v1:
        # Calcular v1
        v1 = (A2 * v2) / A1
        print(f"La velocidad de entrada (v1) es de aproximadamente {v1:.2f} m/s")
    elif r1 and A1 and v1 and not v2:
        # Calcular v2
        v2 = (A1 * v1) / A2
        print(f"La velocidad de salida (v2) es de aproximadamente {v2:.2f} m/s")
    elif A1 and A2 and v2 and not v1:
        # Calcular v1
        v1 = (A2 * v2) / A1
        print(f"La velocidad de entrada (v1) es de aproximadamente {v1:.2f} m/s")
    elif A1 and A2 and v1 and not v2:
        # Calcular v2
        v2 = (A1 * v1) / A2
        print(f"La velocidad de salida (v2) es de aproximadamente {v2:.2f} m/s")
    else:
        print("No se puede determinar la variable faltante con los datos proporcionados. Asegúrese de ingresar al menos tres valores conocidos.")

# Ejecutar la función
calculate_velocity()
