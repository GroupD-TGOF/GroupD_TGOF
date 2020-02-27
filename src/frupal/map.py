"""
Nick Grout 1/23/2020
"""
from .tiles import Tile, Water, Mud, Tree, Troll, Blackberry, Boulder
from .config import Config
from random import randint
import platform


class Map:
    """
    This is the main map class. It constructs and manages the 2d array of
    tiles
    """

    def __init__(self, config: Config, debug: bool):
        """
        :param rows: the x dimension of the map
        :param columns: the y dimension of the map
        :returns: a new map object with a basic (all normal Tiles) 2d array
        """
        self._array = []

    def update_map(self, config: Config, debug: bool):
        base_icon = u"\u25A0"
        base = 'tile'
        if platform.system() == "Windows":
            base_icon = "L"
        base_color = 'green'
        base_tool = 'feet'

        tiles = config.get_tiles()
        self._array = [[] for i in range(config.get_map("height"))]

        for i in range(len(self._array)):
            self._array[i] = [Tile(base, 1, base_icon, base_color, base_tool, debug) for i in
                              range(config.get_map("width"))]

        self.__random_gen(base, tiles, config, debug)

        self._array[randint(0, len(self._array) - 1)][randint(0, len(self._array[0]) - 1)].add_inv('jewels')
        for j in range(config.get_map('total') // 90):
            self._array[randint(0, len(self._array) - 1)][randint(0, len(self._array[0]) - 1)].add_inv('jewels')

        self._array[0][0].seen_set(True)

    def __random_gen(self, base, tiles, config, debug):
        for tile in tiles:
            count = 0
            info = config.get_tile(tile)
            while count < info['count']:
                x = randint(0, len(self._array) - 1)
                y = randint(0, len(self._array[0]) - 1)
                if self._array[x][y].get_name() == base:
                    self.__set_tile(tile, info, x, y, debug)
                    count += 1

    def __set_tile(self, tile, info, x, y, debug):
        if tile == 'water':
            self._array[x][y] = Water(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)
        elif tile == 'tree':
            self._array[x][y] = Tree(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)
        elif tile == 'mud':
            self._array[x][y] = Mud(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)
        elif tile == 'troll':
            self._array[x][y] = Troll(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)
        elif tile == 'blackberry':
            self._array[x][y] = Blackberry(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)
        elif tile == 'boulder':
            self._array[x][y] = Boulder(tile, info['energy_req'], info['icon'], info['color'], info['tool']['name'], debug)

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

    def map_reveal(self):
        for i in range(len(self._array[0])):
            for j in range(len(self._array)):
                self._array[j][i].seen_set(True)
