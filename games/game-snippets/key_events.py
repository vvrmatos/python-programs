import sys
import pygame


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDHT, SCREEN_HEIGHT = 200, 100

# Colors
R = 250
G = 250
B = 250

FULL_COLOR = (R, G, B)

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
screen.fill((FULL_COLOR))


runnining = True

while runnining:
    for event in pygame.event.get():
        # Event listener
        if event.type == pygame.KEYDOWN:
            
            # Events
            if event.key == pygame.K_ESCAPE:
                runnining = False
            
            elif event.key == pygame.K_DOWN and R > 0:
                R -= 10
                G -= 10
                B -= 10
                screen.fill((R, G, B))


            elif event.key == pygame.K_UP and R < 250:
                R += 10
                G += 10
                B += 10
                screen.fill((R, G, B))

    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()
