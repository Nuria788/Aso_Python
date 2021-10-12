# CONTINUE contrario al BREAK. 
# EL bucle sigue hasta el final aunque lo haya la primera vez
# Break para en la primera vex

for letra in 'progremecion':
    if letra == 'e':
      print('letra erronea!')
      continue # continua hasta el fin del bucle
    print(letra)
print("Fin del bucle!")