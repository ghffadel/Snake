import pygame
import random

# screen
WIDTH = 500
WHITE = (255, 255, 255)
ROWS = 20

window = pygame.display.set_mode((WIDTH, WIDTH))

# colors
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)

# images
SNAKE_IMG = pygame.image.load('assets/Sprite-0002.png')
APPLE_IMG = pygame.image.load('assets/Sprite-0001.png')

# apple
apple = APPLE_IMG
apple_in_screen = False

# snake
snake = {
    'image': SNAKE_IMG,
    'direction': (1, 0),
    'position': ((WIDTH / 2), (WIDTH / 2))
}


def draw_snake(snake):
    distance = WIDTH // ROWS
    x, y = snake['position']

    window.blit(snake['image'], (x, y))

    if snake:
        center = distance // 2
        radius = 3
        circle1_center = (x * distance + center - radius, y * distance + 8)
        circle2_center = (x * distance + distance - 2 * radius, y * distance + 8)


def snake_controls():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('UP')
            if event.key == pygame.K_DOWN:
                print('DOWN')

            if event.key == pygame.K_LEFT:
                print('LEFT')
            if event.key == pygame.K_RIGHT:
                print('RIGHT')


game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    # draw
    if not apple_in_screen:
        window.blit(apple, (random.randint(0, WIDTH), random.randint(0, WIDTH)))
        apple_in_screen = True

    draw_snake(snake)

    # control snake
    snake_controls()

    # update
    pygame.display.flip()
    game_clock.tick(60)
