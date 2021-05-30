import pygame

RED = (255, 0, 0)
ROWS = 20
WIDTH = 500
WHITE = (255, 255, 255)

def draw_snake(head):
    distance = WIDTH // ROWS
    x, y = snake['position']

    pygame.draw.rect(window, snake['color'], (x * distance + 1, y * distance + 1, distance - 2, distance - 2))

    if head:
        center = distance // 2
        radius = 3
        circle1_center = (x * distance + center - radius, y * distance + 8)
        circle2_center = (x * distance + distance - 2 * radius, y * distance + 8)
        pygame.draw.circle(window, WHITE, circle1_center, radius)
        pygame.draw.circle(window, WHITE, circle2_center, radius)


window = pygame.display.set_mode((WIDTH, WIDTH))
snake = {
    'color': RED,
    'direction': (1, 0),
    'position': (1, 0)
}