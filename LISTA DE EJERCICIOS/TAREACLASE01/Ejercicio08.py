# Escribir un programa que genere una contraseña de un usuario
# Pregunte la contraseña e imprima
# Considerar minusculas y mayúsculas como igual
# lower dif mayuscula de min.

contraseña="Ninguno123"

contraseña_usuario=input("Introduce la contraseña: ")
if contraseña.lower()==contraseña_usuario.lower():
    print("¡Contraseña Correcta!")

else:
    print("Contraseña incorrecta")