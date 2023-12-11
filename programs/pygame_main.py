import pygame


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PYGAME')

image = pygame.image.load('resources/pygame_logo.png')
image = pygame.transform.scale(image, (600, 200))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(image, (100, 100))
    pygame.display.flip()


pygame.quit()