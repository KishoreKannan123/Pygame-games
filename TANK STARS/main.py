import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

while(run):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()