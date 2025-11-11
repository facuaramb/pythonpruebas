def reverse(texto):
    texto_reves = ""
    for char in texto:
        texto_reves = char + texto_reves
    return texto_reves

def no_space(texto):
    sinspacio = ""
    for char in texto:
        if char != " ":
            sinspacio += char
    return sinspacio

def es_palindromo(texto):
    sinespacio2 = no_space(texto)
    textoalreves = reverse(sinespacio2)
    if sinespacio2 == textoalreves:
        return True
    else:
        return False

textouser = input("ingrese texto: ")
print(textouser)
print(no_space(reverse(textouser)))
print(es_palindromo(textouser))