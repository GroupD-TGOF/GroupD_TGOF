

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

        self.map_size()
        self.map_style()
        self.player_stats()

    def map_size(self):
        print("Frupal Settings:")
        print("Set your game map size:")
        print("1. Small (10 x 10)")                                         # Prints size options in ascending order
        print("2. Medium (20 x 20)")
        print("3. Large (20 x 40)")           # User inputs size choice
        while self.map['height'] == 0:                               # Ensures proper input
            self.input_size = int(input("Enter selection (1-3): "))
            if self.input_size == 1:
                self.map["height"] = 10
                self.map["width"] = 10
            elif self.input_size == 2:
                self.map["height"] = 20
                self.map["width"] = 20
            elif self.input_size == 3:
                self.map["height"] = 20
                self.map["width"] = 40
            else:
                print("Must be 1, 2, or 3")
        self.map['total'] = self.map['height'] * self.map['width']

    def map_style(self):
        print('Select your game style (Ranked by difficulty)')
        print('1. Park')                                             # Prints map style options ranked by difficulty
        print('2. Forest')
        print('3. Rocky Forest')
        print('4. Rain Forest')
        print('5. Marsh')
        print('6. Rocky Swamp')
        print('7. Quarry')
        while self.map['trees'] == 0:                                    # User inputs difficulty choice
            self.input_style = int(input('Enter Selection (1-7): '))
            if self.input_style == 1:
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 2:
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 3:
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 5)
                self.map['water'] = int(self.map['total'] / 20)
            elif self.input_style == 4:
                self.map['trees'] = int(self.map['total'] / 2)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 10)
                self.map['mud'] = int(self.map['total'] / 10)
            elif self.input_style == 5:
                self.map['trees'] = int(self.map['total'] / 5)
                self.map['boulder'] = int(self.map['total'] / 20)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.input_style == 6:
                self.map['trees'] = int(self.map['total'] / 10)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 6)
                self.map['mud'] = int(self.map['total'] / 2)
            elif self.input_style == 7:
                self.map['trees'] = int(self.map['total'] / 20)
                self.map['boulder'] = int(self.map['total'] / 6)
                self.map['water'] = int(self.map['total'] / 20)
                self.map['mud'] = int(self.map['total'] / 20)
            else:  # default, could also just omit condition or 'if True'
                print("Must be 1-7")                                     # Ensures proper input

    def player_stats(self):
        self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        while self.player['energy'] < 1 or self.player['energy'] > 100:
            print("Must be 1-100")
            self.player['energy'] = int(input("Input your player's starting energy(1-100): "))
        self.player['money'] = int(input("Input your player's starting money(1-100): "))
        while self.player['money'] < 1 or self.player['money'] > 100:
            print("Must be 1-100")
            self.player['money'] = int(input("Input your player's starting money(1-100): "))

    def print_settings(self):
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
            Marsh = 5
            Rocky_Swamp = 6
            Quarry = 7
        print()
        print("Creating a",                                           # Prints map size and style
              Size(self.input_size).name,
              Style(self.input_style).name, ":")
        print(self.map['trees'], "trees,",                     # Prints quantity of each tile user can expect to find
              self.map['boulder'], "boulders,",
              self.map['water'], "sqrft of water, and",
              self.map['mud'], "sqrft of mud....")
        print("Creating your player:")  # Prints user starting energy and money
        print(self.player['energy'], "starting energy and",
              self.player['money'], "starting Ethereum.")
        print("Good Luck!")


config = Config()
config.print_settings()
