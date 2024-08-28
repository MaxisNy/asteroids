# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField

clock = pygame.time.Clock()
dt = 0

def main():
    global dt
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    # player object handlingf
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # asteroid object handling
    Asteroid.containers = (updatable, drawable, asteroids_group)

    # asteroid field handling
    AsteroidField.containers = (updatable)
    AsteroidField()

    while True:
        screen.fill('black')
        # update all updatable objects 
        for obj in updatable:
            obj.update(dt)
        # draw all drawable obejcts
        for obj in drawable:
            obj.draw(screen)
        # check for collisions with
        for asteroid in asteroids_group:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()
        # screen render function
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
