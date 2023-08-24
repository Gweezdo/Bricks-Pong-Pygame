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
    
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
