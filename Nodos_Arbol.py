class Nodo: 
    '''
    Iniciarlizar un nuevo nodo con un valor especifico
        Parametros: 
            v: Cualquier valor a almacenar en el nodo
    '''

    def __init__ (self, v): 
        self.homo = None #Referencia al hijo izquierdo del nodo 
        self.hetero = None # Referenecia al hijo derecho del nodo
        self.elemento = v # Dato o valor almacenado en el nodo. 


def Inorder(taro): 
    '''
    Realiza el recorrido inorden del arbol binario
    Imprime los nodos en el orden: I-R-D

    Parametros: 
        taro = Nodo raiz del arbol o subarbol a recorrer 
    '''
    if taro: # Si el nodo actual no es nulo
        # recorrer el subarbol izquierdo
        Inorder (taro.homo) 

        # Recorrer el arbol derecho
        Inorder(taro.hetero)
        
        # Visitar el nodo raiz 
        print(taro.elemento, end = " ")


def Preorder(taro): 
    '''
    Realiza el recorrido inorden del arbol binario
    Imprime los nodos en el orden: I-R-D

    Parametros: 
        taro = Nodo raiz del arbol o subarbol a recorrer 
    '''
    if taro: # Si el nodo actual no es nulo
        # Visitar el nodo raiz 
        print(taro.elemento, end = " ")
        
        # recorrer el subarbol izquierdo
        Preorder (taro.homo) 

        # Recorrer el arbol derecho
        Preorder(taro.hetero)


def Postorder(taro): 
    '''
    Realiza el recorrido inorden del arbol binario
    Imprime los nodos en el orden: I-R-D

    Parametros: 
        taro = Nodo raiz del arbol o subarbol a recorrer 
    '''
    if taro: # Si el nodo actual no es nulo
        # recorrer el subarbol izquierdo
        Postorder (taro.homo) 

        # Recorrer el arbol derecho
        Postorder(taro.hetero)

        # Visitar el nodo raiz 
        print(taro.elemento, end = " ")



# Función principal que se ejecuta al correr el scrip
if __name__ == "__main__": 
    
    # Contrucción manual del arbol binario
    groot = Nodo (12) # Nodo raiz del arbol

    # Construcción del subarbol izquierdo.
    groot.homo = Nodo(7) # Nodo izquierdo de la raiz 12 
    groot.homo.homo = Nodo (4) # Nodo izquierdo de la raiz 7
    groot.homo.homo.homo = Nodo (2) # Nodo izquierdo de la raiz 4
    
    groot.homo.hetero = Nodo (9) # Nodo derecho de la raiz 7
    groot.homo.hetero.homo = Nodo (8) # Nodo izquierdo de la raiz 9
    groot.homo.hetero.hetero = Nodo (11) # Nodo derecho de la raiz 9


    # Construcción subarbol derecho
    groot.hetero = Nodo(21) # Nodo derecho de la raiz 12
    groot.hetero.homo = Nodo(16) # Nodo izquierdo de la raiz 21
    groot.hetero.hetero = Nodo(25) # Nodo derecho de la raiz 21
    groot.hetero.homo.hetero = Nodo(19) # Nodo derecho de la raiz 19


    # Llamada a las funciones de recorrido
    print("Recorrido en Inorder: ", end = " ")
    Inorder(groot) # Imprime recorrido Inorder

    print("Recorrido en Inorder: ", end = " ")
    Preorder(groot) # Imprime recorrido Preorder

    print("Recorrido en Inorder: ", end = " ")
    Postorder(groot) # Imprime recorrido Postorder
