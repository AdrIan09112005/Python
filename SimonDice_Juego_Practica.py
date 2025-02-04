import tkinter as tk
import random 
from tkinter import messagebox

# Definir los colores RGB
colores_rgb = {
                'Rojo': (255, 0, 0),
                'Verde': (0, 255, 0),
                'Azul': (0, 0, 255),
                'Amarillo': (255, 255, 0)
}

# Función para convertir RGB a Hx
def rgb_a_hex(rgb):
    return '#%02x%02x%02x' % rgb

class SimonDice: 
    def __init__(self, ventana):
        # Inicializar la ventana y las variables del juego
        self.ventana = ventana
        self.ventana.title("Simon Dice")
        self.ventana.geometry("400x500")

        # Lista de nombres de colores disponibles
        self.colores = list(colores_rgb.keys())

        # Secuencia generada por el juego
        self.secuencia_juego = []

        # Secuencia ingresada por el jugador 
        self.secuencia_jugador = []

        # Variable para controlar si se espera la entrada del jugador
        self.esperando_input = False

        # Ronda Actual
        self.ronda = 1

        # Indice para controlar la recursion en la reproducción de la secuencia
        self.indice_secuencia = 0

        # Crear la interfaz gráfica
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear una etiqueta para mostrar la ronda actual 
        self.label_ronda = tk.Label(self.ventana, text = f"Ronda {self.ronda}", 
                                                    font = ('Arial', 20))
        self.label_ronda.pack(pady = 20)

        # Crear un boton que muestra los colores durante la secuencia
        self.boton_mostrar = tk.Button(self.ventana, bg = 'grey', 
                                            width = 20, height = 5, state = 'disable')

        self.boton_mostrar.pack(pady = 10)

        # Crear un marco para los botones de colores
        self.frame_botones = tk.Frame(self.ventana) 
        self.frame_botones.pack(pady = 10)

        # Crear los botones de colores para que jugador ingrese la secuencia
        for color in self.colores:
            boton = tk.Button(
                self.frame_botones, 
                text = color, 
                bg = rgb_a_hex(colores_rgb[color]), 
                width = 10,
                height = 3, 
                command = lambda c = color: self.boton_clic(c)
            )
            boton.pack(side = 'left', padx = 5)

        # Crear el boton para empezar el juego
        self.boton_empezar = tk.Button(self.ventana, 
                                        text = 'Empezar juego',
                                        command = self.monstrar_secuencia)
        self.boton_empezar.pack(pady = 20)
    
    def monstrar_secuencia (self):
        # Inicializar varaiables para una nueva ronda
        self.esperando_input = False
        self.secuencia_jugador.clear()

        # Añadir un nuevo jugador aleatorio a la secuencia del juego
        self.secuencia_juego.append(random.choice(self.colores))

        # Actualizar la etiqueta de la ronda
        self.label_ronda.config(text = f"Ronda {self.ronda}")

        # Desactivar el boton empezar
        self.boton_empezar.config(state = 'disabled')

        # Iniciar la reproducción de la secuencia desde el primer indice
        self.indice_secuencia = 0
        self.reproducir_secuencia ()

    def reproducir_secuencia(self):
        # Si aun hay colores en la secuencia por mostrar
        if self.indice_secuencia < len(self.secuencia_juego):

            #Obtener el color actual
            color = self.secuencia_juego[self.indice_secuencia]

            # Mostrar el color actual en el boton
            self.boton_mostrar.config(bg = rgb_a_hex(colores_rgb[color]))

            # Esperar un segundo antes de apagar el color
            self.ventana.after(1000, self.apagar_color)

        else: 
            # Si se ha mostrado toda la secuencia, iniciar el turno del jugador
            self.boton_mostrar.config(bg = 'grey')
            self.iniciar_input_jugador()

    def apagar_color(self):
        # Apagar el color (volver el boton a color gris)
        self.boton_mostrar.config(bg = 'grey')

        # Incrementar el indice para pasar al siguiente color
        self.indice_secuencia += 1

        # Esperar 0.5 antes de mostrar el siguiente color
        self.ventana.after(500, self.reproducir_secuencia)

    def iniciar_input_jugador(self):
        # Iniciar que ahora se espera la entrada del jugador
        self.esperando_input = True 

        # Mostrar mensaje al jugador
        messagebox.showinfo("Tu turno", "Ahora es tu turno de repetir la secuencia.")

    def boton_clic(self, nombre_color):
        # Si se esta esperando la entrada del jugador
        if self.esperando_input: 

            # Añadir el color seleccionado por el jugador a su secuencia
            self.secuencia_jugador.append(nombre_color)

            # Obtener el indice actual
            indice_actual = len(self.secuencia_jugador) - 1

            # Verificar si el ultimo color ingresado es correcto
            if self.secuencia_jugador[indice_actual] != self.secuencia_juego[indice_actual]:
                
                # Si es incorrecto, mostrar mensaje y reiniciar el juego
                messagebox.showerror("ERROR", "¡Incorrecto! Hasta aqui llegaste Perro ")
                self.reiniciar_juego()
            
            elif len(self.secuencia_jugador) == len(self.secuencia_juego):
                # Si la secuencia esta completa y es correcta, avanzar a la siguiente ronda
                self.ronda += 1
                messagebox.showinfo("Correcto", "¡Correcto! Avanza a la siguiente ronda")

                # Esperar 1 segundo antes de iniciar la siguiente ronda
                self.ventana.after(1000, self.monstrar_secuencia)
            
    def reiniciar_juego(self):
        # Reiniciar las variables del juego
        self.secuencia_juego.clear()
        self.secuencia_jugador.clear()
        self.ronda = 1

        # Activar el boton de empezar
        self.boton_empezar.config(state = 'normal')

        # Actualizar la etiqueta de la ronda
        self.label_ronda.config(text = f"Ronda {self.ronda}")


if __name__ == "__main__":
    # Crear la ventana principal del tkinter
    ventana = tk.Tk()

    # Crear una instancia del juego 
    juego = SimonDice(ventana)

    # Iniciar el bucle principal de la ventana 
    ventana.mainloop()