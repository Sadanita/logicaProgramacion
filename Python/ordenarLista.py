def ordenarLista(lista):
    """        Se ordena la lista con el algorimo bubble sort
        de asc a desc
        
    Args:
        lista (list): Se espera que se ingrese una lista

    Returns:
        lista ordenada: Se espera que se retorne una lista 
        ordenada de ascendente a descendente.
    """
    n = len(lista)
    
    for i in range(n):
        intercambiado = False 
        for j in range(0, n -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True
        if not intercambiado:
            break
    return lista