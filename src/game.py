import pygame
from pygame import font
from renderer import Renderer
from debug_screen import DebugScreen
from src.hud import HeadsUpDisplay
from walls import Walls
from src.player_character import PlayerCharacter
from worldmap import WorldMap
from input.input_handler import InputHandler
from src.texture_library import TextureLibrary

SCREEN_X = 1280
SCREEN_Y = 720


def main():
    font.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    input_handler = InputHandler()
    clock = pygame.time.Clock()
    running = True
    renderer = Renderer(screen, Walls(SCREEN_X, SCREEN_Y), SCREEN_X, SCREEN_Y, TextureLibrary())
    debug_screen = DebugScreen()
    world = WorldMap()
    pc = PlayerCharacter(1, 5, input_handler, debug_screen, renderer)
    pc.set_world(world)
    hud = HeadsUpDisplay(screen, SCREEN_X, SCREEN_Y, pc)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                input_handler.on_event(event)

        screen.fill("black")
        pc.camera.render_walls()
        pc.camera.render_forwards()
        debug_screen.render(screen)
        hud.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()