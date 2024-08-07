# Este programa lee un archivo Excel y calcula la desviación estándar de calificaciones para cada materia.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Calcular la desviación estándar de calificaciones para cada materia
desviacion_materias = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].std()
print('Desviación estándar de calificaciones por materia:')
print(desviacion_materias)
