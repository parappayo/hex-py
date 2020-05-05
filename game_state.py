import hex_geometry


class GameState:
    def __init__(self):
        self.background_colour = 0, 0, 0 # rgb 256
        self.screen_size = 1024, 768 # pixels
        self.board_position = 100, 100 # pixels

        self.hex_tile_size = 40
        self.board_width_tiles = 11 
        self.board_height_tiles = 11 
        self.generate_board()


    def generate_board(self):
        width = self.board_width_tiles
        height = self.board_height_tiles
        hex_size_px = hex_geometry.tile_size_to_px(self.hex_tile_size)
        self.hex_tiles = [hex_geometry.HexTile(x, y, hex_size_px) for x in range(width) for y in range(height)]
