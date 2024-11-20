import pygame

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.color = (0, 0, 255) # Color de la nave 
        self.velocity = 10

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x - self.velocity > 0: 
            self.x -= self.velocity
        if keys[pygame.K_d] and self.x + self.velocity < 800 - self.width: 
            self.x += self.velocity
        if keys[pygame.K_w] and self.y - self.velocity > 0: 
            self.y -= self.velocity
        if keys[pygame.K_s] and self.y + self.velocity < 600 - self.height: 
            self.y += self.velocity
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))