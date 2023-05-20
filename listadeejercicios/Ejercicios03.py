def obtener_mayor(numero1, numero2):
    if numero1 > numero2:
        return numero1
    else:
        return numero2

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

mayor_valor = obtener_mayor(numero1, numero2)
print("El mayor valor es:", mayor_valor)