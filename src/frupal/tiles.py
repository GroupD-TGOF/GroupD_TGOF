"""
Jonathan Sabini 3/12/2020
"""
from string import capwords


# Base Tile Class - holds most data
class Tile:
    # Defines data for tiles
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
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
        self.tool_eng = tool_eng
        self.used = False

    # Gets the color of a tile
    def get_color(self):
        return self.color

    # Gets the name of a tile
    def get_name(self):
        return self.title

    # Gets the energy of a tile based on whether player has tool or not
    def get_energy_req(self, player_inventory: dict):
        if self.tool in player_inventory:
            return self.tool_eng
        else:
            if self.energy_req == 0 and self.title != "water":
                return 1
            else:
                return self.energy_req

    # Gets the stored icon for printout in drawer
    def get_icon(self):
        return self.icon

    # Adds inventory to a tile
    def add_inv(self, item: str):
        if item not in self.inv:
            self.inv.append(item)

    # Grabs the inventory of a tile and returns it, also clears the tile inventory
    def get_inv(self):
        t_inv = self.inv.copy()
        self.inv.clear()
        return t_inv

    # Determine if an item is in the tile inventory
    def has_item(self, item: str):
        return item in self.inv

    # Determine the seen status of a tile
    def seen_status(self):
        return self.is_seen

    # Set the Seen Status of a tile
    def seen_set(self, status: bool):
        self.is_seen = status

    # Prints the tile message located near player stats in drawer
    def print_tile(self, player_inventory: dict):
        r_str = ''
        return r_str

    # Determine if the tile has been used
    def has_used(self):
        return self.used

    # Sets the tile to used status
    def used_tile(self):
        self.used = False

    # Determine if the tool passed in matches the tile tool
    def has_tool(self, tool: str):
        return tool in self.tool

    # Get the name of the tool of a tile
    def get_tool(self):
        return self.tool


# Obstacle class inherits all methods from Tile and overrides some, Custom printout for obstacles
class Obstacle(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += capwords(self.tool.replace("_", " ")) + " used!, " + str(self.tool_eng) + " energy was spent!"
        else:
            r_str += "A " + capwords(self.title.replace("_", " ")) + " Blocks Your Path!, " + str(self.energy_req) + \
                     " energy was spent to break the " + capwords(self.title.replace("_", " ")) + " by hand!"
        return r_str

    def used_tile(self):
        self.used = True


# Water class inherits all methods from Tile and overrides some, Custom printout for water info
class Water(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += capwords(self.tool.replace("_", " ")) + " used!, " + str(self.tool_eng) + " energy was spent!"
        else:
            r_str += "You entered this area without a " + capwords(self.tool.replace("_", " ")) \
                     + ", doing so made you spend " + str(self.energy_req) + " energy to swim!"
        return r_str


# Mud class inherits all methods from Tile and overrides some, Custom printout for Mud
class Mud(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += capwords(self.tool.replace("_", " ")) + " used!, " + str(self.tool_eng) + " energy was spent!"
        else:
            r_str += "No " + capwords(self.tool.replace("_", " ")) + " available, " + str(self.energy_req) + \
                     " energy was spent to wallow through the " + capwords(self.title.replace("_", " ")) + "!"
        return r_str


# Troll class inherits all methods from Tile and overrides some, Custom printout for Troll, Player class takes care
# of removing money from the player
class Troll(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def get_energy_req(self, player_inventory: dict):
        return self.energy_req

    def print_tile(self, player_inventory: dict):
        r_str = "HAHAHAHA ALL YOUR MONEY IS MINE NOW< MUAHAHAHAHAHAH"
        return r_str


# Custom class inherits all methods from Tile and overrides some, Custom printout for custom tilesq
class Custom(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def print_tile(self, player_inventory: dict):
        r_str = ''
        if self.tool in player_inventory:
            r_str += capwords(self.tool.replace("_", " ")) + " used!, " + str(self.tool_eng) + " energy was spent!"
        else:
            r_str += "A " + capwords(self.title.replace("_", " ")) + " Blocks Your Path!, " \
                     + str(self.energy_req) + " energy was spent to bypass the " \
                     + capwords(self.title.replace("_", " ")) + "!"
        return r_str
