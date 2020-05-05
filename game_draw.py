import pygame


def draw_hex_tile(surface, game, tile):
    center_point = tile.center_point(game.board_position)
    corner_points = tile.corner_points(game.board_position)
    pygame.draw.polygon(surface, tile.colour, corner_points)
    pygame.draw.polygon(surface, (255, 255, 255), corner_points, 2) # border
    pygame.draw.circle(surface, (0, 0, 255), center_point, 12) # checking the center points


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for tile in game.hex_tiles:
        draw_hex_tile(surface, game, tile)

    pygame.display.flip()
