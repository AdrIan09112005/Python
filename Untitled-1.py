class Nodo: # Este manejará los datos
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agarrando {dato} a la cima de la Pila\n")
        # Si no hay datos, agregar el valor en el elemento superior
        if self.superior == None:
            self.superior = Nodo(dato)
            return 0
        
        nuevo_nodo = Nodo(dato) # Crear un nuevo dato al Nodo
        nuevo_nodo.siguiente = self.superior 
        self.superior = nuevo_nodo

    def desapilar(self): 
        # Si no hay datos en el nodo 
        # superior, regresamos
        if self.superior == None:
            print("No hay ningun elemento")
            return 0
        print(f"\nDesapilar {self.superior.dato}")
        self.superior = self.superior.siguiente

    def imprimir(self):
        print ("Imprimiendo la Pila")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior

        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end = ",")
            nodo_temporal = nodo_temporal.siguiente
            print("")

# Uso de Pila_EJEMPLO
pila = Pila()
pila.apilar("Juan Escutia")
pila.apilar("Vicente Fernandez")
pila.apilar("Alejandro Fernandez")
pila.imprimir()
pila.desapilar()
pila.imprimir()
pila.desapilar()
pila.apilar("Johan Sebastian")
pila.imprimir()