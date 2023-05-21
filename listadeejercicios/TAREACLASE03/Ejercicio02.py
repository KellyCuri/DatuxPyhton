# Una tienda de autopartes necesita un programa para catalogar sus productos,
# crear la clase Catálogo y producto ,realizar un objeto dentro de un catálogo productos el cual debe
# tener un método para agregar productos y otra para mostrar toda la lista de productos


class Producto:
    def _init_(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Código: {producto.codigo}")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print("")

# Ejemplo de uso
catalogo = Catalogo()

# Agregar productos
producto1 = Producto("001", "Batería de automóvil", 100)
catalogo.agregar_producto(producto1)

producto2 = Producto("002", "Filtro de aceite", 20)
catalogo.agregar_producto(producto2)

producto3 = Producto("003", "Pastillas de freno", 50)
catalogo.agregar_producto(producto3)

# Mostrar lista de productos
catalogo.mostrar_productos()