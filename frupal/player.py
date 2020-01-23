import enum


class Direction(enum.Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Player:
    def __init__(self, energy, money, game_map):
        self.energy = energy
        self.money = money
        self.position = [0, 0]

    # Needs a case for the boundary wall?
    def move(self, direction, game_map):
        if self.energy > 0:
            if direction == "north":
                self.position[1] += -1
            if direction == "west":
                self.position[0] += -1
            if direction == "east":
                self.position[0] += 1
            if direction == "south":
                self.position[1] += 1
            self.energy += -(game_map.get_tile(self.position[1], self.position[0]).get_energy_req())

    def get_energy(self):
        return self.energy

    def get_money(self):
        return self.money

    def get_position(self):
        return self.position
