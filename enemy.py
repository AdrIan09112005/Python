import pygame
import random

class Enemy: 
    def __init__(self):
        self.x = random.randint(0, 750)
        self.y = random.randint(-100, -40)
        self.width = 50
        self.height = 40
        self.color = (255, 0, 0) # Color del enemigo
        self.velocity = random.randint(1, 3)
        self.health = 3

    def move(self):
        self.y += self.velocity
        if self.y > 600: # Si el enemigo cruza el limite inferior de la pantalla
            self.y = random.randint(1, 3)
            self.x = random.randint(0, 750)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collides_with(self, bullet):
        # Comprueba si la bala esta dentro del ancho y alto del enemigo
        return (
            self.x < bullet.x < self.x + self.width and
            self.y < bullet.y < self.y + self.height
        )