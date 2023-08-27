import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.width = 10
        self.height = 10
        self.x_velocity = 5
        self.y_velocity = 5
        self.x_pos = x_pos #200
        self.y_pos = y_pos #530
        self.radius = self.width/2
        self.color = (255, 255, 255)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))

        # Note the position of the circle is relative to the top left cnr of the surface you're targeting 
        pygame.draw.circle(self.image, self.color, (self.width/2, self.height/2), self.radius)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
        # self.rect.center = (self.x_pos, self.y_pos)
    
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
        # self.bouncing()
        # print(f'y_pos: {self.y_pos}')
    
        
