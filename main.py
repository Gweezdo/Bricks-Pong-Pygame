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
        self.game_border = pygame.Rect(50, 50, RES_WIDTH-100, RES_HEIGHT-100)

        # Paddle
        # self.paddle = pygame.sprite.GroupSingle()
        # self.paddle.add(Paddle())

        # Ball
        self.ball = pygame.sprite.Group()
        sprite_ball = Ball()
        self.ball.add(sprite_ball)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill('purple')
            pygame.draw.rect(self.screen, (255,255,255),self.game_border, GAME_BORDER_THICKNESS, 10)

            # Paddle
            # self.paddle.draw(self.screen)
            # self.paddle.update()

            # Ball
            self.ball.draw(self.screen)
            self.ball.update()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
        exit()
    
Game().run()

