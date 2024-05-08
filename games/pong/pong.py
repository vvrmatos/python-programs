# DOCUMENTATION
# File: pong.py
# Author: Victor Kolis
# Date: 05/07/2024 (MM/DD/YY)
# Description: Simple Pong Game is the classic back and forth, paddle hit,
#                       digital computer ping-pong game.
#                       press spacebar to start the game.
#                       press spacebar to release the ball.
# Controls:  ↑ and ↓ arrows (right paddle), w and s (left paddle)
# Theme song: Victor Kolis (No Copyright)
# Version: 1.0
# License: The unlicensed


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Mixer
pygame.mixer.init()
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.play(-1)

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
FONT_SIZE = 30
WHITE = (200, 200, 200)
GREEN = (144, 238, 144)
RED = (200, 0, 0)

# Audible
hit_sound = pygame.mixer.Sound("hit.mp3")

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
font = pygame.font.Font(None, FONT_SIZE)

# Paddle settings
paddle_speed = 10
left_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball settings
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x, ball_speed_y = 0, 0  # Start with no movement
initial_speed = 7

# Scores
left_score = 0
right_score = 0

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_x, ball_speed_y = 0, 0
    # Do not reset scores here to keep them persistent between rounds

def display_intro():
    intro = True
    title_font = pygame.font.Font(None, 48)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
        
        screen.fill((0, 0, 0))
        title_text = title_font.render("Welcome to Pong!", True, WHITE)
        instruction_text = font.render("Press Space to start", True, WHITE)
        author_text = font.render("by Victor Kolis", True, RED)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, 200))
        screen.blit(author_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 3, 250))
        pygame.display.flip()
        pygame.time.Clock().tick(15)

# Game loop
running = True
clock = pygame.time.Clock()

display_intro()  # Show the intro screen

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key is pygame.K_SPACE and ball_speed_x == 0 and ball_speed_y == 0:
                angle = random.uniform(0.5, 1)
                ball_speed_x = initial_speed * random.choice([-1, 1])
                ball_speed_y = initial_speed * angle * random.choice([-1, 1])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
        hit_sound.play()

    if ball.left <= 0:
        right_score += 1
        reset_ball()
    elif ball.right >= SCREEN_WIDTH:
        left_score += 1
        reset_ball()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, GREEN, ball)

    left_score_text = font.render(str(left_score), True, WHITE)
    right_score_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_text, (SCREEN_WIDTH // 4, 10))
    screen.blit(right_score_text, (3 * SCREEN_WIDTH // 4, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
