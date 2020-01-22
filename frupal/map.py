import enum
from .tiles import Tile
from .player import Player
from .config import Config


class Map:
	#Needs map generator, basic format that fills map with default tile.
	def __init__(self, x, y):
		self.columns = x
		self.rows = y
		self.tiles = [[Tile(u"\u25A0", 1) for j in range(self.columns)] for i in range(self.rows)]

	def get_rows(self):
		return self.rows

	def get_columns(self):
		return self.columns

	def get_row(self, n):
		return self.tiles[n]

	def get_tile(self, x, y):
		return self.tiles[y][x]

	def get_size(self):
                return [self.columns, self.rows]
