# Este programa lee un archivo Excel y filtra los alumnos que tienen calificaciones por encima de 80 en todas las materias.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Filtrar alumnos con calificaciones mayores a 80 en todas las materias
alumnos_alto_rendimiento = datos[(datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']] > 80).all(axis=1)]
print('Alumnos con calificaciones mayores a 80 en todas las materias:')
print(alumnos_alto_rendimiento)
