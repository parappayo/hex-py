import math
from functools import lru_cache


def tile_size_to_px(size):
    return (math.floor(size * math.sqrt(3)), size * 2)


@lru_cache(maxsize=128)
def center_point(grid_position, width, height, offset):
    x, y = grid_position
    dx, dy = offset
    height = math.floor(height * 3/4)

    # stagger odd rows
    if y % 2:
        dx += width // 2

    return (x * width + dx, y * height + dy)


def corner_point(radius, index, position_px):
    """Hexes with corner at top."""
    theta = math.tau * index / 6 + math.tau / 12
    x, y = position_px
    return (radius * math.cos(theta) + x, radius * math.sin(theta) + y)


@lru_cache(maxsize=128)
def corner_points(grid_position, width, height, offset):
    radius = height // 2
    position_px = center_point(grid_position, width, height, offset)
    return [corner_point(radius, i, position_px) for i in range(6)]


class HexTile:
    def __init__(self, grid_x, grid_y, size_px):
        self.grid_position = (grid_x, grid_y)
        self.width, self.height = size_px
        self.colour = 0, 128, 128 # rgb 256


    def center_point(self, game):
        return center_point(self.grid_position, self.width, self.height, game.board_position)


    def corner_points(self, game):
        return corner_points(self.grid_position, self.width, self.height, game.board_position)


    def distance_squared(self, pos, game):
        x1, y1 = self.center_point(game)
        x2, y2 = pos
        dx, dy = x1 - x2, y2 - y1
        return dx * dx + dy * dy
