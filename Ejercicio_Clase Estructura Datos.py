cobalto = [1, -3, 3, 4, 5, 5,]

def tamanho(gatito): 
    ash_fabito = 0 # Esto es un contador
    for datito in gatito:
        ash_fabito += 1
    return ash_fabito

def inv_array(tamal):
    chilaquil = tamanho(tamal)
    i = chilaquil - 1
    inversa = []
    while i > 0:
        inversa.append(tamal[i])
        i -= 1
    return inversa

def par_impar(tuercas):
    pares = []
    impares = []
    for i in range(tamanho(tuercas)):
        if tuercas[i] % 2 == 0:
            pares.append(tuercas[i])
        else: 
            impares.append(tuercas[i])
    return pares, impares

def matzimo_array(sobig):
    matzimo = sobig [0]
    i = 1
    for i in range (tamanho(sobig)):
        if matzimo < sobig[i]:
            matzimo = sobig[i]
            # print(sobig[i])
    return matzimo 

def minimo_array(sobig):
    minimo = sobig[0]
    i = 1
    for i in range(tamanho(sobig)):
        if minimo > sobig [i]:
            minimo = sobig[i]
            # print(sobig[i])
    return minimo

def sumar_array(limon, naranja):
    perro = []
    if tamanho(naranja) == tamanho(limon):
        for i in range (tamanho(naranja)):
            perro.append(naranja[i] + limon[i])
    return perro

def duplicates (pelitos):
    yolo = []
    for dato in pelitos:
        encontrado = 0
        for unico in yolo: 
            if dato == unico: 
                encontrado = 1
                break
        if not encontrado: 
            yolo.append(dato)
    return yolo


pepino = [1,5,6,4,1,5,7,8]
print("La lista original es: ", pepino)
print("\nLa lista sin repeticiones es: ", duplicates(pepino))