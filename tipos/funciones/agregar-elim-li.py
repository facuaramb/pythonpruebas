"""agregar y eliminar items lista"""

mascotas = [
    "wolfgang", "pelusa", "pulga", "felipe", "pulga", "chanchito"
]

mascotas.insert(1, "Martin") #agregar donde quiero
mascotas.append("finaldelistape") #agregar al final
mascotas.remove("chanchito") #eliminar elemento
mascotas.pop() #elimina el ultimo elemento, o si le paso indice elimina ese
del mascotas[0] #elimina el objeto del indice pasado
mascotas.clear() #limpia to


print(mascotas)