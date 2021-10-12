#Input engloba lo que el usuario debe de escribir desde el teclado en la terminal
#La funcion print añade un salto de linea por lo que el usuario al contestar 
# lo hace en una linea más abajo

#print("Cómo te llamas: ")
#nombre = input()
#print("Me alegro de conocerte, ",nombre)
#------------

#Con  ,end=""  hace que el INPUT 
# se quede en la misma linea en la solucitud.

#print("Como te llamas:   ",end="")
#nombre = input()
#print("Me alegro de conocerte, ",nombre)
#----------

#Una forma más óptima  con menos lineas de código es:
# Con la funcion INPUT() agregando un argumento que 
# se imprime en pantalla,
# sin generar un salto de linea

nombre = input("Como te llamas?: ")
print(f"Me alegro de conocerle, {nombre}")
#------------------


#INPUT() Convierte la entrada en una cadena, 
# aunque escribamos un número. Y ello dará un ERROR.
#Para ello debemos de poner INT delante de INPUT entre ()

#cantidad = int(input("Digame una cantidad en Dolares: "))
#print(f'{cantidad} Dolares son')
#-----------------

#INPUT  con FLOAT.

#cantidad = float(input("Digame una cantidad en Dolares con dos decimales: "))
#print(f'Son  {cantidad} Dolares')
#---------------------------------


#nombre = input("Dígame su nombre: ")
#apellido = input(f"Digame su apellido {nombre}: ")
#print(f'Me alegro de conocerle, {nombre} {apellido}.')
#----------------

#Conversion por el int del input
#Por que INPUT es de Cadenas y para traducir 
# numeros hay que ponerle primero int.

#numero1 = int(input("Ingrese un número: "))
#numero2 = int(input(f"Ingrese un número mayor que {numero1}: "))
#print(f"La diferencia entre ellos es {numero2 - numero1}.")

