def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        print("Letra actual:", char)
        texto_al_reves = char + texto_al_reves
        print("Acumulado:", texto_al_reves)
    return texto_al_reves

reverse("hola")