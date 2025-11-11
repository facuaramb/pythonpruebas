"""SYSTEM MODULE : calculadora.py"""

n1 = input("Ingrese el primer número: ")
n2 = input("Ingrese el segundo número: ")
n1=int(n1)
n2=int(n2)
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2 
Mensaje = f"""para los numeros {n1} y {n2}:
la suma es {suma}, la resta es {resta}, la multiplicacion es 
{multiplicacion} y la division es {division}."""
print(Mensaje)