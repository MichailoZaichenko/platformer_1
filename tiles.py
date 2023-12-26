import pygame
import os
STONE = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'space', 'stone.jpg')), (70, 70))
# Class used to create tiles in game.
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # Size is the same since we are creating square tiles.
        self.image = pygame.Surface((size, size))
        # self.image.fill('grey')
        self.image.blit(STONE, (0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift