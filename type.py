# Con type nos dice que tipo de variable usamos.

#nombre = 'hola'
#a = (1)
#b = (1.0)
#c = (True)
#
#type('nombre')

palabra = 'Hola a todos'
#
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


