#1.- Realizar un Menú Iterativo que tenga las siguientes opciones(Solo poner el número de la pregunta):

# - Realizar un programa que dibuje un cuadrado en consola con *, usando bucles.

m=int(input("Numero de filas: "))
n=int(input("Numero de columnas: "))

for i in range (1,m+1):
    for j in range (1,n+1):
        print("*",end="")
    print(" ")


