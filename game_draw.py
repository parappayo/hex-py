import pygame


def draw_hex_tile(surface, game, tile):
    width = game.hex_width_pixels
    center_point = tile.center_point_pixels(game.board_position, width)
    pygame.draw.circle(surface, tile.colour, center_point, width//2)


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for tile in game.hex_tiles:
        draw_hex_tile(surface, game, tile)

    pygame.display.flip()
