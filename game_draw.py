import pygame, math


def hex_corner_point(width, index, offset):
    theta = math.tau * index / 6 + math.tau / 12
    return (width * math.cos(theta) + offset[0], width * math.sin(theta) + offset[1])


def draw_hex_tile(surface, game, tile):
    width = game.hex_width_pixels
    center_point = tile.center_point_pixels(game.board_position, width)
    corner_points = [hex_corner_point(width // 2, i, center_point) for i in range(6)]
    pygame.draw.polygon(surface, tile.colour, corner_points)
    pygame.draw.circle(surface, (0, 0, 255), center_point, 12) # checking the center points


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for tile in game.hex_tiles:
        draw_hex_tile(surface, game, tile)

    pygame.display.flip()
