import pygame
from sys import exit

RES_WIDTH = 800
RES_HEIGHT = 600

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.x_pos = 200
        self.y_pos = 500
        self.width = 60
        self.height = 10
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 51:
            self.x_pos -= 10
        elif keys[pygame.K_RIGHT] and self.rect.right <= (RES_WIDTH - 51):
            self.x_pos += 10
    
    def update(self):
        self.rect = self.image.get_rect(midbottom = (self.x_pos, self.y_pos))
        self.movement()
        print(f'left: {self.rect.left}')
        print(f'x_pos: {self.x_pos}')

pygame.init()
screen = pygame.display.set_mode((RES_WIDTH,RES_HEIGHT))
clock = pygame.time.Clock()
running = True
paddle = pygame.sprite.GroupSingle()
paddle.add(Paddle())

game_border = pygame.Rect(50, 50, RES_WIDTH-100, RES_HEIGHT-100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill('purple')
    pygame.draw.rect(screen, (255,255,255),game_border, 3, 10)
    paddle.draw(screen)
    paddle.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
    

