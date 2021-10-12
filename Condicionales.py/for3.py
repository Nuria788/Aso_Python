# Nos pedira que ingresemos un Valor 5 veces (range(5))
# Ese valor lo sumara con el valor de suma --- suma = 0
# Cuando ya hayan pedido los 5 valores nos dará su suma y 
# luego la división por 10
suma = 0
for f in range(5):
    valor=int(input("Ingrese un valor: "))
    suma = suma + valor
print("La suma es: ", suma)
promedio = suma/10
print("El promedio es: ", promedio)