# Este programa lee un archivo Excel que contiene las calificaciones de los alumnos en varias materias,
# agrega una nueva columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 (con un decimal),
# y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Generar valores aleatorios para la columna "Mat_Fisica"
np.random.seed(0)  # Para reproducibilidad
datos['Mat_Fisica'] = np.round(np.random.uniform(0, 100, datos.shape[0]), 1)

# Guardar el archivo Excel con la nueva columna
archivo_actualizado = 'calificaciones_alumnos_actualizado.xlsx'
datos.to_excel(archivo_actualizado, index=False)

print(f'Archivo actualizado guardado como {archivo_actualizado}')
