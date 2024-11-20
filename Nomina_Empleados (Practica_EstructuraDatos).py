empleados = []

def agregar_empleado(nombre, sueldo):
    empleados.append({"nombre": nombre,
                      "Sueldo": sueldo})

def modificar_sueldo(nombre, nuevo_sueldo):
    for empleado in empleados: 
        if empleado["nombre"] == nombre: 
            empleado["Sueldo"] = nuevo_sueldo

def eliminar_sueldo(nombre):
    global empleados
    empleados = [e for e in empleados if e["nombre"] != nombre]

def mostrar_empleados():
    for empleado in empleados: 
        print(f"Nombre: {empleado['nombre']}, Sueldo: {empleado['Sueldo']}")

def calcular_nuevo_sueldo():
    total_sueldo = sum(e["Sueldo"] for e in empleados)
    aumento_sueldo = int(total_sueldo / len(empleados) * 1.1) 
    print(f"Nuevo Sueldo = {aumento_sueldo}")

'''# Ejemplo Uso 
agregar_empleado("Maleny Michelle", 2500)
agregar_empleado("Adrian Estrada", 8500)
agregar_empleado("Alejandro Magno", 1500)
mostrar_empleados()
modificar_sueldo("Maleny Michelle", 9500)
mostrar_empleados()
calcular_nuevo_sueldo()
eliminar_sueldo("Alejandro Magno")'''

num_empleados = int(input("¿Cuántos empleados deseas agregar? "))

for _ in range(num_empleados):
    nombre = input("Ingresa el nombre del empleado: ")
    sueldo = int(input(f"Ingresa el sueldo de {nombre}: "))
    agregar_empleado(nombre, sueldo)

mostrar_empleados()

modificar_nombre = input("Ingresa el nombre del empleado cuyo sueldo deseas modificar: ")
nuevo_sueldo = int(input(f"Ingresa el nuevo sueldo de {modificar_nombre}: "))
modificar_sueldo(modificar_nombre, nuevo_sueldo)

mostrar_empleados()


