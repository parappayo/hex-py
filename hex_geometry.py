import math
from functools import lru_cache


def tile_size_to_px(size, points_up):
    a, b = size * 2, math.floor(size * math.sqrt(3))
    if points_up:
        return b, a
    return a, b


@lru_cache(maxsize=128)
def center_point(grid_position, width, height, offset, points_up):
    x, y = grid_position
    dx, dy = offset
    if points_up:
        height = math.floor(height * 3/4)
        # stagger odd rows
        if y % 2:
            dx += width // 2
    else:
        width = math.floor(width * 3/4)
        # stagger odd columns
        if x % 2:
            dy += height // 2

    return (x * width + dx, y * height + dy)


def corner_point(radius, index, position_px, points_up):
    theta = math.tau * index / 6
    if points_up:
        theta += math.tau / 12
    x, y = position_px
    return (radius * math.cos(theta) + x, radius * math.sin(theta) + y)


@lru_cache(maxsize=128)
def corner_points(grid_position, width, height, offset, points_up):
    if points_up:
        radius = height // 2
    else:
        radius = width // 2
    position_px = center_point(grid_position, width, height, offset, points_up)
    return [corner_point(radius, i, position_px, points_up) for i in range(6)]


class HexTile:
    def __init__(self, grid_x, grid_y, size_px, colour, points_up):
        self.grid_position = (grid_x, grid_y)
        self.width, self.height = tile_size_to_px(size_px, points_up)
        self.colour = colour
        self.points_up = points_up


    def center_point(self, game):
        return center_point(
            self.grid_position,
            self.width,
            self.height,
            game.board_position,
            self.points_up)


    def corner_points(self, game):
        return corner_points(
            self.grid_position,
            self.width,
            self.height,
            game.board_position,
            self.points_up)


    def distance_squared(self, pos, game):
        x1, y1 = self.center_point(game)
        x2, y2 = pos
        dx, dy = x1 - x2, y2 - y1
        return dx * dx + dy * dy


def square_board(board_width, board_height, hex_tile_size, hex_colour, points_up):
    return [
        HexTile(x, y, hex_tile_size, hex_colour, points_up)
        for x in range(board_width)
        for y in range(board_height)]
