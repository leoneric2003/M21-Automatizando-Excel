# Este programa lee un archivo Excel y verifica si hay valores nulos en las calificaciones.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Verificar valores nulos en las columnas de calificaciones
valores_nulos = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].isnull().sum()
print('Número de valores nulos por materia:')
print(valores_nulos
