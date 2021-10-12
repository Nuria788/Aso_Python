#Mientras que el valor de la variable f sea menor o igual al valor que ingrese el usuario,
# se imprimirá el valor de nuestra variable de ese momento = 1  luego le sumará un 1 a esa variable f.
# El sistema evaluará si ese valor de f después de sumarle 1 es menor o igual al valor que ingresamos.
# Mientras sea menor o igual seguirá imprimiendo el valor de f  y asi sucesivamente hasta 
# que no se cumpla la condición que será cuando imprima Gracias!


valor = int(input("Ingrese el numero final: "))
f = 1
while f <= valor:
    print("Valor = ", f)
    f +=1
print('Gracias!')
