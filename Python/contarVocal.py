
#  Contar vocales en una cadena 
def contarVocales(cadena):
    cadena = cadena.lower()
    
    vocales= "aeiou"
    
    contador = 0

    for char in cadena:
        if char in vocales:
            contador += 1

    print(f"El total de vocales encontradas es: {contador}")
    