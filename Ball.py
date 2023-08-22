import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        # self.screen = screen
        self.width = 10
        self.height = 10
        self.x_velocity = 3
        self.y_velocity = 5
        self.center_pos = (200,150)
        self.radius = self.width/2

        self.color = (0, 255, 0)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))
        self.rect = self.image.get_rect(center = (self.center_pos[0], self.center_pos[1]))

    def bouncing(self):
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity

    
    def update(self, screen):
        pygame.draw.circle(screen, self.color, self.center_pos, self.radius, 0)
        # self.rect = self.image.get_rect(center = (self.center_pos[0], self.center_pos[1]))
        
        # pygame.draw.circle(self.image,self.color,self.center_pos,self.radius, 0)
    
        
