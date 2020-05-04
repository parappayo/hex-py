
class GameState:
    def __init__(self):
        self.background_colour = 0, 0, 0 # rgb 256
        self.screen_size = 1024, 768 # pixels

        self.hex_width_pixels = 24
        self.board_width_tiles = 11 
        self.board_height_tiles = 11 
        self.hex_tiles = []
