import pygame
from sys import exit

from Paddle import Paddle
from constants import *
from Ball import Ball


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RES_WIDTH,RES_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_border = pygame.Rect(GAME_BORDER_PADDING_X, GAME_BORDER_PADDING_Y, GAME_BORDER_WIDTH, GAME_BORDER_HEIGHT)

        # Paddle
        self.paddle = pygame.sprite.GroupSingle()
        self.paddle.add(Paddle())

        # Ball
        self.ball = pygame.sprite.GroupSingle()
        self.ball.add(Ball())

        self.map = [[1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1]]    
        self.bricks = self.brick_factory(self.map)

   

    def paddle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.sprite.rect.left >= (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X):
            self.paddle.sprite.x_pos -= 8
        elif keys[pygame.K_RIGHT] and self.paddle.sprite.rect.right <= (RES_WIDTH - (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X)):
            self.paddle.sprite.x_pos += 8

    def ball_bouncing(self):

        collide_tolerance = 10
        if pygame.sprite.collide_rect(self.paddle.sprite,self.ball.sprite): 
            if abs(self.paddle.sprite.rect.top - self.ball.sprite.rect.bottom) < collide_tolerance:
                print(f'Top: {self.paddle.sprite.rect.top}, Bottom:{self.ball.sprite.rect.bottom}')
                self.ball.sprite.y_velocity *= -1
                print(f'{self.ball.sprite.y_velocity}')
                # print('collide')
        
        colliding_sprites = pygame.sprite.spritecollide(self.ball.sprite, all_sprites, False)
    
        if colliding_sprites:
            print("Collision detected with:", [sprite for sprite in colliding_sprites])

        if self.ball.sprite.rect.right >= RES_WIDTH-GAME_BORDER_PADDING_X:
            self.ball.sprite.x_velocity *= -1
        if self.ball.sprite.rect.bottom >= RES_HEIGHT-GAME_BORDER_PADDING_Y:
            self.ball.sprite.y_velocity *= -1
        if self.ball.sprite.rect.left <= GAME_BORDER_PADDING_X:
            self.ball.sprite.x_velocity *= -1
        if self.ball.sprite.rect.top <= GAME_BORDER_PADDING_Y:
            self.ball.sprite.y_velocity *= -1

        self.ball.sprite.x_pos += self.ball.sprite.x_velocity
        self.ball.sprite.y_pos += self.ball.sprite.y_velocity
        

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill('purple')
            pygame.draw.rect(self.screen, (255,255,255),self.game_border, GAME_BORDER_THICKNESS, 10)

            self.ball_bouncing()

            # Paddle
            self.paddle.draw(self.screen)
            self.paddle_movement()
            self.paddle.update()

            # Ball
            self.ball.draw(self.screen)
            self.ball.update()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
        exit()
    
Game().run()

