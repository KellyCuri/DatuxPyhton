# Crear un menu iterativo el cual las opciones sean importadas desde otro paquete de programa(módulo )
# Una función que me permita dividir 2 números.
# importar esos módulos desde el archivo main


def dividir_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    except ValueError:
        print("¡Error! Ingrese números válidos.")
    except ZeroDivisionError:
        print("¡Error! No se puede dividir entre cero.")

def sumar_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("¡Error! Ingrese números válidos.")

def mostrar_menu():
    print("----- MENÚ -----")
    print("1. Dividir dos números")
    print("2. Sumar dos números")
    print("3. Salir")

def ejecutar_opcion(opcion):
    if opcion == "1":
        dividir_numeros()
    elif opcion == "2":
        sumar_numeros()
    elif opcion == "3":
        print("Saliendo del programa...")
        quit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Programa principal
if _name_ == '_main_':
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")
        ejecutar_opcion(opcion)

class Producto:
    def _init_(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def _str_(self):
        pais, lote, anio = self.codigo.split('-')
        return f"Producto: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"

# Ejemplo de uso
producto = Producto("Nombre del Producto", "PERU-0001-2023")
print(producto)