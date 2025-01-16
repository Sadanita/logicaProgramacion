def eliminarNegativos(lista):
    
    #Se eliminan los negativos
    lista_positivos = [num for num in lista if num >= 0]
    
    #Se ordena la lista
    lista_positivos.sort()
    
    return lista_positivos