# 4.1 Realizar una operación al archivo (ya sea filtro ,merge ,añadir columna con lógica ,etc)
# 1 archivo excel xlsx
import pandas as pd
ruta_archivo = 'C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/LISTA DE EJERCICIOS/ejemplo2.xlsx'
df = pd.read_excel(ruta_archivo, sheet_name= "Hoja1")

# Filtros
columna_filtrada = df['nombre']
print(columna_filtrada)

# filtros con logica
edades_filtradas = df[df['edad'] >= 32]
print(edades_filtradas)

#  Añadir una columna con logica

df['NuevaColumna'] = ['Tienen deudas' if edad >= 32 else 'Pueden que no tengan deudas' for edad in df['edad']]
print(df)