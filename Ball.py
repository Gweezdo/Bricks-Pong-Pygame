import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 100
        self.x_velocity = 3
        self.y_velocity = 5
        self.x_pos = 200
        self.y_pos = 150
        self.radius = self.width/2
        self.color = (0, 0, 0)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        # self.image.set_colorkey((255,0,0))
        pygame.draw.circle(self.image, self.color, (0, 0), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def bouncing(self):
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity

    
    # def update(self, screen):
    #     pygame.draw.circle(self.image, self.color, (self.x_pos, self.y_pos), self.radius, 0)
    #     self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
    #     self.bouncing()
        
        # pygame.draw.circle(self.image,self.color,self.center_pos,self.radius, 0)
    
        
