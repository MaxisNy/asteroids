# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

clock = pygame.time.Clock()
dt = 0
score = 0
play_game = True
game_over = True

def display_gui(screen, hp):
    my_font = pygame.font.SysFont("Arcade Classic", 25)
    user_score = my_font.render(f"YOUR SCORE: {score}", 1, 'yellow')
    screen.blit(user_score, (SCREEN_WIDTH - 150, 20))

    user_health = my_font.render(f"HEALTH: {hp}", 1, 'yellow')
    screen.blit(user_health, (SCREEN_WIDTH - 250, 20))

def display_game_over(screen):
    screen.fill('black')
    my_font = pygame.font.SysFont("Arcade Classic", 25)
    go_msg1 = my_font.render("Game Over :(", 1, 'yellow')
    screen.blit(go_msg1, (SCREEN_WIDTH // 2 - 65, SCREEN_HEIGHT // 2 - 20))
    go_msg2 = my_font.render("Continue? Y / N", 1, 'yellow')
    screen.blit(go_msg2, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 20))

def main():
    global dt
    global score
    global play_game
    global game_over
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # player object handling
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # shot object handling
    Shot.containers = (updatable, drawable, shots_group)
    # shot = Shot(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # asteroid object handling
    Asteroid.containers = (updatable, drawable, asteroids_group)

    # asteroid field handling
    AsteroidField.containers = (updatable)
    AsteroidField()

    while play_game:
        screen.fill('black')
        display_gui(screen, player.health)

        # update all updatable objects
        for obj in updatable:
            obj.update(dt)
        # draw all drawable obejcts
        for obj in drawable:
            obj.draw(screen)
        # check for destroyed asteroids
        for asteroid in asteroids_group:
            for shot in shots_group:
                if asteroid.check_collision(shot):
                    if not asteroid.split():
                        score += 1
                    shot.kill()
        # check for player collision with asteroids
        if not player.is_invincible():
            for asteroid in asteroids_group:
                if player.check_collision(asteroid):
                    if player.health == 1:  # last health
                        # game over logic
                        game_over = True
                        while game_over:
                            display_game_over(screen)
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_n:
                                        game_over = False
                                        play_game = False
                                        break
                                    if event.key == pygame.K_y:
                                        game_over = False
                                        player.reset()
                                        score = 0
                    else:           
                        player.take_damage()

        # screen render function
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()
