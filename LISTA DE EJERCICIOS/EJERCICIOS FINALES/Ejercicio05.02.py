# Crear un método que permita leer todos esos datos usando fetchall() e iterar.

import sqlite3
conn = sqlite3.connect('Sqlitekelly.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM datos')
rows = cursor.fetchall()
for row in rows:
    nombre = row[0]
    edad = row[1]
    codigo = row[2]
    
    print(nombre, edad, codigo)


conn.close()
