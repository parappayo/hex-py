import unittest
import hex_geometry


class TestHexGrid(unittest.TestCase):

    def test_populate_neighbours(self):
        hex_grid = hex_geometry.HexGrid(3, 3, 10, True)

        neighbours = hex_grid.tiles[(0, 0)].neighbours
        self.assertEqual(len(neighbours), 2)
        self.assertIn(hex_grid.tiles[(0, 1)], neighbours)
        self.assertIn(hex_grid.tiles[(1, 0)], neighbours)

        neighbours = hex_grid.tiles[(1, 1)].neighbours
        self.assertEqual(len(neighbours), 6)


if __name__ == '__main__':
    unittest.main()
