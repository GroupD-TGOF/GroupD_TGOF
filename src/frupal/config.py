import json
import os
import enum


class Config:
    static = None

    def __init__(self):
        self.player = {  # Creates Player Library
            'energy': 25,   # Initializes player stats
            'money': 25,    # Initializes player energy
            'p_r': 0,       # Initializes player position rows
            'p_c': 0        # Initializes player position columns
        }

        self.map = {  # Creates Map Library
            'total': 100,   # Initializes map dimensions
            'height': 10,   # Initializes map height
            'width': 10     # Initializes map width
        }

        # Initialize Base Tiles with energy, counts, icons, color, and tools and their names and prices
        self.tiles = {
            'tree': {'energy_req': 2, 'count': 20, 'icon': u"\u25B2", 'color': 'green',
                     'tool': {'name': 'saw', 'price': 25}},
            'blackberry': {'energy_req': 2, 'count': 5, 'icon': u"\u25C9", 'color': 'magenta',
                           'tool': {'name': 'shears', 'price': 10}},
            'boulder': {'energy_req': 2, 'count': 5, 'icon': u"\u25CF", 'color': 'white',
                        'tool': {'name': 'pickaxe', 'price': 25}},
            'water': {'energy_req': 2, 'count': 5, 'icon': u"\u25A0", 'color': 'blue',
                      'tool': {'name': 'boat', 'price': 10}},
            'mud': {'energy_req': 5, 'count': 0, 'icon': u"\u25A7", 'color': 'yellow',
                    'tool': {'name': 'wood_plank', 'price': 5}},
            'troll': {'energy_req': 1, 'count': 0, 'icon': u"\u25A0", 'color': 'green',
                      'tool': {'name': ' ', 'price': 0}}
        }

        self.map_Input = {  # Creates Input Library
            'style': 1,     # Initializes Input variables
            'size': 1       # Initializes Input variables
        }

        # Initialize Store
        self.store = {
            '+10 energy': 10,
            "+25 energy": 20,
            'binoculars': 15,
        }

        # Visit each tile in the tile list and add their tool's name and price to the store
        for tile in self.tiles:
            if not tile == 'troll':
                self.store[self.tiles[tile]['tool']['name']] = self.tiles[tile]['tool']['price']

        # Search for a config file in the file structure
        self.conf = "config.txt"
        count = 0
        for root, direct, files in os.walk("."):
            if self.conf in files:
                if count < 1:
                    self.conf = os.path.join(root, self.conf)

        # If no config create one from defaults above
        if not self.load_config():
            self.create_config()

    def get_map(self, k):  # Defines get function for Map Library
        return self.map[k]

    def get_player(self, k):  # Defines get function for Player Stats Library
        return self.player[k]

    def get_tile(self, k):  # Defines get function for Tiles Library
        return self.tiles[k]

    def get_tiles(self):  # Defines get function for TIles Library to get list of tiles
        tiles = []
        for key in self.tiles:
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
        f.write(json.dumps(total, indent=4))
        f.close()

    def load_config(self):  # Function loads previous settings from file
        try:
            with open(self.conf) as file:  # Open file
                total = file.read()  # Import data to string
                total = json.loads(total)  # Parse string to "total" library
                self.player = total["player"]  # Transfer total library to individual libraries
                self.map = total["map"]
                self.map['total'] = self.map['height'] * self.map['width']
                self.tiles = total["tiles"]
                self.map_Input = total["map_Input"]
                return True  # If file exists return true
        except FileNotFoundError:
            return False  # If file does not exist yet return false

    def map_size(self):  # Function sets Map size
        # Prints size options in ascending order
        print("Frupal Settings:\n" + "Set your game map size:\n" + "1. Small (10 x 10)\n" + "2. Medium (20 x 20)\n"
              + "3. Large (30 x 30)\n" + "4. Custom (N x N)\n")

        while self.map_Input['size'] == 0:  # User inputs size choice (H X W)
            self.map_Input['size'] = int(input("Enter selection (1-4): "))
            if self.map_Input['size'] == 1:  # Small 10 x 10
                self.map["height"] = 10
                self.map["width"] = 10
            elif self.map_Input['size'] == 2:  # Medium 20 x 20
                self.map["height"] = 20
                self.map["width"] = 20
            elif self.map_Input['size'] == 3:  # Large 30 x 30
                self.map["height"] = 30
                self.map["width"] = 30
            elif self.map_Input['size'] == 4:
                self.map["height"] = int(input("Enter Height: "))
                self.map["width"] = int(input("Enter Width: "))
            else:  # Bad input
                print("Must be 1, 2, 3, or 4!")
                self.map_Input['size'] = 0
        self.map['total'] = self.map['height'] * self.map['width']

    def __tile_counts(self, blackberry_count, boulder_count, mud_count, tree_count, troll_count, water_count):
        for tile in self.tiles:
            self.tiles[tile]['count'] = 0
        self.tiles['blackberry']['count'] = int(self.map['total'] * blackberry_count)
        self.tiles['boulder']['count'] = int(self.map['total'] * boulder_count)
        self.tiles['mud']['count'] = int(self.map['total'] * mud_count)
        self.tiles['tree']['count'] = int(self.map['total'] * tree_count)
        self.tiles['troll']['count'] = int(self.map['total'] * troll_count)
        self.tiles['water']['count'] = int(self.map['total'] * water_count)

    def change_tile(self):
        tile_f = input("Please enter a tile name: ").lower()
        if tile_f not in self.tiles:
            self.tiles[tile_f] = {'energy_req': 1, 'count': 0, 'icon': u"\u25A0", 'color': 'green', 'tool': {'name': ' ', 'price': 0}}
        self.tiles[tile_f]['energy_req'] = int(input("Please Enter the Energy Requirement: "))
        self.tiles[tile_f]['icon'] = input("Please Enter the Tile Icon: ")
        self.tiles[tile_f]['color'] = input("Please Enter the Tile Color: ").lower()
        inp = int(input('Do You Want to Change the Tool Properties? (1 - Y, 0 - N): '))
        if inp == 1:
            self.tiles[tile_f]['tool']['name'] = input("Please Enter the Tool Name: ").lower()
            self.tiles[tile_f]['tool']['price'] = int(input("Please Enter the Tool Price: "))

        self.store.clear()

        self.store = {
            '+10 energy': 10,
            "+25 energy": 20,
            'binoculars': 15,
        }

        for tile in self.tiles:
            if not tile == 'troll':
                self.store[self.tiles[tile]['tool']['name']] = self.tiles[tile]['tool']['price']

    def map_style(self):  # Function sets Map style
        # Prints map style options ranked by difficulty
        print('Select your game style (Ranked by difficulty)\n' + '1. Park\n' + '2. Forest\n' + '3. Rocky Forest\n'
              + '4. Rain Forest\n' + '5. Bog\n' + '6. Stony Swamp\n' + '7. Quarry\n' + "8. Custom\n")

        while self.map_Input['style'] == 0:  # User inputs difficulty choice
            self.map_Input['style'] = int(input('Enter Selection (1-8): '))
            if self.map_Input['style'] == 1:
                # Park: trees 20%, boulders 5%, bbush 5% water 5%, trolls 0%, mud 0%
                self.__tile_counts(0.05, 0.05, 0, 0.20, 0, 0.05)
            elif self.map_Input['style'] == 2:
                # Forest: trees 40%, bbush 10%, boulders 5%, water 5%, trolls 1%, mud 0%
                self.__tile_counts(0.10, 0.05, 0, 0.40, 0.01, 0.05)
            elif self.map_Input['style'] == 3:
                # RockyForest: trees 40%, bbush 20%, boulders 20%, water 5%, trolls 1%, mud 0%
                self.__tile_counts(0.20, 0.20, 0, 0.40, 0.01, 0.05)
            elif self.map_Input['style'] == 4:
                # RainForest: trees 50%, bbush 10%, boulders 5%, water 10%, mud 10%, trolls 1%
                self.__tile_counts(0.10, 0.05, 0.10, 0.50, 0.01, 0.10)
            elif self.map_Input['style'] == 5:
                # Bog: trees 20%, bbush 5%, boulders 5%, water 20%, mud 40%, trolls 1%
                self.__tile_counts(0.05, 0.05, 0.40, 0.20, 0.01, 0.20)
            elif self.map_Input['style'] == 6:
                # StonySwamp: trees 10%, bbush 2%, boulders 20%, water 20%, mud 40%, trolls 1%
                self.__tile_counts(0.02, 0.20, 0.40, 0.10, 0.01, 0.20)
            elif self.map_Input['style'] == 7:
                # Quarry: trees 5%, bbush 2%, boulders 50%, water 10%, mud 5%, trolls 1%
                self.__tile_counts(0.02, 0.50, 0.05, 0.05, 0.01, 0.10)
            elif self.map_Input['style'] == 8:
                # Quarry: trees 5%, bbush 2%, boulders 50%, water 10%, mud 5%, trolls 1%
                counts = [0] * len(self.tiles)
                sum_t = 0
                for i, tile in enumerate(self.tiles):
                    counts[i] = int(input("Enter " + tile.capitalize() + " Count: "))
                    sum_t += counts[i]
                if sum_t < self.map['total']:
                    for i, tile in enumerate(self.tiles):
                        self.tiles[tile]['count'] = counts[i]
                else:
                    print("Your entries for tile counts exceeds maximum allowed tiles!")
                    self.map_Input['style'] = 0
            else:  # default, for bad input
                print("Must be 1-8!")
                self.map_Input['style'] = 0

    def change_stats(self, energy, money):  # Function sets player stats
        self.player['energy'] = energy
        self.player['money'] = money

    def print_config(self):

        class Size(enum.Enum):  # Creates enum classes for print_settings
            Small = 1
            Medium = 2
            Large = 3
            Custom = 4

        class Type(enum.Enum):
            Park = 1
            Forest = 2
            Rocky_Forest = 3
            Rain_Forest = 4
            Bog = 5
            Stony_Swamp = 6
            Quarry = 7
            Custom = 8

        r_str = ["Player's Statistics: ", "(Press P) Starting Energy: " + str(self.player['energy']),
                 "(Press P) Starting Money: " + str(self.player['money']), "\n", "Map Statistics: ",
                 "(Press S) Map Type: " + Size(self.map_Input['size']).name + " " + Type(self.map_Input['style']).name,
                 "(Press S) Map Size: " + '(' + str(self.map['height']) + "x" + str(self.map['width']) + ' SQ. Yards) or '
                 + str(self.map['total']) + " Tiles"]
        for key in self.tiles:
            r_str.append(
                "(Press T) " + str(key).replace('_', ' ').capitalize() + ": " + str(self.tiles[key]['count']) + " SQ. Yards, "
                + "Energy Req: " + str(self.tiles[key]['energy_req']) + ", Icon: " + str(self.tiles[key]['icon'])
                + ", Color: " + str(self.tiles[key]['color']).capitalize())
        r_str.append("\n")
        r_str.append("(Press Q) Exit Config")

        return r_str
