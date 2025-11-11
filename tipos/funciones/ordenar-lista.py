"""ordenar listas"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 33, 12, 3, 5, 6, 2, 3, 4, 5, ]
#numeros.sort() #devuelve la lista pero ordenada, numeros.sort(reverse=True) los ordena al reves

numeros2 = sorted(numeros)  #crea otra lista, ordenada reverse=True se puede

print(numeros2)

usuarios = [["chanchito", 4], ["felipe", 1], ["pulga", 5]]


def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
print(usuarios)
