# Este programa lee un archivo Excel que contiene las calificaciones de los alumnos en varias materias,
# imprime la cantidad de registros (filas) y campos (columnas), identifica y muestra qué campos son numéricos,
# agrega una nueva columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100 (con un decimal),
# ordena la tabla por el campo "Nombre", y guarda el archivo actualizado.

import pandas as pd
import numpy as np

# Cargar el archivo Excel
archivo = 'calificaciones_alumnos.xlsx'
datos = pd.read_excel(archivo)

# Imprimir la cantidad de registros y campos
num_registros = datos.shape[0]
num_campos = datos.shape[1]
print(f'Cantidad de registros (filas): {num_registros}')
print(f'Cantidad de campos (columnas): {num_campos}')

# Identificar y mostrar qué campos son numéricos
campos_numericos = datos.select_dtypes(include=[np.number]).columns
print('Campos numéricos:')
for campo in campos_numericos:
    print(f'- {campo}')

# Generar valores aleatorios para la columna "Mat_Fisica"
np.random.seed(0)  # Para reproducibilidad
datos['Mat_Fisica'] = np.round(np.random.uniform(0, 100, datos.shape[0]), 1)

# Ordenar la tabla por el campo "Nombre"
datos = datos.sort_values(by='Nombre')

# Guardar el archivo Excel con la nueva columna y la tabla ordenada
archivo_actualizado = 'calificaciones_alumnos_actualizado.xlsx'
datos.to_excel(archivo_actualizado, index=False)

print(f'Archivo actualizado guardado como {archivo_actualizado}')
