from .map import Direction


class Player:
	def __init__(self, energy, money):
		self.energy = energy
		self.money = money
		self.position = [3, 5]

	# Needs a case for the boundary wall?
	def move(self, direction, map):
		if (direction == "north"):
			self.position[1] += -1
		if (direction == "west"):
			self.position[0] += -1
		if (direction == "east"):
			self.position[0] += 1
		if (direction == "south"):
			self.position[1] += 1
		self.energy += -(map.get_req(self.position[0], self.position[1]));

	def getenergy(self):
		return self.energy

	def getmoney(self):
		return self.money

	def getposition(self):
		return self.position

