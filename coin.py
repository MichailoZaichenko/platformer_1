import pygame
import os
import math
import time

start_time = time.time()
current_time = time.time()
elapsed_time = current_time - start_time
SCORE = 0
COINS = []
for i in range(4):
    coin = pygame.transform.scale(pygame.image.load(os.path.join('graphics', 'coins', 'gold', '{}.png'.format(i+1))), (70, 70))
    COINS.append(coin)

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.images = COINS[:]
        self.image = self.images.pop(0)
        self.rect = self.image.get_rect(topleft = pos)
        self.angle = 0
        self.rotation_speed = 1 # degrees per frame
        self.current_time = time.time()

    def update(self, x_shift):
        self.rect.x += x_shift
        current_time = time.time()
        elapsed_time = current_time - self.current_time
        if elapsed_time > 0.4: # 100 ms delay
            self.current_time = current_time
            if self.images:
                self.image = self.images.pop(0)
            else:
                self.images = COINS[:]
                self.image = self.images.pop(0)

    def kill(self):
        pygame.sprite.Sprite.kill(self)

    def collect(self):
        self.kill() # Remove the coin sprite from the sprite group
        # Add 1 to the player's score (assuming a variable 'score' exists)
        global SCORE 
        SCORE += 1