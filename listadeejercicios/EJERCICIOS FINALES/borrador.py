# csv(<ruta archivo>, sep=<separador datos>)

import pandas as pd
df = pd.read_csv('C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/ejemplo.csv',sep=';')
#print(df.shape) cantidad por filas y columnas
# tail -> retorna los últimos 5 resultados del df
print(df.tail())
