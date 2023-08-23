import pygame
from constants import *

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.x_velocity = 3
        self.y_velocity = 5
        self.x_pos = 200
        self.y_pos = 150
        self.radius = self.width/2
        self.color = (255, 255, 255)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))

        # Note the position of the circle is relative to the top left cnr of the surface you're targeting 
        pygame.draw.circle(self.image, self.color, (self.width/2, self.height/2), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)

    def bouncing(self):
        if self.rect.right >= RES_WIDTH-GAME_BORDER_PADDING_X:
            self.x_velocity *= -1
        if self.rect.bottom >= RES_HEIGHT-GAME_BORDER_PADDING_Y:
            self.y_velocity *= -1
        if self.rect.left <= GAME_BORDER_PADDING_X:
            self.x_velocity *= -1
        if self.rect.top <= GAME_BORDER_PADDING_Y:
            self.y_velocity *= -1
        self.x_pos += self.x_velocity
        self.y_pos += self.y_velocity



    
    def update(self):
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.bouncing()
        
    
        
