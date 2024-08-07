# Este programa lee un archivo Excel e identifica el alumno con la mayor calificación en cada materia.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Encontrar el alumno con la mayor calificación en cada materia
max_calificaciones = datos[['Nombre', 'Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].iloc[datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].idxmax()]
print('Alumno con la mayor calificación en cada materia:')
print(max_calificaciones)
