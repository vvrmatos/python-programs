# This program makes the user interact with the keyboard
# And as soon as any of the (esc, spacebar, return, k) are pressed
# The program dies/stops

import sys
import pygame


pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
KEYS = {pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN, pygame.K_k}

# Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((100, 45, 40))

running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in KEYS:
                running = False

    pygame.display.flip()        

pygame.quit()
sys.exit()
