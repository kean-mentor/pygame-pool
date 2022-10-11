import sys
import pygame

pygame.init()
pygame.display.set_caption('PyGame Pool')
screen = pygame.display.set_mode((800, 600), 0, 32)
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    clock.tick(60)
    pygame.display.update()
