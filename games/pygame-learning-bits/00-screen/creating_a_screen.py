import sys
import pygame

pygame.init() # Initialize all of pygame's modules

screen = pygame.display.set_mode((200, 200)) # You set the display with set_mode giving it a tuple, Width, Height

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
