# Este programa lee un archivo Excel y muestra las calificaciones más bajas y más altas en cada materia.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Mostrar calificaciones más bajas y más altas en cada materia
calificaciones_extremas = {
    'Min': datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].min(),
    'Max': datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].max()
}
print('Calificaciones extremas por materia:')
print(pd.DataFrame(calificaciones_extremas))
