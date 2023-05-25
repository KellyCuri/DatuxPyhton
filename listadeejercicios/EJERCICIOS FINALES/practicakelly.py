# 1 archivo excel xlsx
import pandas as pd
ruta_archivo = 'C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/listadeejercicios/ejemplo1.xlsx'
df = pd.read_excel(ruta_archivo, sheet_name= "Hoja1")

print(df)

# 2 archivo csv
import pandas as pd
df = pd.read_csv('C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/listadeejercicios/ejemplo.csv',sep=';')
print(df.tail(2+1))

print("SIGUIENTE COMANDO")


#En excel
import pandas as pd
ruta_archivo = 'C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/listadeejercicios/ejemplo1.xlsx'
df = pd.read_excel(ruta_archivo, sheet_name= "Hoja1")

print(df.head(17+1))

print(df.columns)