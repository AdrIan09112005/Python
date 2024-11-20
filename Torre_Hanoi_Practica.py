# Torre Hanoi

def Hanoi(a, b, c, n):
    ''' NOTA: 
        a: Origen 
        b: Destino
        c: Auxiliar
    '''

    # Caso Base
    # Si solo hay un disco, se mueve directamente del origen destino
    
    if n == 1: 
        print(f"Mover disco 1 de la torre {a} a la torre {b}")
        return None

    # Mover n-1 discos de Origen a Auxiliar usando Destino como apoyo 
    Hanoi(a, c, b, n-1)

    # Mover disco n de Origen a Destino
    print(f"Mover disco {n} de la torre {a} a la torre {b}")

    # Mover n-1 discos de Auxiliar a Destino usando Origen como apoyo 
    Hanoi(c, b, a, n-1)

# Ejemplo de Uso
n = 3
Hanoi ("A", "B", "C", n)