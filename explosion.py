from circleshape import *
from constants import *
import pygame

class Explosion(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 20)

    def draw(self, screen):
        pygame.draw.circle(screen, 'red', self.position, self.radius, 1)
        
    def update(self, dt):
        self.radius = self.radius + dt * 50
        if self.radius > 75:
            self.kill()