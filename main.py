import pygame, sys
from settings import *
from level import Level
import os
from coin import SCORE
from pygame import font

# Pygame setup
pygame.init()
# Screen width and screen height from settings
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'space', 'space.png')), (2000, 1000))
# Creates a level and passes level_map from settings
level = Level(level_map, screen)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(BACKGROUND_IMG, (0, 0))
    # Draw the score
    SCORE_FONT = pygame.font.SysFont('comicsans', 40)
    score_text = SCORE_FONT.render(f"Score: {SCORE}", 1, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # Update the display
    # pygame.display.flip()
    level.run()

    pygame.display.update()
    clock.tick(60)
