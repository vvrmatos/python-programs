import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Rectangle details
rect_x, rect_y = 300, 220  # Initial position
rect_width, rect_height = 60, 40
rect_speed = 5  # Movement speed per frame

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Prevent the rectangle from going out of the window
    rect_x = max(0, min(SCREEN_WIDTH - rect_width, rect_x))
    rect_y = max(0, min(SCREEN_HEIGHT - rect_height, rect_y))

    # Fill the screen with white to clear old frames
    screen.fill(WHITE)
    
    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
