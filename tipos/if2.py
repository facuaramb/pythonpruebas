"""SYSTEM MODULE"""
inp = input("usted está loco? si/no ")

inp = True if inp == "si" else False

mensaje = "usted está loco" if inp is True else "usted está cuerdo."

print(mensaje)