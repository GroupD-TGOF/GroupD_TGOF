import enum


class Direction(enum.Enum):
    NORTH = 'north'
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'


class Map:
    def __init__(self):
        self.rows = []

    def get_row(self, n: int):
        """
        Get a specific row from the map
        :param n: the row index to return
        :return:
        """
        return self.rows[n]

    def get_tile(self, x: int, y: int):
        """
        Get a specific tile
        :param x: the x coordinate
        :param y: the y coordinate
        :return:
        """
        return self.rows[x][y]
