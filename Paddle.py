import pygame
from constants import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.x_pos = 200
        self.y_pos = 500
        self.width = 60
        self.height = 10
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X):
            self.x_pos -= 10
        elif keys[pygame.K_RIGHT] and self.rect.right <= (RES_WIDTH - (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X)):
            self.x_pos += 10
    
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
        self.movement()
        print(f'left: {self.rect.left}')
        print(f'x_pos: {self.x_pos}')
