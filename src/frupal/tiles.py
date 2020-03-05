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
        self.visited = 0

    def get_color(self):
        return self.color

    def get_name(self):
        return self.title

    def get_energy_req(self, player_inventory: dict):
        if self.tool in player_inventory:
            return 1
        else:
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
        return item in self.inv

    def seen_status(self):
        return self.is_seen

    def seen_set(self, status: bool):
        self.is_seen = status

    def print_tile(self, player_inventory: dict):
        r_str = ''
        return r_str

    def has_visited(self):
        return self.visited

    def visit_tile(self, player_inventory):
        if self.tool in player_inventory:
            self.visited += 0

    def has_tool(self, tool):
        return tool in self.tool


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
            return self.energy_req * 2

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + str(self.energy_req) + " energy was spent!"
        else:
            r_str += "You entered this area without a boat, doing so made you spend " + str(
                self.energy_req * 2) + " energy to swim!"
        return r_str


class Mud(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "M"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + "1 energy was spent!"
        else:
            r_str += "No wood plank available, " + str(self.energy_req) + " energy was spent to wallow through the mud!"
        return r_str


class Tree(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "T"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + "1 energy was spent!"
        else:
            r_str += "A Tree Blocks Your Path!, " + str(self.energy_req) + " energy was spent to go around the tree!"
        return r_str

    def visit_tile(self, player_inventory):
        if self.tool in player_inventory:
            self.visited += 1


class Blackberry(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "B"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)
        b_color = [self.color, "magenta"]
        self.color = b_color[randint(0, 1)]

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + "1 energy was spent!"
        else:
            r_str += "A Black Berry Bush Blocks Your Path!, " + str(self.energy_req) + " energy was spent to cut down the bush!"
        return r_str


class Troll(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "T"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def get_energy_req(self, player_inventory: dict):
        return self.energy_req

    def print_tile(self, player_inventory: dict):
        r_str = "HAHAHAHA ALL YOUR MONEY IS MINE NOW< MUAHAHAHAHAHAH"
        return r_str


class Boulder(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        if platform.system() == "Windows":
            icon = "R"
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + "1 energy was spent!"
        else:
            r_str += "A Boulder Blocks Your Path!, " + str(
                self.energy_req) + " energy was spent climbing over the rock!"
        return r_str


class Custom(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += self.tool.capitalize() + " used!, " + "1 energy was spent!"
        else:
            r_str += "A " + self.title.capitalize() + " Blocks Your Path!, " + str(self.energy_req) + " energy was " \
                                                                                                      "spent to go around it!"
        return r_str
