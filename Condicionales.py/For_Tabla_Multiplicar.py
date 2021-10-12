# Tabla de multiplicar
# Valor es el número que introduce el usuario.
# Nos pide que introduccamos un valor.
# Imprime el valor que el usuario introdujo -- ,valor.
# Ponemor un bucle For con un rango 11, porque son los valores que tiene una tabla de multiplicar. 
# Ponemos sólo un 11 porqur así empieza desde 0 hasta el 11 (10)

# Imprime valor ( lo introducido por el usuario), X (que representa el por -- multiplicar --), 
# el contador f (en la primera vuelta pondrá el 0, en la seguinda vuelta el 1,el 2...), 
# =  y asi realizará una multiplicación en cada vuelta. 
# El contador se encarga de cada vez sea un número 1, el 2 , 3...


valor = int(input('Indique el valor de tabla: '))
print('Eligió ver la tabla del: ', valor)

for f in range(11):
    print(valor, 'x', f, '=', f*valor)
