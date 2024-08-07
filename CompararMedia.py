# Este programa lee un archivo Excel y compara la media de calificaciones entre dos materias.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Calcular la media de calificaciones en las dos materias y compararlas
media_calculo = datos['Mat_CalculoIntegral'].mean()
media_programacion = datos['Mat_ProgramacionOOP'].mean()
print(f'Media de calificaciones en Mat_CalculoIntegral: {media_calculo}')
print(f'Media de calificaciones en Mat_ProgramacionOOP: {media_programacion}')
