import json
import enum


class Config:
    static = None

    # @staticmethod
    def get_map(self, k):                                                      # Defines get function for Map Library
        return self.map[k]

    # @staticmethod
    def get_player(self, k):                                                   # Defines get function for Player Stats Library
        return self.player[k]

    def __init__(self):
        self.map = {                                                     # Creates Map Library
            'total': 0,                                                  # Initializes map dimensions
            'height': 0,
            'width': 0,
            'trees': 0,                                                  # Initializes tile quantities
            'boulders': 0,
            'water': 0,
            'mud': 0
        }
        self.player = {                                                  # Creates Player Library
            'energy': 0,                                                 # Initializes player stats
            'money': 0
        }
        self.map_Input = {                                               # Creates Input Library
            'style': 0,                                                  # Initializes Input variables
            'size': 0
        }

        if self.load_config():                                           # Opens Config File
            self.print_config()                                          # Display Config Data
            input_config = input("Do you want to use your previous settings? (y or n): ")
            while input_config != "y" and input_config != "n":
                input_config = input("Do you want to use your previous settings? (y or n): ")
            if input_config == 'y':
                print("Starting game...")
                print("Good Luck!")
                return                                                   # If user keeps settings, return to main
            else:
                self.map_Input['size'] = 0                               # If user wants new settings, reset inputs
                self.map_Input['style'] = 0

        self.map_size()                                                  # Calls function to set new Map Dimensions
        self.map_style()                                                 # Calls function to set new Map Tile quantities
        self.player_stats()                                              # Calls function to set new Player stats
        self.create_config()                                             # Calls function to save to config file
        self.print_config()                                              # Calls function to display new settings
        print("Starting game...")
        print("Good Luck!")

    def create_config(self):                                             # Function saves settings to config file
        total = {
            "player": self.player,
            "map": self.map,
            "map_Input": self.map_Input
        }
        f = open("config.txt", "w")
        f.write(json.dumps(total))
        f.close()

    def load_config(self):                                               # Function loads previous settings from file
        try:
            with open("config.txt") as file:                             # Open file
                total = file.read()                                      # Import data to string
                total = json.loads(total)                                # Parse string to "total" library
                self.player = total["player"]                            # Transfer total library to indiv libraries
                self.map = total["map"]
                self.map_Input = total["map_Input"]
                return True                                              # If file exists return true
        except FileNotFoundError:
            print("This is your first time playing! Let's set up a map:")
            return False                                                 # If file does not exist yet return false

    def map_size(self):                                                  # Function sets Map size
        print("Frupal Settings:")
        print("Set your game map size:")                                 # Prints size options in ascending order
        print("1. Small (10 x 10)")
        print("2. Medium (20 x 20)")
        print("3. Large (20 x 40)")
        while self.map_Input['size'] == 0:                               # User inputs size choice (H X W)
            self.map_Input['size'] = int(input("Enter selection (1-3): "))
            if self.map_Input['size'] == 1:                              # Small 10 x 10
                self.map["height"] = 10
                self.map["width"] = 10
            elif self.map_Input['size'] == 2:                            # Medium 20 x 20
                self.map["height"] = 20
                self.map["width"] = 20
            elif self.map_Input['size'] == 3:                            # Large 20 x 40
                self.map["height"] = 20
                self.map["width"] = 40
            else:                                                        # Bad input
                print("Must be 1, 2, or 3")
        self.map['total'] = self.map['height'] * self.map['width']

    def map_style(self):                                                 # Function sets Map style
        print('Select your game style (Ranked by difficulty)')           # Prints map style options ranked by difficulty
        print('1. Park')
        print('2. Forest')
        print('3. Rocky Forest')
        print('4. Rain Forest')
        print('5. Bog')
        print('6. Stony Swamp')
        print('7. Quarry')
        while self.map_Input['style'] == 0:                    # User inputs difficulty choice
            self.map_Input['style'] = int(input('Enter Selection (1-7): '))
            if self.map_Input['style'] == 1:                   # Park: trees 20%, boulders 5%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.map_Input['style'] == 2:                 # Forest: trees 50%, boulders 5%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.map_Input['style'] == 3:                 # RockyForest: trees 50%, boulders 20%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 5)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.map_Input['style'] == 4:                 # RainForest: trees 50%, boulders 5%, water 10%, mud 10%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 10)
                self.map['mud'] = int(self.map['total'] / 10)
            elif self.map_Input['style'] == 5:                 # Bog: trees 20%, boulders 5%, water 20%, mud 50%
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.map_Input['style'] == 6:                 # StonySwamp: trees 10%, boulders 20%, water 20%, mud 50%
                self.map['trees'] = int(self.map['total'] / 10)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.map_Input['style'] == 7:                 # Quarry: trees 5%, boulders 33%, water 10%, mud 5%
                self.map['trees'] = int(self.map['total'] / 20)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 20)
                self.map['mud'] = int(self.map['total'] / 20)
            else:                                              # default, for bad input
                print("Must be 1-7")

    def player_stats(self):                                    # Function sets player stats
        self.player['energy'] = int(input("Input your player's starting energy(1-100): "))       # User inputs Energy
        while self.player['energy'] < 1 or self.player['energy'] > 100:
            print("Must be 1-100")
            self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        self.player['money'] = int(input("Input your player's starting money(1-100): "))         # User inputs Money
        while self.player['money'] < 1 or self.player['money'] > 100:
            print("Must be 1-100")
            self.player['money'] = int(input("Input your player's starting money(1-100): "))

    def print_config(self):

        class Size(enum.Enum):                                 # Creates enum classes for print_settings
            Small = 1
            Medium = 2
            Large = 3

        class Style(enum.Enum):
            Park = 1
            Forest = 2
            Rocky_Forest = 3
            Rain_Forest = 4
            Bog = 5
            Stony_Swamp = 6
            Quarry = 7

        print()
        print("Loading your player's stats:")                  # Prints user starting energy and money
        print(self.player['energy'], "starting energy and",
              self.player['money'], "starting Ethereum.")
        print()
        print("Loading your map data:")
        print(Size(self.map_Input['size']).name,
              Style(self.map_Input['style']).name,
              '(', self.map['height'], "x", self.map['width'], ' sq. yards) with',
              self.map['trees'], "trees,",                     # Prints quantity of each tile user can expect to find
              self.map['boulder'], "boulders,",
              self.map['water'], "sq. yards of water, and",
              self.map['mud'], "sq. yards of mud....")


config = Config()
