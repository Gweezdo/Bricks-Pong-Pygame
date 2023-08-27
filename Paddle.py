import pygame
from constants import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.x_pos = 200
        self.y_pos = 540
        self.width = 60
        self.height = 10
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((0,255,0))
        self.image.set_colorkey((0,255,0))

        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width,self.height), width=0, border_top_left_radius=5, border_top_right_radius=5, border_bottom_left_radius=1, border_bottom_right_radius=1)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
    
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))

        
