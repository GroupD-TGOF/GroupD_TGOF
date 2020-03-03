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
        self.map_size = [0, 0]
        self.energy = 0
        self.money = 0
        self.position = [0, 0]
        self.inventory = []

    def update_player(self, config: Config, debug):
        self.map_size = [config.get_map('width'), config.get_map('height')]
        if not debug:
            self.energy = config.get_player('energy')
            self.money = config.get_player('money')
            self.position = [config.get_player('p_c'), config.get_player('p_r')]
        else:
            self.energy = 100
            self.money = 100
            self.position = [config.get_map('width') // 2, config.get_map('height') // 2]

        self.inventory = []

    #               row                        column
    # game_map[self.position[1] + 1][self.position[0] + 1].seen_set(True)
    def player_view(self, view_dist, game_map):
        if not game_map[self.position[1]][self.position[0]].seen_status():
            game_map[self.position[1]][self.position[0]].seen_set(True)
        for i in range(-view_dist, view_dist + 1):
            for j in range(-view_dist, view_dist + 1):
                if (self.position[1] + i > -1 and self.position[0] + j > -1) and \
                        (self.position[1] + i < self.map_size[1] and self.position[0] + j < self.map_size[0]):
                    game_map[self.position[1] + i][self.position[0] + j].seen_set(True)

    # Needs a case for the boundary wall?
    def move(self, direction: Direction, game_map):
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

            # Adjust energy
            self.energy += -(game_map[self.position[1]][self.position[0]].get_energy_req(self.inventory))
            if game_map[self.position[1]][self.position[0]].get_name() == 'troll':
                self.money = self.money // 2

            # Add inventory of Tile to inventory of Player
            if game_map[self.position[1]][self.position[0]].inv:
                self.inventory.extend(game_map[self.position[1]][self.position[0]].get_inv())
            if self.energy < 0:
                self.energy = 0

            view_dist = 1
            if 'binoculars' in self.inventory:
                view_dist = 4
            self.player_view(view_dist, game_map)

    def add_inv(self, item: str, cost: int):
        if self.money >= cost:
            self.money -= cost
            if item == "+10 energy":
                self.energy += 10
            elif item == "+25 energy":
                self.energy += 25
            else:
                self.inventory.append(item)
            return True
        else:
            return False

    def get_energy(self):
        return self.energy

    def get_money(self):
        return self.money

    def get_position(self):
        return self.position

    def has_item(self, item: str):
        return item in self.inventory
