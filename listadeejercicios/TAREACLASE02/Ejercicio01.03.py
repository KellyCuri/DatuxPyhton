# Iterar una lista de elementos que contengan nombre y edad e imprimir solo los mayores de edad

nombres= ["Kelly","Kassandra","Steven","Zoe","Maria","Liam","Katty","Jose"]
edades= [28,24,27,10,52,9,30,52]

print("Solo mayores de edad")
for i in range(len(nombres)):
    if edades [i] >=18:
        print("{0} tiene {1} años de edad".format(nombres[i], edades[i]))


