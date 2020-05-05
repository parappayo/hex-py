import math


def tile_size_to_px(size):
    return (math.floor(size * math.sqrt(3)), size * 2)


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


def corner_points(grid_position, width, height, offset):
    radius = height // 2
    position_px = center_point(grid_position, width, height, offset)
    return [corner_point(radius, i, position_px) for i in range(6)]


class HexTile:
    def __init__(self, grid_x, grid_y, size_px):
        self.grid_position = (grid_x, grid_y)
        self.width, self.height = size_px
        self.colour = 0, 128, 128 # rgb 256


    def center_point(self, offset):
        return center_point(self.grid_position, self.width, self.height, offset)


    def corner_points(self, offset):
        return corner_points(self.grid_position, self.width, self.height, offset)
