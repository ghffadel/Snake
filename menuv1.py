import pygame, sys
pygame.init()

# screen
BLOCK = 15
SPEED = 15
WIDTH = 500


# colors
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)

#background image
main_menu = pygame.image.load("assets/snake_menu.jpg")
#background1 = pygame.image.load("startscreen.png")
pause_menu_image = pygame.image.load("assets/pause.jpg")
credits_menu_image = pygame.image.load("assets/credits_snakev2.jpg")


click = False


window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake")

game_clock = pygame.time.Clock()
game_over = False
pause_menu = False
credits_menu = False
menu = True

FONT = pygame.font.Font("assets/PressStart2P.ttf", 24)

#font = pygame.font.SysFont(None, 20)


#def draw_text(text, font, color, surface, x, y):
 #   textobj = font.render(text, 1, color)
  #  textrect = textobj.get_rect()
  #  textrect.topleft = (x, y)
  #  surface.blit(textobj, textrect)


def run_menu():
    global menu
    while menu:
        window.fill((0, 0, 0, 0))
        window.blit(main_menu, (0, 0))

        start_button = pygame.Rect(50, 200, 200, 50)
        credits_button = pygame.Rect(50, 300, 200, 50)
        pygame.image.load("assets/Start.png")
        pygame.image.load("assets/credits.png")

        start_message = FONT.render("Start", 1, COLOR_WHITE)
        window.blit(start_message, (50, 200))


        credits_option = FONT.render("Credits", 1, COLOR_WHITE)
        window.blit(credits_option, (50, 300))

        #draw_text('main menu', font, (255, 255, 255), window, 20, 20)

        #pygame.draw.rect(window, (255, 0, 0), start_button)
        #pygame.draw.rect(window, (0, 0, 255), credits_button)

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint((mx, my)):
                        menu = False
                    elif  credits_button.collidepoint((mx, my)):
                        credits()




        game_clock.tick(SPEED)
        pygame.display.update()



def pause():
    pause_menu = True
    while pause_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pause_menu = False

        window.fill((0, 0, 0, 0))
        game_clock.tick(SPEED)
        window.blit(pause_menu_image, (0, 0))

        pause_message = FONT.render("Click  to return", 1, COLOR_WHITE)
        window.blit(pause_message, (50, 300))

        pygame.display.update()

def credits():
    credits_menu = True
    while credits_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    credits_menu = False

        window.fill((0, 0, 0, 0))
        game_clock.tick(SPEED)
        window.blit(credits_menu_image, (0, 0))

        pygame.display.update()

