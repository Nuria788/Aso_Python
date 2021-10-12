# BREAK 
# Declaramos una variable conador que se llama  letra
# Si nuestra variable letra cada vez que recorra la palabra  programación.
# Si el valor de nuestra variuable letra es = m  el bucle se corta.
 

#for letra in 'programacion':
 #   print(letra)
  #  if letra == "m":
   #     break # de aquí sale el bucle
#print("Letra encontrada: ", letra, 'Fin de bucle')

# WHILE
# Variable llamado conteo con un valor = 10.
# Abrimos un bucle en que dice que mientra que esta variable sea mayor de 0
# Va ir imprimiendo por consola que diga -- conteo en: y el valor de la 
# variable de ese momento de esa vuelta. Para vuelta 1 el conteo será 10
# Luego coge el valor que ya tiene y le va a restar 1 pasa a valer 9.
# Si en conteo es = 5 rompe el conteo.


conteo = 10
while conteo > 0:
    print("Conteo en : ", conteo)
    conteo = conteo -1
    if conteo == 5:
        break # aqui sale el bucle
print("Fin del conteo")

