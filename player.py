from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):

    cooldown_timer = 0

    def __init__(self, x, y) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    def triangle(self):
        forward = pygame.math.Vector2(0, 1).rotate(self.rotation)
        right = pygame.math.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, 'cyan', self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        # update shooting cooldown timer
        Player.cooldown_timer -= dt
        if Player.cooldown_timer < 0:
            Player.cooldown_timer = 0

        keys = pygame.key.get_pressed()
        # inverse rotation if moving backwards
        if keys[pygame.K_s]:
            self.move(dt * -1)
            if keys[pygame.K_a]:
                self.rotate(dt)
            if keys[pygame.K_d]:
                self.rotate(dt * -1)
        else:
            if keys[pygame.K_a]:
                self.rotate(dt * -1)
            if keys[pygame.K_d]:
                self.rotate(dt)
            if keys[pygame.K_w]:
                self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        # screen wrapping
        vertical_center_offset = abs((SCREEN_WIDTH // 2) - self.position[0]) 
        
        # top / bottom wrapping       
        if self.position[1] < 0:    # top
            self.position[1] = SCREEN_HEIGHT
            if self.position[0] > SCREEN_WIDTH // 2:
                self.position[0] -= 2 * vertical_center_offset
            else:
                self.position[0] += 2 * vertical_center_offset
        if self.position[1] > SCREEN_HEIGHT:    # bottom
            self.position[1] = 0
            if self.position[0] > SCREEN_WIDTH // 2:
                self.position[0] -= 2 * vertical_center_offset
            else:
                self.position[0] += 2 * vertical_center_offset
        
        # left / right wrapping
        if self.position[0] < 0:    # left
            self.position[0] = SCREEN_WIDTH
        if self.position[0] > SCREEN_WIDTH: # right
            self.position[0] = 0

    def shoot(self):
        if Player.cooldown_timer == 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.math.Vector2.rotate(pygame.math.Vector2(0, 1), self.rotation) * PLAYER_SHOOT_SPEED
            Player.cooldown_timer = PLAYER_SHOOT_COOLDOWN