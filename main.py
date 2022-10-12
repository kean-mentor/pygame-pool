import sys
import pygame

import constants as c


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('PyGame Pool')
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        self._load_images()

    def run(self):
        while True:
            self.screen.blit(self.table_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(c.FPS)
            pygame.display.update()

    def _load_images(self):
        self.table_img = pygame.image.load('images/table.png').convert_alpha()


if __name__ == "__main__":
    game = Game()
    game.run()
