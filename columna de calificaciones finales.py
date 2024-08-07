# Este programa lee un archivo Excel, añade una columna de calificaciones finales como el promedio de todas las materias,
# y guarda el archivo actualizado.

import pandas as pd

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Calcular el promedio de calificaciones y añadirlo como una nueva columna
datos['Calificaciones_Finales'] = datos[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']].mean(axis=1)

# Guardar el archivo Excel con la nueva columna
archivo_actualizado = 'calificaciones_alumnos_con_finales.xlsx'
datos.to_excel(archivo_actualizado, index=False)

print(f'Archivo actualizado guardado como {archivo_actualizado}')
