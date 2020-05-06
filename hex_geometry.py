import math
from functools import lru_cache


def distance_squared(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x1 - x2, y2 - y1
    return dx * dx + dy * dy


def points_up_tile_size_px(size):
    return math.floor(size * math.sqrt(3)), size * 2


def flats_up_tile_size_px(size):
    return size * 2, math.floor(size * math.sqrt(3))


@lru_cache(maxsize=128)
def points_up_tile_center_point(grid_position, width, height, offset):
    x, y = grid_position
    dx, dy = offset
    height = math.floor(height * 3/4)

    # stagger odd rows
    if y % 2:
        dx += width // 2

    # diamond-shaped board
    x += y // 2

    return (x * width + dx, y * height + dy)


@lru_cache(maxsize=128)
def flats_up_tile_center_point(grid_position, width, height, offset):
    x, y = grid_position
    dx, dy = offset
    width = math.floor(width * 3/4)

    # stagger odd columns
    if x % 2:
        dy += height // 2

    # diamond-shaped board
    y += x // 2

    return (x * width + dx, y * height + dy)


def points_up_tile_corner_point(radius, index, position_px):
    theta = math.tau * index / 6 + math.tau / 12
    x, y = position_px
    return (radius * math.cos(theta) + x, radius * math.sin(theta) + y)


def flats_up_tile_corner_point(radius, index, position_px):
    theta = math.tau * index / 6
    x, y = position_px
    return (radius * math.cos(theta) + x, radius * math.sin(theta) + y)


@lru_cache(maxsize=128)
def points_up_tile_corner_points(grid_position, width, height, offset):
    radius = height // 2
    position_px = points_up_tile_center_point(grid_position, width, height, offset)
    return [points_up_tile_corner_point(radius, i, position_px) for i in range(6)]


@lru_cache(maxsize=128)
def flats_up_tile_corner_points(grid_position, width, height, offset):
    radius = width // 2
    position_px = flats_up_tile_center_point(grid_position, width, height, offset)
    return [flats_up_tile_corner_point(radius, i, position_px) for i in range(6)]


class HexTile:
    def __init__(self, grid_x, grid_y, size_px, colour, points_up):
        self.grid_position = (grid_x, grid_y)
        if points_up:
            self.width, self.height = points_up_tile_size_px(size_px)
        else:
            self.width, self.height = flats_up_tile_size_px(size_px)
        self.colour = colour
        self.points_up = points_up


    def center_point(self, game):
        if self.points_up:
            return points_up_tile_center_point(
                self.grid_position,
                self.width,
                self.height,
                game.board_position)
        else:
            return flats_up_tile_center_point(
                self.grid_position,
                self.width,
                self.height,
                game.board_position)


    def corner_points(self, game):
        if self.points_up:
            return points_up_tile_corner_points(
                self.grid_position,
                self.width,
                self.height,
                game.board_position)
        else:
            return flats_up_tile_corner_points(
                self.grid_position,
                self.width,
                self.height,
                game.board_position)


    def distance_squared(self, position, game):
        return distance_squared(self.center_point(game), position)


def generate_board(board_width, board_height, hex_tile_size, hex_colour, points_up):
    return [
        HexTile(x, y, hex_tile_size, hex_colour, points_up)
        for x in range(board_width)
        for y in range(board_height)]
