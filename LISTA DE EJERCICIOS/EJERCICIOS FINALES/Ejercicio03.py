# Validar una entrada mediante una expresión regular (númerica, texto, email, celular etc)

# Validación númerica
import re
entrada_numerica = '12345'
if re.match(r'^\d+$', entrada_numerica):
    print('La entrada numérica es válida')
else:
    print('La entrada numérica no es válida')

# Validación de texto
import re
entrada_texto = 'abcde'
if re.match(r'^[A-Za-z]+$', entrada_texto):
    print('La entrada de texto es válida')
else:
    print('La entrada de texto no es válida')

# Validación de correo electronico
import re
entrada_email = 'correo@ejemplo.com'
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', entrada_email):
    print('La entrada de correo electrónico es válida')
else:
    print('La entrada de correo electrónico no es válida')

# Validación de celular
import re
entrada_celular = '1234567890'
if re.match(r'^\d{10}$', entrada_celular):
    print('La entrada de número de celular es válida')
else:
    print('La entrada de número de celular no es válida')
