from string import capwords


class Tile:
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

    def get_color(self):
        return self.color

    def get_name(self):
        return self.title

    def get_energy_req(self, player_inventory: dict):
        if self.tool in player_inventory:
            return self.tool_eng
        else:
            if self.energy_req == 0 and self.title != "water":
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

    def has_used(self):
        return self.used

    def used_tile(self):
        self.used = False

    def has_tool(self, tool: str):
        return tool in self.tool

    def get_tool(self):
        return self.tool


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


class Troll(Tile):
    def __init__(self, title: str, energy_req: int, icon, color: str, tool: str, tool_eng: int, debug: bool):
        Tile.__init__(self, title, energy_req, icon, color, tool, tool_eng, debug)

    def get_energy_req(self, player_inventory: dict):
        return self.energy_req

    def print_tile(self, player_inventory: dict):
        r_str = "HAHAHAHA ALL YOUR MONEY IS MINE NOW< MUAHAHAHAHAHAH"
        return r_str


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
