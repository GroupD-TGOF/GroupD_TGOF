import json

class Config:
    static = None

    input_size: 0                                                       # Initializes user inputs
    input_style: 0

    @staticmethod
    def get_map(k):
        return config.map[k]

    @staticmethod
    def get_player(k):
        return config.player[k]

    def __init__(self):
        self.map = {                                                    # Creates Map Library
            'total_tiles_tiles': 0,                                     # Initializes map dimensions and tile quantities
            'height': 0,
            'width': 0,
            'trees': 0,
            'boulders': 0,
            'water': 0,
            'mud': 0
        }
        self.player = {                                                  # Creates Player Library
            'energy': 0,                                                 # Initializes player stats
            'money': 0
        }

        if self.load_config():
            self.print_config()
            self.input_config = input("Do you want to use your previous settings? (y or n): ")
            while self.input_config != 'y' or self.input_config != 'n':
                self.input_config = input("Do you want to use your previous settings? (y or n): ")
            if self.input_config == 'y':
                return

        self.map_size()
        self.map_style()
        self.player_stats()
        self.create_config()
        self.print_config()

    def create_config(self):
        total = {
            "player": self.player,
            "map": self.map
        }
        f = open("config.txt", "w")
        f.write(json.dumps(total))
        f.close()

    def load_config(self):
        try:
            with open("config.txt") as file:
                total = file.read()
                total = json.loads(total)
                self.player = total["player"]
                self.map = total["map"]
                return True
        except FileNotFoundError:
            print("This is your first time playing! Let's set up a map:")
            return False

    def map_size(self):
        print("Frupal Settings:")
        print("Set your game map size:")                               # Prints size options in ascending order
        print("1. Small (10 x 10)")
        print("2. Medium (20 x 20)")
        print("3. Large (20 x 40)")
        while self.map['height'] == 0:                                 # User inputs size choice (H X W)
            self.input_size = int(input("Enter selection (1-3): "))
            if self.input_size == 1:                                   # Small 10 x 10
                self.map["height"] = 10
                self.map["width"] = 10
            elif self.input_size == 2:                                 # Medium 20 x 20
                self.map["height"] = 20
                self.map["width"] = 20
            elif self.input_size == 3:                                 # Large 20 x 40
                self.map["height"] = 20
                self.map["width"] = 40
            else:                                                      # Bad input
                print("Must be 1, 2, or 3")
        self.map['total'] = self.map['height'] * self.map['width']

    def map_style(self):
        print('Select your game style (Ranked by difficulty)')         # Prints map style options ranked by difficulty
        print('1. Park')
        print('2. Forest')
        print('3. Rocky Forest')
        print('4. Rain Forest')
        print('5. Bog')
        print('6. Stony Swamp')
        print('7. Quarry')
        while self.map['trees'] == 0:                                  # User inputs difficulty choice
            self.input_style = int(input('Enter Selection (1-7): '))
            if self.input_style == 1:                                  # Park: trees 20%, boulders 5%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 2:                               # Forest: trees 50%, boulders 5%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 3:                         # RockyForest: trees 50%, boulders 20%, water 5%, mud 0%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 5)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 4:                         # RainForest: trees 50%, boulders 5%, water 10%, mud 10%
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 10)
                self.map['mud'] = int(self.map['total'] / 10)
            elif self.input_style == 5:                                # Bog: trees 20%, boulders 5%, water 20%, mud 50%
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.input_style == 6:                        # StonySwamp: trees 10%, boulders 20%, water 20%, mud 50%
                self.map['trees'] = int(self.map['total'] / 10)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.input_style == 7:                              # Quarry: trees 5%, boulders 33%, water 10%, mud 5%
                self.map['trees'] = int(self.map['total'] / 20)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 20)
                self.map['mud'] = int(self.map['total'] / 20)
            else:                                                    # default, for bad input
                print("Must be 1-7")

    def player_stats(self):
        self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        while self.player['energy'] < 1 or self.player['energy'] > 100:
            print("Must be 1-100")
            self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        self.player['money'] = int(input("Input your player's starting money(1-100): "))
        while self.player['money'] < 1 or self.player['money'] > 100:
            print("Must be 1-100")
            self.player['money'] = int(input("Input your player's starting money(1-100): "))

    def print_config(self):
        import enum

        class Size(enum.Enum):  # Creates enum classes for print_settings
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
        print("Loading your player's stats:")  # Prints user starting energy and money
        print(self.player['energy'], "starting energy and",
              self.player['money'], "starting Ethereum.")
        print()
        print("Transporting your player to a",                                           # Prints map size and style
              Size(self.input_size).name,
              Style(self.input_style).name, ":")
        print(self.map['trees'], "trees,",                     # Prints quantity of each tile user can expect to find
              self.map['boulder'], "boulders,",
              self.map['water'], "sqrft of water, and",
              self.map['mud'], "sqrft of mud....")
        print()
        print("Good Luck!")


config = Config()
config.print_config()
