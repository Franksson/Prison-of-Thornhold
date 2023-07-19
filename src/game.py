import pygame
from pygame import font
from fprenderer import Renderer
from debug_screen import DebugScreen
from src.player_character import PlayerCharacter

SCREEN_X = 1280
SCREEN_Y = 720


def main():
    font.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    clock = pygame.time.Clock()
    running = True
    renderer = Renderer(screen, SCREEN_X, SCREEN_Y)
    debug_screen = DebugScreen()
    pc = PlayerCharacter(1, 3, debug_screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pc.move_forward()
                if event.key == pygame.K_d:
                    pc.turn()
                elif event.key == pygame.K_a:
                    pc.turn(False)

        screen.fill("black")
        renderer.render_walls(True, True, True, True, False)
        debug_screen.render(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()