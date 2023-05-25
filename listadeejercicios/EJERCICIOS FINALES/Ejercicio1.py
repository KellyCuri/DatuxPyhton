import requests
import sqlite3

def obtener_tipo_cambio():
    # Realizar la solicitud GET a la API
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()

        # Obtener los valores relevantes de la respuesta
        fecha = data['fecha']
        compra = data['compra']
        venta = data['venta']

        # Insertar los datos en la base de datos
        conn = sqlite3.connect('DATAAPIDEKELLY.db')
        cursor = conn.cursor()

        # Crear la tabla si no existe
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tipo_cambio (
                fecha TEXT PRIMARY KEY,
                compra REAL,
                venta REAL
            )
        ''')

        # Insertar los datos en la tabla
        cursor.execute('INSERT INTO tipo_cambio (fecha, compra, venta) VALUES (?, ?, ?)', (fecha, compra, venta))

        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

        print('Datos guardados en la base de datos.')
    else:
        print('Error al obtener los datos de la API.')

# Llamar a la función para obtener y almacenar el tipo de cambio
obtener_tipo_cambio()