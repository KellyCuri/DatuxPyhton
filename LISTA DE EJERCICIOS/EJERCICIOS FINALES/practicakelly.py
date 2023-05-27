# comvertir aun archivo de excel a json
import pandas as pd

# Lee el archivo de Excel
df = pd.read_excel('C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/listadeejercicios/ejemplo2.xlsx')

# Convirtiendo mis datos del excel en un diccionario
data = df.to_dict(orient='records')
print(df)

import json

# Guardando los datos en un archivo JSON
with open('ejemplo3.json', 'w') as f:
    json.dump(data, f)
