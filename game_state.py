

class HexTile:
    def __init__(self, x, y):
        self.grid_position = (x, y)
        self.colour = 0, 128, 128 # rgb 256


    def center_point_pixels(self, board_position, tile_width):
        x, y = self.grid_position

        x_offset = 0
        if y % 2:
            x_offset = tile_width // 2

        return (x * tile_width + board_position[0] + x_offset, y * tile_width + board_position[1])


class GameState:
    def __init__(self):
        self.background_colour = 0, 0, 0 # rgb 256
        self.screen_size = 1024, 768 # pixels
        self.board_position = 100, 100 # pixels

        self.hex_width_pixels = 48
        self.board_width_tiles = 11 
        self.board_height_tiles = 11 
        self.generate_board()


    def generate_board(self):
        width = self.board_width_tiles
        height = self.board_height_tiles
        self.hex_tiles = [HexTile(x, y) for x in range(width) for y in range(height)]
