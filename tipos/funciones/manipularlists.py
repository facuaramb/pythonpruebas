"""manipulist"""

mascotas = ["wolfgang", "pelusa", "pulga", "copito"]

mascotas[0] = "bicho"


#print(mascotas[2:])
#print(mascotas[:3])
#print(mascotas[-1])
#print(mascotas[::2])
#print(mascotas[1::2])

numeros = list(range(21))

print(numeros)
print(numeros[1::2]) #imprime impares

#FEO!!!!
#primero = numeros[0]
#segundo = numeros[1]
#tercero = numeros[2]

#primero, segundo, tercero = numeros[:3]

#print(primero, segundo, tercero)

primero, *otros = numeros

print(otros)