"""SYSTEM INFO: tipos/if.py"""
edad = input("ingrese edad: ")
edad = int(edad)
boole = input(f"""su edad se registró como {edad} años, continuar? s/n """)

if boole == "s":
    if edad >= 90:
        print("viejo")
    elif edad >= 80:
        print("señor")
    elif edad <= 40 & edad > 18:
        print("Joven")
    elif edad <= 18:
        print("enano")
else:
    print("reinicia el programa.")