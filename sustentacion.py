import matplotlib.pyplot as plt

# Datos de ejemplo para el gráfico
alpha = [-10, -5, 0, 5, 10, 15, 20]  # Ángulo de ataque en grados
Cl = [-0.4, 0.0, 0.4, 0.8, 1.2, 1.0, 0.5]  # Coeficiente de sustentación
Cd = [0.02, 0.025, 0.03, 0.04, 0.06, 0.08, 0.12]  # Coeficiente de arrastre

# Crear la figura y los ejes
fig, ax1 = plt.subplots()

# Gráfica del Coeficiente de Sustentación
ax1.plot(alpha, Cl, 'b-', label='Coeficiente de Sustentación (Cl)')
ax1.set_xlabel('Ángulo de Ataque (grados)')
ax1.set_ylabel('Coeficiente de Sustentación (Cl)', color='b')
ax1.tick_params('y', colors='b')

# Crear un segundo eje y para el Coeficiente de Arrastre
ax2 = ax1.twinx()
ax2.plot(alpha, Cd, 'r-', label='Coeficiente de Arrastre (Cd)')
ax2.set_ylabel('Coeficiente de Arrastre (Cd)', color='r')
ax2.tick_params('y', colors='r')

# Añadir título y leyenda
plt.title('Curvas características para una determinada Planta Alar')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Mostrar el gráfico
plt.show()
