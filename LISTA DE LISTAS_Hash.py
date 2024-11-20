#LISTA DE LISTAS

class HashTable: 
    def __init__(self, size): 
        # Metoodo constructor para inicializar la tabla hash
        self.size = size
        self.table = [ [] for _ in range(size) ] # Crea una lista de tamaño size 

    def isEmpty(self):
        # Metodo para verificar si la tabla Hash esta vacia
        for i in range(self.size):
            # rrecorrer cada posición de la tabla
            
            if len(self.table[i]) > 0:
                # Si la lista en el indice i no esta vacia, la tabla no esta vacia
                return False
        
        # Si todas las listas estan vacias, la tabla 
        return True
            
            # if self.table [i] is not None: 
            #     return False
    
            # # Si encontramos una posición no vacia, 
            # # la tabla no esta vacia
            # return True 
    

    def Size (self):
        # Metodo para obtener el número de elementos en 
        # la tabla hash

        for i in range (self.size):
            # Recorremos cada posición de la tabla.
            
            if self.tabla [i] is not None:
                # Si la posición no esta vacía, aumentamos un contador. 

                Contador += len(self.table[i])
                # Sumar la cantidad de elementos en la lista del indice
                # ratero += 1

            return Contador # Devolver el númer total de elementos 

    def hashfunction (self, key):
        # Metodo para calcular el indice a partir de la clave
        
        if isinstance(key, int):
            # Si clave es entero, usamos modulo del tamaño de la tabla
            return key % self.size # Hash


        # Otra Forma de Llave
        elif isinstance (key, str):
            
            # Si la calve  es una cadena, sumamos los valores 
            # ASCII de sus caracteres
            total = 0

            for char in key: 
                total += ord(char)
            return total % self.size

    def add(self, key, value):
        # Metodo para agregar una clave (llave) 
        # y su valor a la tabla hash

        index = self.hashfunction(key) # Calcular el indice usando la funcion hash

        for i in range (len(self.table[index])):

            if self.table[index][i][0] == key: 
                # Si encontramos la clave, actualizar su valor

                self.table[index][i] == (key, valor)
                # Actualizar el par clave, valor 

                return
        # Si la clave no existe en la lista, agregamos el nuevo par clave-valor

        self.table[index].append((key, value))
        # Agregar el par al final de la lista 

        ''' Esto ya no va
        self.table[index] = (key, value)
        # Almacenamiento el par Key-value en el index calculado'''


    def getByKey (self, key):
        # Metodo para obtener un valor a partir de la clave
        index = self.hashfunction(key)
        
        # Recorrer la lista en el indice calculado
        for k, v in self.table[index]:
            if k == key: 
                #Si encontramos la calve, devolvemo el valor asociado
                return v
        
        # Si no encontramos el valor, devolver None
        return None


        """if self.table[index] is not None: 
            # Si en ese indice hay un elemento

            if self.table[index][0] == key:
                #y la clave coincide, devolvemos el valor asociado
                return self.table[index][1]
            
            # Si no encontramos la clave, devolvemos None
            return None"""
    

    def getByValue(self, value): 
        # Metodo para obtener clave a partir de su valor
        
        for i in range(self.size):
            # Recorrer cada posición de la tabla 
            
            for k, v in self.table [i]:
                #Recorremos cada par clave-valor en la lista del indice i 
                
                if v == value: 
                    # Si encontramos el valor, devolver la clave asociada
                    return k

            # Si no encontramos el valor, devolver None
            return None


'''
            if self.table[i] is not None: 
                # Si la posición no esta vacia
                
                if self.table[i][1] == value: 
                    # Y valor coincide, devolvemos la clave asociada
                    return self.table[i][0]
        
        # Si no encontramos el valor, devolvemos None
        return None'''

# Creamos una tabla Hash de tamaño definido
hash_table = HashTable(5)

# Agregar 2 claves que generan el mismo indice
hash_table.add(1, "valor1") # Hashfunction (1) % 5 --> 1
hash_table.add(6, "valor2") # Hashfunction (6) % 5 --> 1

# Obtenemos los valores de ambas claves
print(hash_table.getByKey(1)) # --> Devolver "valor1"
print(hash_table.getByKey(6)) # --> Devolver "valor2"