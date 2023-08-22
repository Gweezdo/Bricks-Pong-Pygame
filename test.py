import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Drawing Example")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create a sprite class
class CircleSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Create an image for the sprite
        self.image = pygame.Surface((50, 50))
        self.image.fill((255,0,0))  # Fill the image with white initially
        
        # Draw a circle on the image
        pygame.draw.circle(self.image, black, (25, 25), 25)  # Center at (25, 25), radius 25
        
        # Get the rectangle of the image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Center the sprite
        
# Create a sprite group
all_sprites = pygame.sprite.Group()
circle_sprite = CircleSprite()
all_sprites.add(circle_sprite)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Clear the screen
    screen.fill('purple')
    
    # Update and draw sprites
    all_sprites.update()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
