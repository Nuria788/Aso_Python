#Ejecucion condicional
#Al declarar el IF hay que poner :  la condicion a evaluar.
#La siguiente linea de IF debe de estar sangrada.
#Sino es cierto no se cumple la condicion y como no 
# tiene otra condición se quedará así

#x = -2
#if x > 0:
    #print("x es positivo")
#----------------------------

#x = -8
#if x > 0:
 #   print("x es positivo")
#print("Este se imprimirá si o si por que no es parte del IF, está fuera de la sangría.")
#-------------------

#Alternativa sino cumple la condición
#en  if (prueba == 20):  hay que ponerle == porque es una 
# comparación si pusieramos = sería una asignación.
#Si else lo ponemos con sangria daría error porque formaría parte del IF.

#prueba = 20
#if (prueba == 20):
 #   print("Es igual a 1,")
 #   print("y si es igual")
#else:
 #   print("no es igual a 1")
#-------------

#Ejecucion Alternativa Ejemplo de averiguar si es 
# par o impar el número asignado al X con el modulo
#Ponemos else porque solo evaluamos dos posibilidades.

#X = 7
#if X%2 == 0:
#    print (X, "es par")
#else:
#    print(X, "es impar")
#----------------------------

#Condicionales Encadenados:
# Permite evaluar 3 posibles salidas a un problema.

#x = 10
#y = 10
#if x < 7:
 #   print(x,"es menor que",y)
#elif x > y:
 #   print(x,"es mayor que" ,y)
#else:
 #   print(x,"&", y, "son iguales")
#------------------------------------

#Condicionales Anidados.  IF-ELSE (IF-ELSE).
#Es lo mismo que el ejercicio anterior pero anidado.

#x = 5
#y = 5
#if x == y:
#    print(x, "&", y, "son iguales")
#else:
 #   if x < y:
  #      print(x, "es menor que",y)
   # else:
    #    print(x, "es mayor que",y)
#---------------------------------------------------------

#Implementa un script que reciba por entrada 
# estandar el nombre del usuario
# y lo  compare con el tuyo. Deberás darle 
# la bienvenida al curso, pero se lo
# dirás de manera especial si se llama como tú:
# "Bienvenido al curso de So tocay@"


nombre=input("Escribe tu nombre: ")
 
if nombre =="Nuria":
        print("Bienvenida al curso de ASO tocay@")
else:
    print("Bienvenido al curso de Aso")
    print("Bienvenido al curso de Aso",nombre)
    print("Bienvenido al curso de Aso"+nombre)



    



