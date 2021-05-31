import pygame
import random
import time

pygame.init()

# screen
BLOCK = 15
SPEED = 15
WIDTH = 500

# colors
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)

# assets
APPLE_IMG = pygame.image.load('assets/Sprite-0001.png')
SNAKE_IMG = pygame.image.load('assets/Sprite-0002.png')
FONT = pygame.font.Font('assets/PressStart2P.ttf', 24)

# apple
apple = {
    'image': APPLE_IMG,
    'position': (random.randint(100, WIDTH - 100), random.randint(100, WIDTH - 100))
}

# snake
snake = {
    'direction': (0, BLOCK),
    'image': SNAKE_IMG,
    'length': 1,
    'positions': [(WIDTH // 2, WIDTH // 2)]
}
  
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Snake')

game_clock = pygame.time.Clock()
game_over = False

while not game_over:
    window.fill(COLOR_BLACK)

    # draw elements
    window.blit(apple['image'], apple['position'])

    # control snake
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake['direction'] = (0, -BLOCK)
            if event.key == pygame.K_DOWN:
                snake['direction'] = (0, BLOCK)
            if event.key == pygame.K_LEFT:
                snake['direction'] = (-BLOCK, 0)
            if event.key == pygame.K_RIGHT:
                snake['direction'] = (BLOCK, 0)

    current_x, current_y = snake['positions'][-1]
    direction_x, direction_y = snake['direction']
    new_x, new_y = (current_x + direction_x, current_y + direction_y)

    if not (-BLOCK <= new_x <= WIDTH + BLOCK and -BLOCK <= new_y <= WIDTH + BLOCK):
        game_over = True

    else:
        head = (new_x, new_y)
        snake['positions'].append(head)

        if len(snake['positions']) > snake['length']:
            del snake['positions'][0]
        
        for position in snake['positions'][:-1]:
            if position == head:
                game_over = True
                break

        for position in snake['positions']:
            window.blit(snake['image'], position)
        
        apple_x, apple_y = apple['position']

        if apple_x - (BLOCK + 10) <= head[0] <= apple_x + (BLOCK + 10) and \
            apple_y - (BLOCK + 10) <= head[1] <= apple_y + (BLOCK + 10):
            apple['position'] = (random.randint(0, WIDTH), random.randint(0, WIDTH))
            snake['length'] += 1

    # update
    pygame.display.update()
    game_clock.tick(SPEED)

game_over_message = FONT.render('Game Over', 1, COLOR_WHITE)
window.blit(game_over_message, (WIDTH // 2 - 100, WIDTH // 2 - 50))
score_message = FONT.render('Your score: %d' % (snake['length'] - 1), 1, COLOR_WHITE)
window.blit(score_message, (WIDTH // 2 - 150, WIDTH // 2))
pygame.display.update()
time.sleep(2)