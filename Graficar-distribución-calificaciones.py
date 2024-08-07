# Este programa lee un archivo Excel y grafica la distribución de calificaciones en una materia específica.

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Graficar la distribución de calificaciones en 'Mat_CalculoIntegral'
plt.hist(datos['Mat_CalculoIntegral'].dropna(), bins=10, edgecolor='black')
plt.xlabel('Calificaciones')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones en Mat_CalculoIntegral')
plt.show()
