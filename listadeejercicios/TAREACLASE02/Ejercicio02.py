# Realizar un Programa que simule funcionalidades de una Biblioteca, definir la biblioteca
# como un diccionario.
# - La biblioteca deberá tener las siguientes operaciones:
# - Obtener la lista de categorías de libros.
# - Obtener nombres de los libros y autores.
# - Poder cambiar el estado de un libro a prestado
# - Lista de usuarios de la biblioteca.



biblioteca = {
    "Categorias": ["Novela", "Ciencia Ficción", "Infantil"],
    "libros": {
        "Novela": [{"nombre":"Mujercitas","autor":"Louisa May Alcott"},
                   {"nombre":"Romeo y Julieta","autor":"William Shakespeare"},
                   {"nombre":"Orgullo y prejuicio","autor":"Jane Austen"}],
        "Ciencia Ficción": [{"nombre":"Divergente","autor":"Veronica Roth"},
                            {"nombre":"Maze Runner","autor":"James Dashner"},
                            {"nombre":"Los Juegos del hambre","autor":"Suzanne Collins"}],
        "Infantil": [{"nombre":"Un gran cambio","autor":"Micaela Plaza"},
                     {"nombre":"El principito","autor":"Antoine de Saint"}]
    },
    "usuarios": ["Kelly Curi Laura", "Steven Cornejo Castro"]
}

# Obtener la lista de categorías de libros
categorias = biblioteca["Categorias"]
print("Categorías de libros:", categorias)

# Obtener nombres de los libros y autores
libros = []
for categoria in biblioteca["libros"]:
    for libro in biblioteca["libros"][categoria]:
        libros.append((libro["nombre"], libro["autor"]))
print("Libros y autores:", libros)

# Cambiar el estado de un libro a prestado
libro_prestado = "Mujercitas"
for categoria in biblioteca["libros"]:
    for libro in biblioteca["libros"][categoria]:
        if libro["nombre"] == libro_prestado:
            libro["prestado"] = True
            print("El libro", libro_prestado, "se marcó como prestado.")
            break
    else:
        continue
    break
else:
    print("El libro", libro_prestado, "no se encontró en la biblioteca.")

# Lista de usuarios de la biblioteca
usuarios = biblioteca["usuarios"]
print("Usuarios de la biblioteca:", usuarios)