import json
import os
import enum


class Config:
    static = None

    def __init__(self):
        self.player = {  # Creates Player Library
            'energy': 25,  # Initializes player stats
            'money': 25,
            'p_r': 0,
            'p_c': 0

        }

        self.map = {  # Creates Map Library
            'total': 100,  # Initializes map dimensions
            'height': 10,
            'width': 10
        }

        self.tiles = {
            'tree': {'energy_req': 2, 'count': 20, 'icon': u"\u25B2", 'color': 'green'},
            'blackberry': {'energy_req': 2, 'count': 5, 'icon': u"\u25C9", 'color': 'magenta'},
            'boulder': {'energy_req': 2, 'count': 5, 'icon': u"\u25CF", 'color': 'white'},
            'water': {'energy_req': 2, 'count': 5, 'icon': u"\u25A5", 'color': 'blue'},
            'mud': {'energy_req': 5, 'count': 0, 'icon': u"\u25A7", 'color': 'yellow'},
            'troll': {'energy_req': 1, 'count': 0, 'icon': u"\u25A0", 'color': 'green'}
        }

        self.map_Input = {  # Creates Input Library
            'style': 1,  # Initializes Input variables
            'size': 1
        }

        self.store = {
            '+10 energy': 10,
            "+25 energy": 20,
            'boat': 10,
            'binoculars': 15,
            'saw': 25,
            'shears': 10,
            'wood_plank': 5
        }

        self.conf = "config.txt"
        count = 0
        for root, dir, files in os.walk("."):
            if self.conf in files:
                if count < 1:
                    self.conf = os.path.join(root, self.conf)

        if not self.load_config():
            self.create_config()

    def get_map(self, k: str):  # Defines get function for Map Library
        return self.map[k]

    def get_player(self, k: str):  # Defines get function for Player Stats Library
        return self.player[k]

    def get_tile(self, k: str):
        return self.tiles[k]

    def get_tiles(self):
        tiles = []
        for key in self.tiles:
            print(key)
            tiles.append(key)
        return tiles

    def create_config(self):  # Function saves settings to config file
        total = {
            "player": self.player,
            "map": self.map,
            "tiles": self.tiles,
            "map_Input": self.map_Input

        }
        f = open(self.conf, "w")
        f.write(json.dumps(total, indent=2))
        f.close()

    def load_config(self):  # Function loads previous settings from file
        try:
            with open(self.conf) as file:  # Open file
                total = file.read()  # Import data to string
                total = json.loads(total)  # Parse string to "total" library
                self.player = total["player"]  # Transfer total library to indiv libraries
                self.map = total["map"]
                self.map['total'] = self.map['height'] * self.map['width']
                self.tiles = total["tiles"]
                self.map_Input = total["map_Input"]
                return True  # If file exists return true
        except FileNotFoundError:
            return False  # If file does not exist yet return false

    def map_size(self):  # Function sets Map size
        print("Frupal Settings:")
        print("Set your game map size:")  # Prints size options in ascending order
        print("1. Small (10 x 10)")
        print("2. Medium (20 x 20)")
        print("3. Large (30 x 30)")
        while self.map_Input['size'] == 0:  # User inputs size choice (H X W)
            self.map_Input['size'] = int(input("Enter selection (1-3): "))
            if self.map_Input['size'] == 1:  # Small 10 x 10
                self.map["height"] = 10
                self.map["width"] = 10
            elif self.map_Input['size'] == 2:  # Medium 20 x 20
                self.map["height"] = 20
                self.map["width"] = 20
            elif self.map_Input['size'] == 3:  # Large 30 x 30
                self.map["height"] = 30
                self.map["width"] = 30
            else:  # Bad input
                print("Must be 1, 2, or 3")
        self.map['total'] = self.map['height'] * self.map['width']

    def map_style(self):  # Function sets Map style
        print('Select your game style (Ranked by difficulty)')  # Prints map style options ranked by difficulty
        print('1. Park')
        print('2. Forest')
        print('3. Rocky Forest')
        print('4. Rain Forest')
        print('5. Bog')
        print('6. Stony Swamp')
        print('7. Quarry')
        while self.map_Input['style'] == 0:  # User inputs difficulty choice
            self.map_Input['style'] = int(input('Enter Selection (1-7): '))
            if self.map_Input['style'] == 1:  # Park: trees 20%, boulders 5%, bbush 5% water 5%, trolls 0%, mud 0%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.20)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.05)
                self.tiles['water']['count'] = int(self.map['total'] * 0.05)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.05)
                self.tiles['mud']['count'] = int(self.map['total'] * 0)
                self.tiles['troll']['count'] = int(self.map['total'] * 0)
            elif self.map_Input['style'] == 2:  # Forest: trees 40%, bbush 10%, boulders 5%, water 5%, trolls 1%, mud 0%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.40)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.10)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.05)
                self.tiles['water']['count'] = int(self.map['total'] * 0.05)
                self.tiles['mud']['count'] = int(self.map['total'] * 0)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 3:  # RockyForest: trees 40%, bbush 20%, boulders 20%, water 5%, trolls
                # 1%, mud 0%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.40)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.20)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.20)
                self.tiles['water']['count'] = int(self.map['total'] * 0.05)
                self.tiles['mud']['count'] = int(self.map['total'] * 0)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 4:  # RainForest: trees 50%, bbush 10%, boulders 5%, water 10%, mud 10%,
                # trolls 1%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.50)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.10)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.05)
                self.tiles['water']['count'] = int(self.map['total'] * 0.10)
                self.tiles['mud']['count'] = int(self.map['total'] * 0.10)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 5:  # Bog: trees 20%, bbush 5%, boulders 5%, water 20%, mud 40%, trolls 1%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.20)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.05)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.05)
                self.tiles['water']['count'] = int(self.map['total'] * 0.20)
                self.tiles['mud']['count'] = int(self.map['total'] * 0.40)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 6:  # StonySwamp: trees 10%, bbush 2%, boulders 20%, water 20%, mud 40%,
                # trolls 1%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.10)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.02)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.20)
                self.tiles['water']['count'] = int(self.map['total'] * 0.20)
                self.tiles['mud']['count'] = int(self.map['total'] * 0.40)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 7:  # Quarry: trees 5%, bbush 2%, boulders 50%, water 10%, mud 5%, trolls 1%
                self.tiles['tree']['count'] = int(self.map['total'] * 0.05)
                self.tiles['blackberry']['count'] = int(self.map['total'] * 0.02)
                self.tiles['boulder']['count'] = int(self.map['total'] * 0.50)
                self.tiles['water']['count'] = int(self.map['total'] * 0.10)
                self.tiles['mud']['count'] = int(self.map['total'] * 0.05)
                self.tiles['troll']['count'] = int(self.map['total'] * 0.01)
            else:  # default, for bad input
                print("Must be 1-7")

    def player_stats(self):  # Function sets player stats
        self.player['energy'] = int(input("Input your player's starting energy(1-100): "))  # User inputs Energy
        while self.player['energy'] < 1 or self.player['energy'] > 100:
            print("Must be 1-100")
            self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        self.player['money'] = int(input("Input your player's starting money(1-100): "))  # User inputs Money
        while self.player['money'] < 1 or self.player['money'] > 100:
            print("Must be 1-100")
            self.player['money'] = int(input("Input your player's starting money(1-100): "))

    def print_config(self):

        class Size(enum.Enum):  # Creates enum classes for print_settings
            Small = 1
            Medium = 2
            Large = 3

        class Type(enum.Enum):
            Park = 1
            Forest = 2
            Rocky_Forest = 3
            Rain_Forest = 4
            Bog = 5
            Stony_Swamp = 6
            Quarry = 7

        r_str = ["Player's Statistics: ", "(P) Starting Energy: " + str(self.player['energy']),
                 "(P) Starting Money: " + str(self.player['money']), "\n", "Map Statistics: ",
                 "(S) Map Type: " + Size(self.map_Input['size']).name + " " + Type(self.map_Input['style']).name,
                 "(S) Map Size: " + '(' + str(self.map['height']) + "x" + str(self.map['width']) + ' SQ. Yards) or '
                 + str(self.map['total']) + " Tiles"]
        for key in self.tiles:
            r_str.append(str(key).capitalize() + ": " + str(self.tiles[key]['count']) + " SQ. Yards, " + "Energy Req: "
                         + str(self.tiles[key]['energy_req']) + ", Icon: " + str(self.tiles[key]['icon'])
                         + ", Color: " + str(self.tiles[key]['color']).capitalize())
        r_str.append("\n")
        r_str.append("(Q) Exit Config")

        return r_str