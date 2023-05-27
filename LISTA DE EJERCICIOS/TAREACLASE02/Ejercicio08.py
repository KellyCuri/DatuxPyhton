# Generar una funcion rango hasta un numero maximo (10**5) con step y 
# agregar a una lista los numeros que cumplan las siguientes opciones, que sean primos
import math

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def generar_lista_primos(maximo, step):
    primos = []
    for numero in range(2, maximo + 1, step):
        if es_primo(numero):
            primos.append(numero)
    return primos

maximo = 10**5
step = 1
lista_primos = generar_lista_primos(maximo, step)

print(lista_primos)