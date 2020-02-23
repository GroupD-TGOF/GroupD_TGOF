"""
Nick Grout 1/23/2020
"""
from random import randint
import enum
from .tiles import Tile, Water, Mud, Tree
from .player import Player
from .config import Config


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
        base = 'tile'
        tiles = ['water', 'tree', 'mud', 'troll', 'blackberry', 'boulder']
        self._array = [[] for i in range(config.get_map("height"))]
        
        for i in range(len(self._array)):
            self._array[i] = [Tile(base, 1, debug) for i in range(config.get_map("width"))]

        for tile in tiles:
            count = 0
            while count < config.get_map(tile):
                x = randint(0,len(self._array)-1)
                y = randint(0,len(self._array[0])-1)
                if self._array[x][y].get_name() == base:
                    if tile == 'water':
                        self._array[x][y] = Water(debug)
                    elif tile == 'tree':
                        self._array[x][y] = Tree(debug)
                    elif tile == 'mud':
                        self._array[x][y] = Mud(debug)
                    elif tile == 'troll':
                        self._array[x][y] = Tile('troll',1,debug)
                    elif tile == 'blackberry':
                        self._array[x][y] = Tile('blackberry',1,debug)
                    elif tile == 'boulder':
                        self._array[x][y] = Tile('boulder',1,debug)
                    count += 1
        
        for j in range(config.get_map('total') // 90):
            self._array[randint(0,len(self._array)-1)][randint(0,len(self._array[0])-1)].add_inv('jewels')
                        

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
