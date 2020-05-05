import hex_geometry


class GameState:
    def __init__(self):
        self.background_colour = 0, 0, 0 # rgb 256
        self.screen_size = 1024, 768 # pixels
        self.board_position = 100, 100 # pixels

        self.hex_tile_size = 32
        self.board_width_tiles = 11
        self.board_height_tiles = 11

        self.empty_hex_colour = (32, 32, 32)
        self.cursor_colour = (32, 128, 32)
        self.player_colour = [(255, 0, 0), (0, 0, 255)]

        self.nearest_tile_to_mouse = None
        self.current_player = 0
        self.moves = []

        self.generate_board()


    def generate_board(self):
        points_up = True
        self.hex_tiles = hex_geometry.generate_board(
            self.board_width_tiles,
            self.board_height_tiles,
            self.hex_tile_size,
            self.empty_hex_colour,
            points_up)


    def nearest_hex_tile(self, pos):
        result = None
        min_distance = None

        for tile in self.hex_tiles:
            tile_distance = tile.distance_squared(pos, self)
            if result == None:
                min_distance = tile_distance
                result = tile
            elif tile_distance < min_distance:
                min_distance = tile_distance
                result = tile

        return result


    def is_valid_move(self, tile=None):
        if tile == None:
            tile = self.nearest_tile_to_mouse
        return not tile in self.moves


    def take_move(self, tile=None):
        if tile == None:
            tile = self.nearest_tile_to_mouse
        tile.colour = self.player_colour[self.current_player]
        self.moves.append(tile)
        self.toggle_player_turn()


    def toggle_player_turn(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0
