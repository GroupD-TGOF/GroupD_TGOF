from random import randint
import platform


class Tile:
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if debug:
            self.is_seen = True
        else:
            self.is_seen = False
        self.title = title
        self.energy_req = energy_req
        self.icon = icon
        self.color = color
        self.inv = []
        self.tool = tool

    def get_color(self):
        return self.color

    def get_name(self):
        return self.title

    def get_energy_req(self, player_inventory: dict):
        return self.energy_req

    def get_icon(self):
        return self.icon

    def add_inv(self, item: str):
        if item not in self.inv:
            self.inv.append(item)

    def get_inv(self):
        t_inv = self.inv.copy()
        self.inv.clear()
        return t_inv

    def has_item(self, item: str):
        if item in self.inv:
            return True
        else:
            return False

    def seen_status(self):
        return self.is_seen

    def seen_set(self, status: bool):
        self.is_seen = status

    def print_tile(self, player_inventory: dict):
        r_str = ''
        return r_str


class Water(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "W"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)  # the water_type also represent the energy
        # requirements

    def get_energy_req(self, player_inventory: dict):  # if the tile is water, calling get_energy will call this method
        if self.tool in player_inventory:
            return self.energy_req
        else:
            temp_energy = self.energy_req * 2  # without a boat the energy requirements is doubles
            return temp_energy

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            return r_str
        else:
            r_str += "You entered this area without a boat, doing so made you spend " + str(
                self.energy_req * 2) + " energy!"
            return r_str


class Mud(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "M"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)
        self.plank = False

    def get_energy_req(self, player_inventory: dict):
        if not self.plank:  # check self whether a wood plank has been place here or not
            if self.tool in player_inventory:  # no plank has been place, check player bag for the planks
                self.plank = True  # available plank will be placed
                return 1
            else:
                return self.energy_req
        else:
            return 1  # if player returns to this tile, wood plank has been place so return 1

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if not self.plank:
            if self.tool in player_inventory:
                r_str += "Wood plank used!, 1 energy was spent!"
                return r_str
            else:
                r_str += "No wood plank available, " + str(self.energy_req) + " energy was spent!"
                return r_str
        return r_str


class Tree(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "T"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)
        self.tree_status = True  # the tree is chopper down for False, and standing for True

    def get_energy_req(self, player_inventory: dict):
        if self.tree_status:
            if self.tool in player_inventory:
                self.tree_status = False
                return 1
            else:
                return self.energy_req
        else:
            return 1

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tree_status:
            if self.tool in player_inventory:
                r_str += "Path is cleared, 1 energy was spent!"
                return r_str
            else:
                r_str += "A Tree Blocks Your Path!, " + str(self.energy_req) + " energy was spent!"
                return r_str
        return r_str


class Blackberry(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "B"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)
        self.bush_status = True  # the bush is cleared if false,
        b_color = ["red", "magenta"]
        self.color = b_color[randint(0, 1)]

    def get_energy_req(self, player_inventory: dict):
        if self.bush_status:
            if self.tool in player_inventory:
                self.bush_status = False
                return 1
            else:
                return 2
        else:
            return 1

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.bush_status:
            if self.tool in player_inventory:
                r_str += "Path is cleared, 1 Energy was spent"
                return r_str
            else:
                r_str += "A Black Berry Bush Blocks Your Path!, " + str(self.energy_req) + " energy was spent!"
            return r_str
        return r_str


class Troll(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "T"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def get_energy_req(self, player_inventory: dict):
        return 1

    def print_tile(self, player_inventory: dict):
        r_str = "HAHAHAHA ALL YOUR MONEY IS MINE NOW< MUAHAHAHAHAHAH"
        return r_str


class Boulder(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "R"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = "A Boulder Blocks Your PAth!, " + str(self.energy_req) + " energy was spent climbing over!"
        return r_str


class Custom(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = "A " + self.title.capitalize() + " Blocks Your Path!, " + str(self.energy_req) + " energy was " \
            "spent to go around it!"
        return r_str
