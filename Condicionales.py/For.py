#Una variable f EN un rango de 0 a 10
#imprime
# Un texto que diga... Valor de f y 
# luego concatenamos el valor correspondiente f en el mmento 
# que vaya a imprimir la vuelta de bucle correspondiente

# El contador es f
# Los bucles siempre tienen: un control, una variable de contador (f) 
# para un bucle FOR, por lo tanto para el valor de f en un rango de 0 a 10 (valor final 10.)

for f in range(10):
    print("Valor de f:", f)

# Ejemplo while 
# Es lo mismo que el ejemplo del For pero en el While debemos de ponerle f += 1
# Tb se debe de especificar en While el valor de f en el FOR no 
# Tb se dene de especificar mientras f sea menor o igual al valor ingresado.

f = 0
while f<10:
    print("Valor de f", f)
    f +=1
