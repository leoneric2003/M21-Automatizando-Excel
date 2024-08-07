# Este programa lee un archivo Excel que contiene las calificaciones de los alumnos en varias materias,
# y grafica dichas calificaciones para cada alumno, evitando que las etiquetas del eje X se encimen.

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Obtener los nombres de los alumnos y sus calificaciones
nombres = datos['Nombre']
calificaciones = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]

# Crear un gráfico de barras apiladas para cada alumno
fig, ax = plt.subplots(figsize=(10, 6))

# Definir el ancho de las barras y la posición de cada grupo de barras
bar_width = 0.25
index = range(len(nombres))

# Graficar las barras para cada materia
for i, columna in enumerate(calificaciones.columns):
    ax.bar(index, calificaciones[columna], bar_width, label=columna)

# Ajustar las etiquetas del eje X para que no se encimen
ax.set_xticks(index)
ax.set_xticklabels(nombres, rotation=45, ha='right')

# Añadir etiquetas y título
ax.set_xlabel('Alumnos')
ax.set_ylabel('Calificaciones')
ax.set_title('Calificaciones de los alumnos en distintas materias')
ax.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
