#Implementa un string para que calcule la longitud de la palabra más larga de un string
# prefijado en el script. Para simplificar el ejercicio los signos de puntuación que 
# pudiera tener una frase se considerarán como parte de la longitud de la palabra a la 
# que van unidos.

lst = "Esta frase es muy complicada, te lo digo yo."
lst2 = lst.split()
leng = 0
string = ""
for i in range(len(lst2)):
    if len(lst2[i]) >= leng:
        leng = len(lst2[i])

for j in range(len(lst2)):
    if len(lst2[j]) == leng:
        string = lst2[j]
print(string)