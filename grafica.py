import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools

#definiciones
fs = 1000
t = 1
freq = 5
phase = 0
offset = 0

# Crear la figura y el eje
fig, ax = plt.subplots()
x_data = np.linspace(0, t, fs)
y_data = np.sin(2*np.pi*freq*x_data + phase) + offset
line, = ax.plot(x_data, y_data)

# Función de actualización
def actualizar(frame):
    phase_sum = frame*0.1
    y_data = np.sin(2*np.pi*freq*x_data + phase_sum)  # Modificar los datos
    line.set_ydata(y_data)
    ax.legend([f'{frame} Frame'])
    return line,

# Configurar la animación
ani = animation.FuncAnimation(fig, actualizar, frames=itertools.count(), interval=50, cache_frame_data=False)

plt.show()

