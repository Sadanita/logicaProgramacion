def es_polindromo(palabra:str)->bool:
    """
    Función que determina si una palabra es un palindromo
    Args:
        palabra: str Se pasa una palabra como parámetro
    Returns:
        bool: True si la palabra es un polindromo, False en caso contrario
    """
    # Se comprueba si se ha ingresado la palabra, se la vuelve minuscula y se reemplaza los espacios vacíos por nada.
    palabra = palabra.strip().lower().replace(" ","")
    
    #Comprobación si es o no palindroma
    return palabra == palabra[::-1]

#Uso de la función
palabra_usario = input("Ingrese la palabra para comprobar si es palíndroma")

if es_polindromo(palabra_usario):
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")

