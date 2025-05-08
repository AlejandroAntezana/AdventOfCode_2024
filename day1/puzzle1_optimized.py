"""Revise el codigo con gpt4 y estas son los cambios que hice"""
# Cargar el archivo y procesar líneas válidas
with open("/home/code_zone/AdventCode2024/input_p1.txt") as archivo:
    lineas = [line.strip() for line in archivo if line.strip()] #Esto evita el caracter vacio al final

# Inicializar listas
a = []
b = []

# Separar los valores de cada línea
for linea in lineas:
    a.append(linea[:5])
    b.append(linea[8:])

# Ordenar listas
a.sort()
b.sort()

# Calcular la distancia total (Parte 1)
distancia_total = sum(abs(int(a[i]) - int(b[i])) for i in range(len(a)))
print(distancia_total)

# Parte 2 - Calcular similarScore
from collections import Counter

# Contar apariciones de cada elemento en b
#devuelve un diccionario de la forma valor:cant_apariciones
#Es mas eficiente que realizar un bucle anidado

contador_b = Counter(b) #contador_b ahora es un diccionario

# Calcular similarScore usando los conteos
similar_score = sum(int(valor) * contador_b[valor] for valor in a)
print(similar_score)