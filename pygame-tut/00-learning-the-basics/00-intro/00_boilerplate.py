import sys
import pygame

# Initializing all of pygame modules
pygame.init()


# Creating the screen, with a tuple (WIDTH, HEIGHT)
screen = pygame.display.set_mode((300, 300))

runninig = True

while runninig:
    # Listening for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninig = False

pygame.quit()
sys.exit()
