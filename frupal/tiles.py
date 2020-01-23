
class Tile:
	def __init__(self, title, energy_req):
		self.title = title
		self.is_seen = False
		self.energy_req = energy_req

	def get_name(self):
		return self.title

	def get_energy_req(self):
		return self.energy_req

	def seen_status(self):
		return self.is_seen

	def seen_set(self, status):
		self.is_seen = status
