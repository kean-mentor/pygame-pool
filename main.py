import sys

import pygame
import pymunk
import pymunk.pygame_util

import constants as c


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('PyGame Pool')
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        self.space = pymunk.Space()

        self._load_images()

        self.ball = self._create_ball((c.SCREEN_WIDTH / 2, c.SCREEN_HEIGHT / 2))

    def run(self):
        draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        while True:
            self.screen.blit(self.table_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(c.FPS)
            self.space.step(1 / c.FPS)

            self.space.debug_draw(draw_options)
            pygame.display.update()

    def _load_images(self):
        self.table_img = pygame.image.load('images/table.png').convert_alpha()

    def _create_ball(self, pos, radius=c.BALL_RADIUS):
        ball = pymunk.Body()
        ball.position = pos
        shape = pymunk.Circle(ball, radius)
        shape.mass = c.BALL_MASS

        self.space.add(ball, shape)
        return shape


if __name__ == "__main__":
    game = Game()
    game.run()
