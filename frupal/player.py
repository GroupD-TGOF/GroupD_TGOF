import enum
from .config import Config


class Direction(enum.Enum):
    NORTH = "North"
    EAST = "East"
    SOUTH = "South"
    WEST = "West"
    NULL = "Wrong Direction"


class Player:
    def __init__(self, config: Config, debug):
        if not debug:
            self.energy = config.get_player('energy')
            self.money = config.get_player('money')
            self.position = [0, 0]

        else:
            self.energy = 100
            self.money = 100
            self.position = [config.get_map('width') // 2, config.get_map('height') // 2]

    # Needs a case for the boundary wall?
    def move(self, direction, game_map):
        if self.energy > 0 and direction != Direction.NULL:
            if direction == Direction.NORTH:
                self.position[1] += -1
            elif direction == Direction.WEST:
                self.position[0] += -1
            elif direction == Direction.EAST:
                self.position[0] += 1
            elif direction == Direction.SOUTH:
                self.position[1] += 1
            self.energy += -(game_map[self.position[1]][self.position[0]].get_energy_req())

    def get_energy(self):
        return self.energy

    def get_money(self):
        return self.money

    def get_position(self):
        return self.position
