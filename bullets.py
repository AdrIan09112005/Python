import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = (255, 140, 0) # Color naranja para las bullets
        self.velocity = -10 # La bullet se mueve hacia arriba

    def move(self):
        self.y += self.velocity # Movimiento hacia arriba

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)