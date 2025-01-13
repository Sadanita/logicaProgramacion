
#Contar las palabras de una frase
def contWord(frase):
    frase = input("Ingrese una frase para contabilizar sus palabras")
    try:
        if frase == any:
            print("No ingresó frase")
    except ValueError:
        print("No ingresó frase")
    frase.split()
    print(f"La frase tiene {len(frase.split())} palabras")