import pygame
from sys import exit

from Paddle import Paddle
from constants import *
from Ball import Ball
from Brick import Brick


class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RES_WIDTH,RES_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_border = pygame.Rect(GAME_BORDER_PADDING_X, GAME_BORDER_PADDING_Y, GAME_BORDER_WIDTH, GAME_BORDER_HEIGHT)
        self.play_ball = False

        # Paddle
        self.paddle = pygame.sprite.GroupSingle()
        self.paddle.add(Paddle())

        # Ball
        self.ball = pygame.sprite.GroupSingle()
        self.ball.add(Ball(200, 531))

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]    
        self.brick=self.brick_factory(self.map)

    def brick_factory(self, map):
        brick_group = pygame.sprite.Group()

        for row_index, row in enumerate(map, start=1):
            for brick_index, brick in enumerate(row, start=0):
                print(f'row_index:{row_index}, brick_index: {brick_index}, brick: {brick}')
                brick_group.add(Brick(GAME_BORDER_PADDING_X+GAME_BORDER_THICKNESS+(brick_index*59),(100+(row_index*17))))
        
        return brick_group
   
    def paddle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.sprite.rect.left >= (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X):
            self.paddle.sprite.x_pos -= 8
        elif keys[pygame.K_RIGHT] and self.paddle.sprite.rect.right <= (RES_WIDTH - (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X)):
            self.paddle.sprite.x_pos += 8

    def ball_bouncing(self):
        if self.play_ball:
        #Colission with paddle
            collide_tolerance = 10
            if pygame.sprite.collide_rect(self.paddle.sprite,self.ball.sprite): 
                if abs(self.paddle.sprite.rect.top - self.ball.sprite.rect.bottom) < collide_tolerance:
                    # print(f'Top: {self.paddle.sprite.rect.top}, Bottom:{self.ball.sprite.rect.bottom}')
                    self.ball.sprite.y_velocity *= -1
                    # print(f'{self.ball.sprite.y_velocity}')

            #Colission with border
            if self.ball.sprite.rect.right >= RES_WIDTH-GAME_BORDER_PADDING_X:
                self.ball.sprite.x_velocity *= -1
            if self.ball.sprite.rect.bottom >= RES_HEIGHT-GAME_BORDER_PADDING_Y:
                # self.ball.sprite.y_velocity *= -1
                self.running = False
            if self.ball.sprite.rect.left <= GAME_BORDER_PADDING_X:
                self.ball.sprite.x_velocity *= -1
            if self.ball.sprite.rect.top <= GAME_BORDER_PADDING_Y:
                self.ball.sprite.y_velocity *= -1

            self.ball.sprite.x_pos += self.ball.sprite.x_velocity
            self.ball.sprite.y_pos += self.ball.sprite.y_velocity
        else:
            # Ball moves with paddle untill spacebar is pressed
            self.ball.sprite.x_pos = self.paddle.sprite.x_pos
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.play_ball = True
                

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.screen.fill('blue')
            pygame.draw.rect(self.screen, (255,255,255),self.game_border, GAME_BORDER_THICKNESS, 10)

            # Paddle
            self.paddle.draw(self.screen)
            self.paddle_movement()
            self.paddle.update()

            self.ball_bouncing()
            # Ball
            self.ball.draw(self.screen)
            self.ball.update()

            # Brick
            self.brick.draw(self.screen)
            self.brick.update()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
        exit()
    
Game().run()

