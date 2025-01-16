def borrar_duplicados(lista):
    """Se tienen que eliminar elementos duplicados, 
    retornar la lista sin duplicados y presentarlos en 
    el mismo orden

    Args:
        lista (list): Se espera una lista

    Returns:
        list: Se retorna la lista sin duplicados y en orden
    """
    lista_sin_duplicados= [] #Se almacenaran los elementos de la lista  
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    
    return (lista_sin_duplicados)
    