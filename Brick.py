import pygame

from constants import *

class Brick(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos, color, strength):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.strength = strength #int how many times to hit before break

        self.width = 98
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)

        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))


    def update(self):
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
    
    @classmethod
    def brick_factory(cls, map):

