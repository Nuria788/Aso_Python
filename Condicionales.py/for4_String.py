# Para un contador f EN la palabra Python imprime el valor f

for f in 'python':
    print (f)


# En horizontal
''' for f in 'python': '''
'''    print (f, end='') '''

#Sustitución del valor de la variable por lo que le pongamos en el print
#Lo hará verticalmente.
for f in 'python':
    print ('Eureka')

#Sustitución del valor de la variable por lo que le pongamos en el print
#Lo hará horizontal
'''for f in 'python':'''
'''print ('Eureka ', end='') '''

#   Control de @. Control de caracteres de una variable de tipo string
# Declaramos una primera variable que es de tipo string que va a almacenar un caracter de @.
# Creamos otra variable de tipa entero. 
# Una tercera variable email que nos pide que ingresemos  -- un email --- .
# Cramos un bucle for con un contador f que analiza el rango del email que 
# ingresamos -- in (introduce el rango y luego ponemos el rango -- mail --) -- y
# toma la cantidad de carcteres como rango, 
# analizará letra por letra del email que ingresemos, y analizará que si 
# una de nuestras letras en un = @ , a nuestra variable cantidad le asiganará el valor = 1.
# cuando finalice va a  analizar si nuestra variable cantidad en >= 1 entonces deducirá que sí 
# hay un arroba en nuesrtro correo.

# Si nuestra variable cantidad es 0 porque no encontro ninguna '@' nos imprimirá -- email incorrecto --

arroba = '@'
cantidad = 0
mail = input('Ingresé su email... ')
for f in mail:
    if f == '@':
        cantidad += 1

if cantidad >= 1:
        print('mail correcto!')
else:
    print('Mail incorrecto, no tiene arroba')
