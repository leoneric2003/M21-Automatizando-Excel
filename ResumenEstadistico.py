# Este programa lee un archivo Excel y crea un resumen estadístico de las calificaciones en todas las materias.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Crear un resumen estadístico de las calificaciones
resumen_estadistico = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].describe()
print('Resumen estadístico de las calificaciones:')
print(resumen_estadistico)
