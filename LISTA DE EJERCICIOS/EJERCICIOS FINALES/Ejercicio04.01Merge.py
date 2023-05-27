# Usando Merge 
import pandas as pd

ruta_archivo1 = 'C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/LISTA DE EJERCICIOS/ejemplo1.xlsx'
ruta_archivo2 = 'C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/LISTA DE EJERCICIOS/ejemplo2.xlsx'

dataframe1 = pd.read_excel(ruta_archivo1)
dataframe2 = pd.read_excel(ruta_archivo2)

columna_clave = 'codigo'
resultado_merge = pd.merge(dataframe1, dataframe2, on=columna_clave)

print(resultado_merge)