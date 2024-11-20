estudiantes = []


def agregar_estudiante(nombre, calificacion): 
    estudiantes.append({"nombre": nombre,
                        "Calificacion": calificacion})

def modificar_calificacion(nombre, nueva_calificacion):
    for estudiante in estudiantes: 
        if estudiante["nombre"] == nombre: 
            estudiante["Calificacion"] = nueva_calificacion

def eliminar_estudiante(nombre):
    global estudiantes
    estudiantes = [e for e in estudiantes if e["nombre"] != nombre]

def mostrar_estudiantes():
    for estudiante in estudiantes: 
        print(f"Nombre: {estudiante['nombre']}, Calificacion: {estudiante['Calificacion']}")

def calcular_promedio(): 
    total_calificaciones = sum(e["Calificacion"] for e in estudiantes)
    promedio = total_calificaciones / len(estudiantes)
    print(f"Calificacion promedio del salon = {promedio}")

# Ejemplo Uso 

print("----- CALIFICACIONES -----")
agregar_estudiante("Alan", 9)
agregar_estudiante("Alan2", 8)
agregar_estudiante("Adrian3", 7)
mostrar_estudiantes()

print("\n--- CALIFICACIONES MODIFICADAS ---")
modificar_calificacion("Alan", 10)
mostrar_estudiantes()

print("\n--- MUESTREO DE CALIFICACIONES ---")
mostrar_estudiantes()

print("\n--- PROMEDIO DEL SALON ---")
calcular_promedio()
eliminar_estudiante("Alan2")