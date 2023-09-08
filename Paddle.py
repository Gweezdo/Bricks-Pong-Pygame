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
        self.speed = 600

        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, self.width,self.height), width=0, border_top_left_radius=5, border_top_right_radius=5, border_bottom_left_radius=1, border_bottom_right_radius=1)
        self.rect = self.image.get_rect(topleft = (self.x_pos, self.y_pos))
        self.pos = pygame.math.Vector2(self.rect.topleft)
        # self.rect_pos = self.rect.x
        self.rect_old = self.rect.copy()

    def move(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X):
            self.pos.x -= self.speed * dt
            self.x_pos = round(self.pos.x)
            print(self.x_pos)
        if keys[pygame.K_RIGHT] and self.rect.right <= (RES_WIDTH - (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X)):
            self.pos.x += self.speed * dt
            self.x_pos = round(self.pos.x)
            print(self.x_pos)
    
    def update(self, dt):
        self.rect_old = self.rect.copy()
        self.move(dt)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
        # self.rect_pos = self.rect.x

        
