import pygame
from player import Player
from bullets import Bullet
from enemy import Enemy
import random

# Incializar Pygame
pygame.init()

# Configurar la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GALATSIA")

# Colores
WHITE = (255, 255, 255)

# Inicalizar el jugador
player = Player(WIDTH//2, HEIGHT-50)
bullets = [] # Nueva lista para almacenar las balas
enemies = [] # Lista para almacenar todo los enemigos generados

# Contador para controlar la generacion de enemigos
enemy_spawn_counter = 0 # Contador que ayudara a añadir enemigos periodicamente

# Bucle principal del juego 
running = True 

while running: 
    screen.fill(WHITE) # Fondo Blanco

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Crear una bala nueva al presionar la barra espaciadora
                bullets.append(Bullet(player.x + player.width // 2, player.y))


     # Generar enemigo periodicamente
    enemy_spawn_counter += 1  #Incrementa el contador en cada cuadro del juego

    if enemy_spawn_counter >= 60: # Cuando el contador llega a 60 (aprox 2 seg)
    #Incrementa el contador en cada cuadro del juego
        enemies.append(Enemy())
        enemy_spawn_counter = 0

    # Actualizar la posicion del jugador
    player.move()
    player.draw(screen)

    # Actualizar y dibujar cada bullet
    for bullet in bullets[:]: # Nueva interracion sobre los bullets
        bullet.move() # Movimiento de cada bala 
        bullet.draw(screen) # Dibujo de cada bullet en la pantalla
        if bullet.y < 0: # Eliminar bullet que sale de la pantalla 
            bullets.remove(bullet)
    
    # Actualizar y Dibujar cada enemigo 
    for enemy in enemies[:]:
        enemy.move()
        enemy.draw(screen)
        # Verificar colisiones
        for bullet in bullets[:]:
            if enemy.collides_with(bullet):
                bullets.remove(bullet)
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)

    pygame.display.flip()
    pygame.time.delay(30) # Suavizar el movimiento del jugador

pygame.quit()