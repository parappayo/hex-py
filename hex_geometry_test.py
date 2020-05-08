import unittest
import hex_geometry


class TestHexGrid(unittest.TestCase):

    def test_populate_neighbours(self):
        hex_grid = hex_geometry.HexGrid(3, 3, 10, True)

        neighbours = hex_grid.tiles[(0, 0)].neighbours
        self.assertEqual(len(neighbours), 2)
        self.assertIn(hex_grid.tiles[(0, 1)], neighbours)
        self.assertIn(hex_grid.tiles[(1, 0)], neighbours)

        neighbours = hex_grid.tiles[(2, 2)].neighbours
        self.assertEqual(len(neighbours), 2)
        self.assertIn(hex_grid.tiles[(1, 2)], neighbours)
        self.assertIn(hex_grid.tiles[(2, 1)], neighbours)

        neighbours = hex_grid.tiles[(1, 1)].neighbours
        self.assertEqual(len(neighbours), 6)
        self.assertIn(hex_grid.tiles[(1, 0)], neighbours)
        self.assertIn(hex_grid.tiles[(2, 0)], neighbours)
        self.assertIn(hex_grid.tiles[(0, 1)], neighbours)
        self.assertIn(hex_grid.tiles[(2, 1)], neighbours)
        self.assertIn(hex_grid.tiles[(0, 2)], neighbours)
        self.assertIn(hex_grid.tiles[(1, 2)], neighbours)

    def test_find_path(self):
        hex_grid = hex_geometry.HexGrid(1, 1, 10, True)
        path = hex_grid.find_path(
            hex_grid.tiles[(0, 0)],
            [hex_grid.tiles[(0, 0)]],
            lambda x: True)
        self.assertEqual(len(path), 1)
        self.assertIn(hex_grid.tiles[(0, 0)], path)

        hex_grid = hex_geometry.HexGrid(3, 3, 10, True)
        path = hex_grid.find_path(
            hex_grid.tiles[(0, 0)],
            [hex_grid.tiles[(2, 2)]],
            lambda x: True)
        self.assertTrue(len(path) > 0)
        self.assertIn(hex_grid.tiles[(0, 0)], path)
        self.assertIn(hex_grid.tiles[(2, 2)], path)

    def test_find_path_applies_filter(self):
        player_one_colour = (255, 0, 0)
        player_two_colour = (0, 0, 255)

        hex_grid = hex_geometry.HexGrid(1, 1, 10, True)
        hex_grid.tiles[(0, 0)].colour = player_one_colour
        path = hex_grid.find_path(
            hex_grid.tiles[(0, 0)],
            [hex_grid.tiles[(0, 0)]],
            lambda x: x.colour == player_two_colour)
        self.assertEqual(path, None)

        hex_grid = hex_geometry.HexGrid(3, 3, 10, True)
        for tile in hex_grid.tiles.values():
            tile.colour = player_two_colour
        hex_grid.tiles[(0, 0)].colour = player_one_colour
        hex_grid.tiles[(1, 0)].colour = player_one_colour
        hex_grid.tiles[(1, 1)].colour = player_one_colour
        hex_grid.tiles[(2, 1)].colour = player_one_colour
        hex_grid.tiles[(2, 2)].colour = player_one_colour
        path = hex_grid.find_path(
            hex_grid.tiles[(0, 0)],
            [hex_grid.tiles[(2, 2)]],
            lambda x: x.colour == player_one_colour)
        self.assertEqual(len(path), 5)
        self.assertIn(hex_grid.tiles[(0, 0)], path)
        self.assertIn(hex_grid.tiles[(1, 0)], path)
        self.assertIn(hex_grid.tiles[(1, 1)], path)
        self.assertIn(hex_grid.tiles[(2, 1)], path)
        self.assertIn(hex_grid.tiles[(2, 2)], path)


if __name__ == '__main__':
    unittest.main()
