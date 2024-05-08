import sys
import pygame


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDHT, SCREEN_HEIGHT = 200, 100

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))

# Colors
WHITE = (250, 250, 250)

runnining = True

while runnining:
    for event in pygame.event.get():
        # Event listener
        if event.type == pygame.KEYDOWN:
            
            # Events
            if event.key == pygame.K_ESCAPE:
                runnining = False
            
            elif event.key == pygame.K_0:
                screen.fill((250, 0, 0))

            elif event.key == pygame.K_0:
                screen.fill("Purple")

            elif event.key == pygame.K_0:
                screen.fill("Purple")
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
