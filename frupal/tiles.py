class Tile:
	def __init__(self, title, energy_req, debug):
		if debug:
			self.is_seen = True
		else:
			self.is_seen = False

		self.title = title
		self.energy_req = energy_req
		self.icon = u"\u25A0"

	def get_name(self):
		return self.title

	def get_energy_req(self, player_inventory):
		return self.energy_req

	def get_icon(self):
		return self.icon

	def seen_status(self):
		return self.is_seen

	def seen_set(self, status):
		self.is_seen = status


class Water(Tile):
	def __init__(self, debug):
		Tile.__init__(self, "water", 2, debug)  # the water_type also represent the energy requirements


'''
	def get_energy_req(self, player_inventory):  # if the tile is water, calling get_energy will call this method
		if "boat" in player_inventory:
			return self.energy_req
		else:
			print("Entering this area without a boat will cost double energy")
			self.energy_req *= 2  # without a boat the energy requirements is doubles
			return self.energy_req
'''


class Mud(Tile):
	def __init__(self, debug):
		Tile.__init__(self, "mud", 5, debug)
		self.plank = False


'''
	def get_energy_req(self, player_inventory):
		if not self.plank:  # check self whether a wood plank has been place here or not
			if "wood_plank" in player_inventory:  # no plank has been place, check player bag for the planks
				print("Wood plank used!")
				self.plank = True  # available plank will be placed
				return 1
			else:
				print(
					"No wood planks available, 5 energy is required to tranverse")  # no planks, more energy to go through
				return self.energy_req
		else:
			return 1  # if player returns to this tile, wood plank has been place so return 1
'''


class Tree(Tile):
	def __init__(self, debug):
		Tile.__init__(self, "tree", 1, debug)
		self.tree_status = True  # the tree is chopper down for False, and standing for True
		self.icon = u"\u25B2"


'''
	def get_energy_req(self, player_inventory):
		if self.tree_status:
			if "saw" in player_inventory:
				self.tree_status = False
				print("Path is cleared")
				return self.energy_req
			else:
				print("a tree blocks your path")
				return 0
		else:
			return 1
'''

# hard mode tiles
