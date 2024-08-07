# Este programa lee un archivo Excel y calcula el promedio de calificaciones para cada materia.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Calcular el promedio de calificaciones para cada materia
promedio_materias = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].mean()
print('Promedio de calificaciones por materia:')
print(promedio_materias)
