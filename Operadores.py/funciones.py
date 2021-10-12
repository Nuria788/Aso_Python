

# COUNT  cuenta cuantas letra que le pongamos entre 
# parentésis que hay en la variable palabra
palabra = 'hola a todos'
print(palabra.count('a'))

# INDEX  Nos da la posición de la letra que está en la
#  frase de la variable.
# Pero si esa letra está repetida sólo nos dará la posición 
# de la primera letra que aparezaca.
# Se comienza a contar desde 0
print(palabra.index('a'))

#STARSWITH() Confirma o no si comienza con esa letra -(h) 
# si es así nos devuelve True y no es así nos devuelve False.

print(palabra.startswith('h'))

#ENDSWICHT() Confirma (True) o no (false) 
#con la letra que está entre parentésis.
print(palabra.endswith('s'))



# Primeros 4 carácteres de la variable palabra.--- Hola ---
print(palabra[:4])

# Apartir de la 4 hasta el final --- a todos ---
print(palabra[4:])

#Quita el primero 1: pero el :3 pode que devuelva 
# desde el princio las tres primeras  --- ol --
print(palabra[1:3])

#4: Que devuelve a partir de la 4 posición  
# y el :-1 que desde el final de la frase no devuelva una letra.
#--- a todo ----
print(palabra[4:-1])

# Que devuelva todo desde el princio 
# pero no 2 letras del final de la frase`
# -- Hola a tod -----
print(palabra[:-2])



#Quiero la primera lerta de la frase en mayúscula
# Recordemos que la variable palabra 
# = 'hola a todos' hemos puesto la h en minúscula.
print(palabra.capitalize())

#LOWER Cambia a minúsculas todas las letras de la palabra
frase = 'HOLA A TODOS'
print(frase.lower())

#UPPER() Cambia toda la frase a mayúsculas
frase = 'hola a todos'
print(frase.upper())

#isnumeric() Identifica si nuestra variable contiene unicamente números con False o True
identidad = 'Hola guapa'
frase2 = '123'
frase3 = '123Hola'
print(identidad.isnumeric())
print(frase2.isnumeric())
print(frase3.isnumeric())

# CENTER() Centra por la derecha y por la izq.(50 pixeles)
# LJUST() Ajusta a la izquierda
# RJUST() Aleja el testo hacia la derecha (30 pixeles)

palabra1 = 'Hola'
print(palabra1.center(50))
print(palabra1.ljust(10))
print(palabra1.rjust(50))

# LEN(variable)
palabra2 = ("¿Que tal estas?")
print(len(palabra2))
