import pygame


def draw_hex_tile(surface, tile, center_point):
    return


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for tile in game.hex_tiles:
        draw_hex_tile(tile)

    pygame.display.flip()
