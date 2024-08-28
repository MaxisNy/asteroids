from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius != ASTEROID_MIN_RADIUS:
            rand_angle = random.uniform(20,50)
            new_asteroid_velocity1, new_asteroid_velocity2 = \
                pygame.Vector2.rotate(self.velocity, rand_angle), pygame.Vector2.rotate(self.velocity, rand_angle * -1)
            new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid1.velocity, new_asteroid2.velocity = \
                new_asteroid_velocity1 * 1.2, new_asteroid_velocity2 * 1.2
            
