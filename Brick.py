import pygame

from constants import *

class Brick(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = (247, 167, 62)#color
        self.strength = 1 #strength #int how many times to hit before break

        self.width = 57
        self.height = 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))

    def update(self):
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))
    
    # @classmethod
    # def brick_factory(cls, row):

