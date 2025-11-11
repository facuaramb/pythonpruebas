"""system module: for.py"""
Buscar = input("a quien busca? ")


usuarios = ["marco", "juan", "leandro", "facu"]

for usuario in usuarios:
    print(usuario)
    if usuario == Buscar:
        print("encontrado", Buscar)
        break
else:
    print("user no encontrado")
    