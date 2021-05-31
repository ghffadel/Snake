import pygame
import random
import time
import menuv1
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
BACKGROUND_IMG = pygame.image.load("assets/background.png")
APPLE_IMG = pygame.image.load("assets/apple.png")
SNAKE_IMG = pygame.image.load("assets/snake.png")
FONT = pygame.font.Font("assets/PressStart2P.ttf", 24)

# sound effects

# https://freesound.org/people/Joao_Janz/sounds/482653/
point_sound_effect = pygame.mixer.Sound("assets/point.wav")

# https://freesound.org/people/myfox14/sounds/382310/
game_over_sound_effect = pygame.mixer.Sound("assets/game_over.wav")

score = 0

# apple
apple = {
    "image": APPLE_IMG,
    "position": (
        random.randint(100, WIDTH - 100),
        random.randint(100, WIDTH - 100),
    ),
}

# snake
snake = {
    "direction": (0, -BLOCK),
    "image": SNAKE_IMG,
    "length": 1,
    "positions": [(WIDTH // 2, WIDTH // 2)],
}

window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake")

game_clock = pygame.time.Clock()
game_over = False
menu = True
pause_menu = False
credits_menu = False

#background image
main_menu = pygame.image.load("assets/snake_menu.jpg")
#background1 = pygame.image.load("startscreen.png")
pause_menu_image = pygame.image.load("assets/pause.jpg")
credits_menu_image = pygame.image.load("assets/credits_snakev2.jpg")

click = False

while not game_over:
    menuv1.run_menu()


    window.blit(BACKGROUND_IMG, (0, 0))

    # draw elements
    window.blit(apple["image"], apple["position"])

    # control snake
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake["direction"] = (0, -BLOCK)
            if event.key == pygame.K_DOWN:
                snake["direction"] = (0, BLOCK)
            if event.key == pygame.K_LEFT:
                snake["direction"] = (-BLOCK, 0)
            if event.key == pygame.K_RIGHT:
                snake["direction"] = (BLOCK, 0)
            if event.key == pygame.K_p:
                menuv1.pause()

    current_x, current_y = snake["positions"][-1]
    direction_x, direction_y = snake["direction"]
    new_x, new_y = (current_x + direction_x, current_y + direction_y)

    if not (
        -BLOCK <= new_x <= WIDTH + BLOCK and -BLOCK <= new_y <= WIDTH + BLOCK
    ):
        game_over = True

    else:
        head = (new_x, new_y)
        snake["positions"].append(head)

        if len(snake["positions"]) > snake["length"]:
            del snake["positions"][0]

        for position in snake["positions"][:-1]:
            if position == head:
                game_over = True
                break

        for position in snake["positions"]:
            window.blit(snake["image"], position)

        apple_x, apple_y = apple["position"]

        if apple_x - (BLOCK + 10) <= head[0] <= apple_x + (
            BLOCK + 10
        ) and apple_y - (BLOCK + 10) <= head[1] <= apple_y + (BLOCK + 10):
            point_sound_effect.play()
            score += 1
            apple["position"] = (
                random.randint(0, WIDTH - 16),
                random.randint(0, WIDTH - 16),
            )
            snake["length"] += 1

    # update
    pygame.display.update()
    game_clock.tick(SPEED)

game_over_sound_effect.play()

# game over screen
window.fill(COLOR_BLACK)
game_over_message = FONT.render("Game Over", 1, COLOR_WHITE)
window.blit(game_over_message, (WIDTH // 2 - 100, WIDTH // 2 - 50))

# score
score_message = FONT.render(
    "Your score: %d" % (snake["length"] - 1), 1, COLOR_WHITE
)
window.blit(score_message, (WIDTH // 5, WIDTH // 2))

pygame.display.update()
time.sleep(2)
