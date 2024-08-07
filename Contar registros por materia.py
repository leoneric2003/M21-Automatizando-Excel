# Este programa lee un archivo Excel y cuenta cuántos registros tienen calificaciones para cada materia.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Contar registros no nulos para cada columna de calificaciones
registros_por_materia = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].notnull().sum()
print('Número de registros por materia:')
print(registros_por_materia)
