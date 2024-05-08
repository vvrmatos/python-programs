import sys
import pygame

# Initialize all imported pygame modules
pygame.init()

# Constants
SCREEN_WIDTH,  SCREEN_HEIGHT = 800, 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
