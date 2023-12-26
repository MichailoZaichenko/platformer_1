import pygame
import os
SPIKES_IMG = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'spikes', 'spike.png')), (70, 70))
spike_mask = pygame.mask.from_surface(SPIKES_IMG)
# Class used to create tiles in game.
class Spike(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        # self.image = pygame.Surface((size, size))
        self.image = SPIKES_IMG
        self.rect = self.image.get_rect(topleft = pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x_shift):
        self.rect.x += x_shift