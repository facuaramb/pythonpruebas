"""SYSTEM MODULE: funciones.py"""
def hola():
    """hola"""
    print("hola mundo")
    print("chau mundo")
hola()

def suma(i, j):
    """suma"""
    i = int(i)
    j = int(j)
    result= i + j
    print(f"resultado es {result}")

pepe1 = input("ingrese numero 1 ")
pepe2 = input("ingrese numero 2 ")

suma(pepe1, pepe2) #llamo a suma
    #llamo a suma