"""Okey, tengo un archivo txt de entrada con el siguiente formato:
39687   54930
86219   31559
48536   73145
19932   82178
87646   97411
18305   78515
Debo calcular la suma de la distancia total entre todas las filas.
La distancia total en una fila se calcula sumando la diferencia entre el menor elemento de ambas filas, luego
la diferencia entre el siguiente numero menor, y asi sucesivamente.
Ejemplo:
3   4
4   3
2   5
1   3
3   9
3   3
The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
The third-smallest number in both lists is 3, so the distance between them is 0.
The next numbers to pair up are 3 and 4, a distance of 1.
The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
To find the total distance between the left list and the right list, add up the distances between all the
 pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!"""
"----------------------------------------------------------------------------------------------------------------------"

# Abrimos el archivo de texto y lo guardamos en una variable
#cada persona recive una entrada distinta en formato .txt
with open("/home/code_zone/AdventCode2024/input_p1.txt") as archivo:
    contenido = archivo.read()
distanciaTotal = 0
cadenaIter = contenido.split("\n")  # Contiene 1001 elementos
"Parece que el metodo split() me agrega un caracter en blanco al final de la lista"
# print(cadenaIter)
a = []
b = []
for element in cadenaIter:
    a.append(element[:5])
    b.append(element[8:])
a.sort()
b.sort()
# Elimino los caracteres nulos al principio de las listas con pop()
a.pop(0)
b.pop(0)
for i in range(1000):
    # itero por la cantidad total de elementos de una lista y calculo las distancias para cada elemento.
    distanciaTotal += abs(int(a[i]) - int(b[i]))
# Muestro el resultado final por pantalla
print(distanciaTotal)

# Parte 2 - Utilizo las listas que arme anteriormente
similarScore = 0
aparciciones = 0
for i in range(1000):
    for j in range(1000):
        if a[i] == b[j]:
            aparciciones += 1
    similarScore += (int(a[i])) * aparciciones
    aparciciones = 0
print(similarScore)
