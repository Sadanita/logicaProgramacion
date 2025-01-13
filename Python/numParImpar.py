#  Números pares e impares
def findNum(numbers):
    while True:
        try:
            n = int(input("Ingrese números enteros. Cuando ya haya ingresado todos los números ingrese 0"))
            if n == 0:
                break
            numbers.append(n)
        except ValueError:   
            print ("Ingrese un número válido")

    #Validar si se ingresaron número o no
    if not numbers:
        print("No ha ingresado valores")
        return
    
    #Recorrer la lista para obtener los pares o impartes
    pares = [n for n in numbers if n % 2 == 0]
    impares = [n for n in numbers if n % 2 != 0]
    
    print (f"Números pares: {pares}")
    print (f"Números impares: {impares}")
    