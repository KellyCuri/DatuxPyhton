# Crear un archivo info.log y que registre eventos de un programa
# El formato que debe guardar es fecha-nameFile-nameEvento,para la fecha
# Usar la librería datetime (from datetime import datetime =>datetime.now() )

from datetime import datetime
def registrar_evento(archivo_kelly, evento_kelly):
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d_%H-%M-%S") 
    nombre_completo = f"{fecha_formateada}-{archivo_kelly}-{evento_kelly}"
    registro = f"{fecha_actual}: {evento_kelly}"  

    with open("Kellyinfo.log", "a") as archivo:
        archivo.write(nombre_completo + "\n")  
        archivo.write(registro + "\n")  
        archivo.write("-" * 50 + "\n")  

# Ejemplo de uso
archivo_kelly = "mi_programa"
evento_kelly = "evento_importante"
registrar_evento(archivo_kelly, evento_kelly)
