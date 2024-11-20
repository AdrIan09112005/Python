def Busqueda_Binaria(lista, elemento): 
    # Si la lista esta vacia, retornar -1 
    if not lista: 
        return -1
    
    # Calcular el punto medio de la lista
    medio = len(lista)//2 # int(len(lista) / 2)

    # Verificar si el elemento esta en el medio
    if lista [medio] == elemento: 
        return medio

    # Si el elemento es mayor, busacar en la mitad derecha
    elif lista[medio] < elemento: 
        lista_derecha = lista[medio + 1 : ]

        # Buscar el elemento en la sublista derecha
        subresultado = Busqueda_Binaria(lista_derecha, elemento_a_buscar)

        # Si el elemento se encuentra en la sublista derecha
        # ajustar el indice
        if subresultado != -1: 
            return medio + 1 + subresultado

            # Ajustar el indice con la posición del subarreglo
        else: 
            return -1

    # Si el elemento es menor, buscar en la mitad izquierda
    else: 
        return Busqueda_Binaria(lista[: medio], elemento)


# Ejemplo de uso 
# Recordar que la lista debe de estar odenada

lista = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
elemento_a_buscar = 5
resultado = Busqueda_Binaria(lista, elemento_a_buscar)

# Imprimir mensajes basados en el resultado de la busqueda
if resultado != 1:
    print(f"El elemento {elemento_a_buscar} esta en el indice: {resultado}")

else: 
    print(f"El elemento {elemento_a_buscar} no esta en la lista. ")

