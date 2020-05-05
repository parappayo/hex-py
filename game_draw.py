import pygame


def draw_hex_tile(surface, game, tile):
    center_point = tile.center_point(game)
    corner_points = tile.corner_points(game)
    pygame.draw.polygon(surface, tile.colour, corner_points)
    pygame.draw.polygon(surface, (255, 255, 255), corner_points, 2) # border

    if tile == game.nearest_tile_to_mouse:
        pygame.draw.circle(surface, game.cursor_colour, center_point, 12)


def draw_frame(surface, game):
    surface.fill(game.background_colour)

    for tile in game.hex_tiles:
        draw_hex_tile(surface, game, tile)

    pygame.display.flip()
