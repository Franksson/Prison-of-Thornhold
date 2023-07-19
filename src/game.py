import pygame
from fprenderer import Renderer

SCREEN_X = 1280
SCREEN_Y = 720


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    clock = pygame.time.Clock()
    running = True
    renderer = Renderer(screen, SCREEN_X, SCREEN_Y)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        renderer.render_walls(True, True, True, True, False)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()