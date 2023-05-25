# Convierte los datos a un diccionario
data = df.to_dict(orient='records')
print(df)

import json

# Guarda los datos en un archivo JSON
with open('ejemplo3.json', 'w') as f:
    json.dump(data, f)