"""SYSTEM MODULE: tipos/06-numeros.py"""

import math

numero = 2
decimal = 2.2
imaginario = 2 + 2j

print(1+3)  # Suma
print(3-1)  # Resta
print(2*3)  # Multiplicación
print(6/2)  # División
print(7//2)  # División entera
print(2**3)  # Potencia
print(7%3)  # Módulo

print(round(decimal))  # Redondeo

print(abs(-7))  # Valor absoluto    

print(type(imaginario))  # Tipo de dato

print(math.ceil(4.2))  # Redondeo hacia arriba
print(math.floor(4.7))  # Redondeo hacia abajo
print(math.sqrt(16))  # Raíz cuadrada
print(math.pi)  # Valor de pi
print(math.isnan(math.sqrt(1)))  # Verificar si es NaN
print(math.pow(2, 3))  # Potencia usando math
print(math.log(100, 10))  # Logaritmo base 10

#math documentation: https://docs.python.org/3/library/math.html
