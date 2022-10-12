import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('PyGame Pool')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(60)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
