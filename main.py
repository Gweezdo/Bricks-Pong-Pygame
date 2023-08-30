import pygame
from sys import exit

from Paddle import Paddle
from constants import *
from Ball import Ball
from Brick import Brick

from random import choice

class Game():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RES_WIDTH,RES_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_border = pygame.Rect(GAME_BORDER_PADDING_X, GAME_BORDER_PADDING_Y, GAME_BORDER_WIDTH, GAME_BORDER_HEIGHT)
        self.play_ball = False
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        self.lives = 3
        self.msg_choice = ""

        # Paddle
        self.paddle = pygame.sprite.GroupSingle()
        self.paddle.add(Paddle())

        # Ball
        self.ball = pygame.sprite.GroupSingle()
        self.ball.add(Ball(200, 531))

        self.map = [[1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,0,0,0,0,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1]]    
        self.bricks=self.brick_factory(self.map)

    def display_lives(self):
        text_surf = self.font.render(f"Remaining Lives: {self.lives}", True, (255,255,255))
        text_rect = text_surf.get_rect(topleft = (550,15))
        self.screen.blit(text_surf, text_rect)
    
    def display_kill_msg(self, msg):
        text_surf = self.font.render(f"{msg}", True, (255,255,255))
        text_rect = text_surf.get_rect(center = (RES_WIDTH/2,RES_HEIGHT/2))
        self.screen.blit(text_surf, text_rect)

    def brick_factory(self, map):
        brick_group = pygame.sprite.Group()

        for row_index, row in enumerate(map, start=1):
            for brick_index, brick in enumerate(row, start=0):
                if brick == 1:
                    # print(f'row_index:{row_index}, brick_index: {brick_index}, brick: {brick}')
                    brick_group.add(Brick(GAME_BORDER_PADDING_X+GAME_BORDER_THICKNESS+(brick_index*59),(100+(row_index*17))))
        
        return brick_group
   
    def paddle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.sprite.rect.left >= (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X):
            self.paddle.sprite.x_pos -= 6
        elif keys[pygame.K_RIGHT] and self.paddle.sprite.rect.right <= (RES_WIDTH - (GAME_BORDER_THICKNESS + GAME_BORDER_PADDING_X)):
            self.paddle.sprite.x_pos += 6 

    def ball_bouncing(self):
        if self.play_ball:

            collide_tolerance = 10
            #Colission with bricks
            collide_list = pygame.sprite.spritecollide(self.ball.sprite, self.bricks, True)
            if collide_list:
                for brick in collide_list:
                    if (abs(self.ball.sprite.rect.top - brick.rect.bottom) < collide_tolerance) or (abs(self.ball.sprite.rect.bottom - brick.rect.top) < collide_tolerance):
                        print('colission')
                        self.ball.sprite.y_velocity *= -1
                    if (abs(self.ball.sprite.rect.left - brick.rect.right) < collide_tolerance) or (abs(self.ball.sprite.rect.right - brick.rect.left) < collide_tolerance):
                        print('colission')
                        self.ball.sprite.x_velocity *= -1

            #Colission with paddle
            if pygame.sprite.collide_rect(self.paddle.sprite,self.ball.sprite): 
                if abs(self.paddle.sprite.rect.top - self.ball.sprite.rect.bottom) < collide_tolerance:
                    # print(f'Top: {self.paddle.sprite.rect.top}, Bottom:{self.ball.sprite.rect.bottom}')
                    self.ball.sprite.y_velocity *= -1
                    # print(f'{self.ball.sprite.y_velocity}')

            #Colission with border
            if self.ball.sprite.rect.right >= RES_WIDTH-GAME_BORDER_PADDING_X:
                self.ball.sprite.x_velocity *= -1
            if self.ball.sprite.rect.bottom >= RES_HEIGHT-GAME_BORDER_PADDING_Y:
                self.ball.sprite.y_velocity *= -1
                self.lives -= 1
                self.play_ball = False
                self.msg_choice = choice(['You stink','Do you even game Bro?'])
                
                # self.running = False
            if self.ball.sprite.rect.left <= GAME_BORDER_PADDING_X:
                self.ball.sprite.x_velocity *= -1
            if self.ball.sprite.rect.top <= GAME_BORDER_PADDING_Y:
                self.ball.sprite.y_velocity *= -1

            self.ball.sprite.x_pos += self.ball.sprite.x_velocity
            self.ball.sprite.y_pos += self.ball.sprite.y_velocity
        else:
            # Ball moves with paddle untill spacebar is pressed
            self.ball.sprite.x_pos = self.paddle.sprite.x_pos
            self.ball.sprite.y_pos = self.paddle.sprite.y_pos - self.paddle.sprite.height
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.play_ball = True
                

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #Do logical updates here
            self.paddle.update()
            self.ball_bouncing()
            self.ball.update()
            self.bricks.update()
            self.paddle_movement()

            #Fill screen with solid colour
            self.screen.fill('blue')
            
            #Render graphics here
            pygame.draw.rect(self.screen, (255,255,255),self.game_border, GAME_BORDER_THICKNESS, 10)
            pygame.draw.rect(self.screen, (255,0,0),self.ball.sprite.rect_old)

            self.display_lives()
            self.paddle.draw(self.screen) 
            self.ball.draw(self.screen)
            self.bricks.draw(self.screen)
            if self.lives < 0:
                self.display_kill_msg("GAME OVER!!!")
                self.lives = 0
            elif self.play_ball == False and (self.lives < 3 and self.lives >= 0):
                self.display_kill_msg(self.msg_choice)


            pygame.display.flip()
            self.clock.tick(60)
            
        pygame.quit()
        exit()
    
Game().run()

