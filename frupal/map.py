"""
Nick Grout 1/23/2020
"""
from random import randint
import enum
from .tiles import Tile
from .player import Player
from .config import Config


class Map:
    """
    This is the main map class. It constructs and manages the 2d array of
    tiles
    """

    @staticmethod
    def generate_map(config: Config):
        """
        Generate a new map from the given config, with randomly placed tiles according to the
        :returns: a generated map
        """
        # TODO(Nick) implement map generation once config is finished
        # new_map = Map(config.rows, config.columns)
        new_map = Map(5, 3)
        # Make 1d array of all tiles (easier for tile assignment)
        tiles = []
        for col in new_map._array:
            tiles += col
        # BUG: when we have multiple tile types, they could overwrite each other
        '''
        for i in range(config.boulder_count):
            random_index = randint(0, len(map_arr) - 1)
            tiles[random_index] = BoulderTile()
            # ETC
        for i, tile in enumerate(tiles):
            print(i, tile.title + ', ')
        '''

    def __init__(self, config: Config, debug: bool):
        """
        :param rows: the x dimension of the map
        :param columns: the y dimension of the map
        :returns: a new map object with a basic (all normal Tiles) 2d array
        """
        self._array = [[] for i in range(config.get_map("height"))]
        for i in range(len(self._array)):
            self._array[i] = [Tile('tile', 1, debug) for i in range(config.get_map("width"))]

    def __getitem__(self, row: int):
        """
        Access an item in the 2d array
        """
        return self._array[row]

    def __str__(self):
        """
        Output a representation of the map to a string
        :returns: a string representation (human readable format) of the map
        """
        return_str = "****** FOR DEBUG PURPOSE ONLY\n"
        for i in range(len(self._array[0])):
            for j in range(len(self._array)):
                return_str += self._array[j][i].title + ", "
            return_str += "\n"
        return return_str

    def get_size(self):
        """
        Returns (ROWS, COLUMNS)
        :returns: the dimensions of the 2D array as a tuple. 
        """
        return len(self._array), len(self._array[0])
