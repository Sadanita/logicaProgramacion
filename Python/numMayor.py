def findNum(numbers):  # Defino la función y como argumento la lista de números que recibirá
    
    # Crear un ciclo while para que se puedan ingresar varios números a la lista
    while True:  # El ciclo inicia en estado true.
        try:
            n = int(input("Ingrese números enteros. Cuando ya haya ingresado todos los números ingrese 0: "))
            if n == 0:  # Validación por si es que el usuario desea terminar el ciclo
                break  # Finaliza el ciclo
            numbers.append(n)  # Vamos a agregar el número en la lista llamada numbers, esto con la función append
        except ValueError:
            print("Ingrese un número válido")  # Si el usuario no ingresa un número válido
    
    # Validar si se ingresaron números
    if not numbers:
        print("No se ingresaron números.")
        return
    
    # Inicializamos el primer número como el mayor y su índice como 0
    max_num = numbers[0]
    max_index = 0
    
    # Recorremos la lista, comenzamos desde el índice 1 porque ya tenemos el primer valor como máximo
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:  # Comparamos si el número es mayor que el actual máximo
            max_num = numbers[i]  # Actualizamos el número máximo
            max_index = i  # Actualizamos el índice del número mayor
    
    # Imprimimos el número mayor y su índice
    print(f"El número mayor es {max_num} y su índice es {max_index}.")