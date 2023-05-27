#  Los datos anteriores registrarlos en una base de datos(Sqlite)

import pandas as pd
import sqlite3

# Cargando el archivo
df = pd.read_excel('C:/Users/kelly/OneDrive/Escritorio/Workspacedatux/DatuxPyhton/LISTA DE EJERCICIOS/ejemplo2.xlsx')

# Filtrando el archivo
filtro = df[df['nombre'] == 'kelly']

# Conectandome a la base de datos SQLite
conn = sqlite3.connect('Sqlitekelly.db')

# Creando una tabla
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS datos (nombre TEXT, edad INTEGER, codigo TEXT)')

# Insertando los datos filtrados en la tabla
for index, row in filtro.iterrows():
    nombre = row['nombre']
    edad = row['edad']
    codigo = row['codigo']
    cursor.execute('INSERT INTO datos (nombre, edad, codigo) VALUES (?, ?, ?)', (nombre, edad, codigo))

# Guardando los cambios y cerrando la conexión con la base de datos
conn.commit()
conn.close()