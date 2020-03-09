from platform import system
import json
import os
import enum


class Config:
    def __init__(self):
        self.player = {  # Creates Player Library
            'energy': 25,  # Initializes player stats
            'money': 25,  # Initializes player energy
            'p_r': 0,  # Initializes player position rows
            'p_c': 0  # Initializes player position columns
        }

        self.map = {  # Creates Map Library
            'total': 100,  # Initializes map dimensions
            'height': 10,  # Initializes map height
            'width': 10,  # Initializes map width
            'jewel_var': 400
        }

        # Initialize Base Tiles with energy, counts, icons, color, and tools and their names and prices
        self.tiles = {
            'tree': {'type': 'obs', 'energy_req': 3, 'count': 20, 'icon': u"\u25B2", 'color': 'green',
                     'tool': {'name': 'axe', 'energy': 1, 'price': 15}},
            'blackberry': {'type': 'tile', 'energy_req': 2, 'count': 5, 'icon': u"\u25C9", 'color': 'magenta',
                           'tool': {'name': 'shears', 'energy': 1, 'price': 10}},
            'boulder': {'type': 'obs', 'energy_req': 5, 'count': 5, 'icon': u"\u25CF", 'color': 'white',
                        'tool': {'name': 'pickaxe', 'energy': 1, 'price': 15}},
            'water': {'type': 'tile', 'energy_req': 2, 'count': 5, 'icon': u"\u25A0", 'color': 'blue',
                      'tool': {'name': 'boat', 'energy': 0, 'price': 20}},
            'mud': {'type': 'tile', 'energy_req': 2, 'count': 0, 'icon': u"\u25A7", 'color': 'yellow',
                    'tool': {'name': 'wood_planks', 'energy': 1, 'price': 10}},
            'troll': {'type': 'tile', 'energy_req': 1, 'count': 0, 'icon': u"\u25A0", 'color': 'green',
                      'tool': {'name': 'Feet', 'energy': 1, 'price': 0}}
        }

        self.map_Input = {  # Creates Input Library
            'style': 1,  # Initializes Input variables
            'size': 1  # Initializes Input variables
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

    def get_player(self, k):  # Defines get function for Player Stats Library
        return self.player[k]

    def get_map(self, k):  # Defines get function for Map Library
        return self.map[k]

    def get_tile(self, k):  # Defines get function for Tiles Library
        info = self.tiles[k]
        if system() == "Windows":
            if k == 'tree':
                info['icon'] = 'T'
            elif k == 'blackberry':
                info['icon'] = 'B'
            elif k == 'boulder':
                info['icon'] = 'R'
            elif k == 'water':
                info['icon'] = 'W'
            elif k == 'mud':
                info['icon'] = 'M'
            elif k == 'troll':
                info['icon'] = 'L'
        return info

    def get_tiles(self):  # Defines get function for Tiles Library to get list of tiles
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

    def reset_config(self):
        os.remove(self.conf)
        self.create_config()

    def map_size(self):  # Function sets Map size
        self.map_Input['size'] = 0
        # Prints size options in ascending order
        print("Frupal Settings:\n" + "Set your game map size:\n" + "1. Small (10 x 10)\n" + "2. Medium (20 x 20)\n"
              + "3. Large (30 x 30)\n" + "4. Custom (N x N)\n")

        while self.map_Input['size'] == 0:  # User inputs size choice (H X W)
            try:
                self.map_Input['size'] = int(input("Enter selection (1-4): "))
            except ValueError:
                print("Input Error: ")
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
                height = 0
                while height < 2 or height > 35:
                    try:
                        height = int(input("Enter Height(2-35): "))
                    except ValueError:
                        pass
                    if height > 1 or height < 36:
                        self.map["height"] = height
                    else:
                        print("Must be 2-35")
                width = 0
                while width < 2 or width > 50:
                    try:
                        width = int(input("Enter Width(2-50): "))
                    except ValueError:
                        pass
                    if width > 1 or width < 51:
                        self.map["width"] = width
                    else:
                        print("Must be 2-50")
            else:  # Bad input
                print("Must be 1-4")
                self.map_Input['size'] = 0
            self.map['total'] = self.map['height'] * self.map['width']

    def jewel_change(self):
        jewels = -1
        change = True
        yn = ""
        while yn != 'y' and yn != 'n':
            yn = input("Edit the Jewel Probability? (y or n): ").lower()
        if yn == 'n':
            change = False
        if change:
            while jewels < 0 or jewels > self.map['total']:
                try:
                    print("Reminder: Enter Value that fills the X in 1 in X, so by default its 1 in 200!")
                    jewels = int(input("Enter Jewel Spawn Probability (1-" + str(self.map['total']) + "): "))
                except ValueError:
                    pass
                if jewels > 1 or jewels < self.map["total"]:
                    self.map["jewel_var"] = jewels
                else:
                    print("Must be " + "1-" + str(self.map['total']))

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
        name = False
        existing = True
        tile_f = ''
        while not name:
            tile_f = input("Please enter a tile name: ").lower()
            while 20 < len(tile_f) < 1:
                print("Tile name must be 1-20 characters.")
                input("Please enter a tile name: ")
            if tile_f not in self.tiles:
                yn = ""
                while yn != 'y' and yn != 'n':
                    yn = input("Tile not in library. Create new? (y or n): ").lower()
                    if yn == 'y':
                        name = True
                        existing = False
                        self.tiles[tile_f] = {'energy_req': 1, 'count': 0, 'icon': u"\u25A0", 'color': 'green',
                                              'tool': {'name': ' ', 'price': 0}}
                        print("Creating a new Tile...")
            else:
                name = True

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Tile Icon on the Map? (y or n): ").lower()
            if yn == 'n':
                change = False
        if change:
            icon = ''
            while len(icon) != 1:
                icon = input("Please Enter the Tile Icon(Single Character, ie: T,&,*,8,etc...): ").capitalize()
            self.tiles[tile_f]['icon'] = icon

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Color of the Icon on the Map? (y or n): ").lower()
            if yn == 'n':
                change = False
        if change:
            color = ""
            while color != 'red' and color != 'green' and color != 'yellow' and color != 'blue' and color != 'black' \
                    and color != 'magenta' and color != 'cyan' and color != 'white':
                color = input(
                    "Please Enter the Tile Color(red, green, yellow, blue, black, magenta, cyan, or white): ").lower()
            self.tiles[tile_f]['color'] = color

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Energy Requirements? (y or n): ").lower()
            if yn == 'n':
                change = False
        if change:
            energy = 0
            while energy < 1 or energy > 10:
                try:
                    energy = int(input("Please Enter the Energy Requirement(1-10): "))
                except ValueError:
                    pass
                if energy < 1 or energy > 10:
                    print("Input Error: Must be 1-10")
            self.tiles[tile_f]['energy_req'] = energy

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Tile Type? (y or n): ").lower()
            if yn == 'n':
                change = False
        if change:
            choice = 0
            while 1 > choice > 2:
                try:
                    choice = int(
                        input("Please Enter the Tile Type (1 for Removable Obstacle, 2 for Immovable Object): "))
                except ValueError:
                    pass
                if 1 > choice > 2:
                    print("Must be a 1 or 0!")
            if choice == 1:
                self.tiles[tile_f]['type'] = 'obs'
            elif choice == 2:
                self.tiles[tile_f]['type'] = 'tile'
            else:
                pass
            change = True

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit Applicable Tool Name? (y or n): ").lower()
                if yn == 'n':
                    change = False
        if change:
            tool = input("Please Enter the Tool Name: ").lower()
            while 20 < len(tool) < 1:
                print("Tool Name must be 1-20 Characters.")
                tool = input("Please Enter the Tool Name: ").lower()
            self.tiles[tile_f]['tool']['name'] = tool

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Tool Energy Requirements? (y or n): ").lower()
                if yn == 'n':
                    change = False
        if change:
            req = -1
            while req < 0 or req > 5:
                try:
                    req = int(input("Please Enter the Tool Energy Requirement(0-5): "))
                except ValueError:
                    pass
                if 0 > req > 5:
                    print("Input Error: Must be 0-5")
                    self.tiles[tile_f]['tool']['energy'] = req

        change = True
        if existing:
            yn = ""
            while yn != 'y' and yn != 'n':
                yn = input("Edit the Tool Price? (y or n): ").lower()
                if yn == 'n':
                    change = False
        if change:
            price = 0
            while price < 1 or price > 100:
                try:
                    price = int(input("Please Enter the Tool Price(1-100): "))
                except ValueError:
                    pass
                if price < 1 or price > 100:
                    print("Input Error: Must be 1-100")
                self.tiles[tile_f]['tool']['price'] = price

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
        self.map_Input['style'] = 0
        # Prints map style options ranked by difficulty
        print('Select your game style (Ranked by difficulty)\n' + '1. Park\n' + '2. Forest\n' + '3. Rocky Forest\n'
              + '4. Rain Forest\n' + '5. Bog\n' + '6. Stony Swamp\n' + '7. Quarry\n' + "8. Custom\n")

        while self.map_Input['style'] == 0:  # User inputs difficulty choice
            try:
                self.map_Input['style'] = int(input('Enter Selection (1-8): '))
            except ValueError:
                pass
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
                sum_t = self.map['total'] + 1
                count = -1
                print("(Reminder: When entering individual tile quantities, total tiles cannot exceed maximum allowed:",
                      self.map['total'], ")")
                while sum_t > self.map['total']:
                    sum_t = 0
                    for i, tile in enumerate(self.tiles):
                        while count == -1:
                            try:
                                count = int(input("Enter " + tile.capitalize() + " Count: "))
                            except ValueError:
                                print("Must be an integer less than", self.map['total'])
                        counts[i] = count
                        count = -1
                        sum_t += counts[i]
                    if sum_t <= self.map['total']:
                        for i, tile in enumerate(self.tiles):
                            self.tiles[tile]['count'] = counts[i]
                    else:
                        print("Your entries for tile counts exceeds maximum allowed tiles:", self.map['total'])
                        self.map_Input['style'] = 0
            else:  # default, for bad input
                print("Must be 1-8")
                self.map_Input['style'] = 0

    def change_stats(self):  # Function sets player stats
        energy = 0
        change = True
        yn = ""
        while yn != 'y' and yn != 'n':
            yn = input("Edit the Player's Starting Energy? (y or n): ").lower()
        if yn == 'n':
            change = False
        if change:
            while energy < 1 or energy > 100:
                try:
                    energy = int(
                        input("Input your player's starting energy(1-100): "))  # User inputs Energy
                except ValueError:
                    pass
                if isinstance(energy, int) and (energy < 1 or energy > 100):
                    print("Input Error: Must be 1-100")
            self.player['energy'] = energy
        money = 0
        change = True
        yn = ""
        while yn != 'y' and yn != 'n':
            yn = input("Edit the Player's Starting Money? (y or n): ").lower()
        if yn == 'n':
            change = False
        if change:
            while money < 1 or money > 100:
                try:
                    money = int(
                        input("Input your player's starting money(1-100): "))  # User inputs Money
                except ValueError:
                    pass
                if isinstance(money, int) and (money < 1 or money > 100):
                    print("Input Error: Must be 1-100")
            self.player['money'] = money

    def change_price(self):
        change = True
        yn = ""
        while yn != 'y' and yn != 'n':
            yn = input("Edit the price of the Binoculars? (y or n): ").lower()
        if yn == 'n':
            change = False
        if change:
            self.store['binoculars'] = int(input("Please Enter A New Price: "))

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

        r_str = ["Player's Statistics: ",
                 "(Press P) Starting Energy: " + str(self.player['energy']),
                 "(Press P) Starting Money: " + str(self.player['money']),
                 "^",

                 "Map Statistics: ",
                 "(Press S) Map Type: " + Size(self.map_Input['size']).name + " " + Type(self.map_Input['style']).name,
                 "(Press S) Map Size: " + '(' + str(self.map['height']) + "x" + str(self.map['width']) +
                 ' SQ. Yards) or ' + str(self.map['total']) + " Tiles!",
                 "(Press S) Jewels: 1 in " + str(self.map['jewel_var']),
                 "^",

                 'Tile Statistics: ']
        for key in self.tiles:
            r_str.append(
                "(Press T) " + str(key).replace('_', ' ').capitalize()
                + ": " + str(self.tiles[key]['count']) + " SQ. Yards, " + "Type: " + self.tiles[key]['type'] + ", "
                + "Energy Req: " + str(self.tiles[key]['energy_req']) + ", Icon: " + str(self.tiles[key]['icon'])
                + ", Color: " + str(self.tiles[key]['color']).capitalize())
            r_str.append("Tool Name: " + self.tiles[key]['tool']['name'].capitalize() + ", Energy Requirement: " +
                         str(self.tiles[key]['tool']['energy']) + ", Tool Price: $" +
                         str(self.tiles[key]['tool']['price']))
        r_str.append("^")
        r_str.append("(Press B) Change Binocular Price! (Price: $" + str(self.store['binoculars']) + ")")
        r_str.append("^")
        r_str.append("(Press C) Clear the ConFig File and Recreate File!")
        r_str.append("^")
        r_str.append("(Press R) Exit Config and Return To Main Menu!")

        return r_str
