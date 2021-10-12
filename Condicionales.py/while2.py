#Valor guarda lo que escribe el usuario.


valor = int(input("Ingrese el valor 0 para salir: "))
while valor != 0:
    print("Valor ingresado: ", valor, "Usted no ha ingresado 0")
    valor = int(input("Por favor ingresar 0: "))
print("Gracias!")
