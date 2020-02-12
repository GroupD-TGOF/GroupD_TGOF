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
        self.map_size = [config.get_map('width'), config.get_map('height')]
        if not debug:
            self.energy = config.get_player('energy')
            self.money = config.get_player('money')
            self.position = [0, 0]

        else:
            self.energy = 100
            self.money = 100
            self.position = [config.get_map('width') // 2, config.get_map('height') // 2]

        self.player_inventory = dict()

    def player_view(self, view_dist, position, game_map):
        if not game_map[position[1]][position[0]].seen_status():
            game_map[position[1]][position[0]].seen_set(True)

    # Needs a case for the boundary wall?
    def move(self, direction, game_map):
        self.player_view(2, self.position, game_map)
        if self.energy > 0 and direction != Direction.NULL:
            if direction == Direction.NORTH:
                self.position[1] += -1
                if self.position[1] < 0:
                    self.position[1] -= -1
            elif direction == Direction.WEST:
                self.position[0] += -1
                if self.position[0] < 0:
                    self.position[0] -= -1
            elif direction == Direction.EAST:
                self.position[0] += 1
                if self.position[0] > self.map_size[0] - 1:
                    self.position[0] -= 1
            elif direction == Direction.SOUTH:
                self.position[1] += 1
                if self.position[1] > self.map_size[1] - 1:
                    self.position[1] -= 1
            self.energy += -(game_map[self.position[1]][self.position[0]].get_energy_req(self.player_inventory))
            if self.energy < 0:
                self.energy = 0

    def add_inv(self, new_item):
        if new_item in self.player_inventory:
            self.player_inventory[new_item] += 1
        else:
            self.player_inventory.update({new_item: 1})

    def print_inv(self):
        inv = ''
        for key in self.player_inventory:
            inv += key + ': ' + str(self.player_inventory[key]) + '   '
        return inv

    def get_energy(self):
        return self.energy

    def add_energy(self, addition):
        self.energy += addition

    def spend_money(self, cost):
        self.money -= cost

    def get_money(self):
        return self.money

    def get_position(self):
        return self.position
