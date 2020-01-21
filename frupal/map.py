import enum


class Direction(enum.Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Map:
	def __init__(self, x, y):
		self.y = y
		self.x = x
		self.a = [' '] * self.y
		for i in range(self.y):
			#temp fill map with character for tile
			self.a[i] = [u"\u25A0"] * self.x
	
	def get_rows(self):
		return self.y
	
	def get_columns(self):
		return self.x

	def get_row(self, n):
		return self.a[n]

	def get_tile(self, x, y):
		return self.a[y][x]