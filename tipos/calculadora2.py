"""SYSTEM MODULE: calculadora2.py"""
resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int (resultado)
    op = input("ingrese operacion suma resta multi div: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else: print("operacion no valida.")

    print(f"el resultado es {resultado}")