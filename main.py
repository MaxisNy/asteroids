# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

clock = pygame.time.Clock()
dt = 0

def main():
    global dt
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updatable, drawable)
    while True:
        screen.fill('black')
        # update all player objects 
        for obj in Player.containers[0]:
            obj.update(dt)
        # draw all player obejcts
        for obj in Player.containers[1]:
            obj.draw(screen)
        # screen render function
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
