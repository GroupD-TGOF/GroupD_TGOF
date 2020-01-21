import enum
from .tiles import Tile
from .player import Player
from .config import Config


class Direction(enum.Enum):
	NORTH = "north"
	EAST = "east"
	SOUTH = "south"
	WEST = "west"


class Map:
	#Needs map generator, basic format that fills map with default tile.
	def __init__(self, x, y):
		self.columns = x
		self.rows = y
		self.tiles = [[Tile(u"\u25A0", 1) for j in range(self.columns)] for i in range(self.rows)]
		self.tiles[0][0].seen_set(True)

	def get_rows(self):
		return self.rows

	def get_columns(self):
		return self.columns

	def get_row(self, n):
		return self.tiles[n]

	def get_tile(self, x, y):
		return self.tiles[y][x].get_name()

	def get_req(self, x, y):
		return self.tiles[y][x].get_energy_req()

	def get_seen(self, x, y):
		return self.tiles[y][x].seen_status()