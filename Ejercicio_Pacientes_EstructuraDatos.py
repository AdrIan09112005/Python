''' Ejercicio

Implementar una cola para gestionar una sala 
de espera de un consultorio medico. Cada paciente
tiene su nombre y una hora de llegada. El objetivo
es permitir al usuario añadir pacientes a la cola, 
ver al sigueinte paciente y atender al paciente.  

Pasos:
    1. Implementa la calse cola.
    2. Cada paciente debe de ser un objeto
    3. Implementa una interfaz simple 
        que permita añadir pacientes:
            -Ver siguiente paciente
            - Atender al pacientes 
            - Salir
'''

class Cola: 
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Verificar que la cola esta vacia baby
        return len(self.items) == 0 # variable - Boolena

    def encolar(self, item):
        # Agregar un elemento al rear de al cola
        self.items.append(item) # append - Con esto agregas un elemento. 

    def desencolar (self):
        # Eliminamos el elemento frontal
        if self.is_empty():
            raise IndexError("La cola esta vacia")
        return self.items.pop(0)

    def size(self):
        # Obtener el tamaño de la cola
        return len(self.items)

    def peek(self):
        if self.is_empty():
            raise IndexError("La cola esta vacia")
        return self.items[0]


class Paciente: 
    def __init__(self, nombre, hora_llegada):
        self.nombre = nombre
        self.hora_llegada = hora_llegada
    
def main():
    queue = Cola()
    print("Bienvenido de nuevo\n")
    while True: 
        print("Opciones: ")
        print("1. Agregar paciente")
        print("2. Atender siguiente paciente")
        print("3. Ver siguiente paciente")
        print("4. --FINALIZAR PROGRAMA--")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            hora_llegada = input("Introduce la hora de llegada (ejemplo 10:00 am): ")
            paciente = Paciente(nombre, hora_llegada)
            queue.encolar(paciente)
            print(f"Paciente {nombre} añadido a la cola\n")
        
        elif opcion == "2":
            if not queue.is_empty():
                paciente = queue.desencolar()
                print(f"paciente {paciente.nombre} atendido\n")
            else: 
                print("Ya no hay pacientes\n")

        elif opcion == "3":
            if not queue.is_empty():
                paciente = queue.peek()
                print(f"Siguiente paciente a atender: {paciente.nombre}, Hora de llegada {paciente.hora_llegada}\n")
            else: 
                print("Ya no hay pacientes\n")

        elif opcion == "4":
            break 

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()