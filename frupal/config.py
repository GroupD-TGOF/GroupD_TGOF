import json
import os
import enum


class Config:
    static = None

    def get_map(self, k: str):  # Defines get function for Map Library
        return self.map[k]

    def get_player(self, k: str):  # Defines get function for Player Stats Library
        return self.player[k]

    def __init__(self):
        self.map = {  # Creates Map Library
            'total': 100,  # Initializes map dimensions
            'height': 10,
            'width': 10,
            'tree': 1,  # Initializes tile quantities
            'blackberry': 1,
            'boulder': 1,
            'water': 1,
            'mud': 1,
            'troll': 1
        }
        self.player = {  # Creates Player Library
            'energy': 15,  # Initializes player stats
            'money': 15,
            'p_x': 0,
            'p_y': 0

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

    def create_config(self):  # Function saves settings to config file
        total = {
            "player": self.player,
            "map": self.map,
            "map_Input": self.map_Input
        }
        f = open(self.conf, "w")
        f.write(json.dumps(total))
        f.close()

    def load_config(self):  # Function loads previous settings from file
        try:
            with open(self.conf) as file:  # Open file
                total = file.read()  # Import data to string
                total = json.loads(total)  # Parse string to "total" library
                self.player = total["player"]  # Transfer total library to indiv libraries
                self.map = total["map"]
                self.map_Input = total["map_Input"]
                return True  # If file exists return true
        except FileNotFoundError:
            return False  # If file does not exist yet return false

    def change_config(self):
        if self.load_config():  # Opens Config File
            self.print_config()  # Display Config Data
            input_config = input("Do you want to use your previous settings? (y or n): ")
            while input_config != "y" and input_config != "n":
                input_config = input("Do you want to use your previous settings? (y or n): ")
            if input_config == 'y':
                print("Moving Back to Main Menu...")
                print("Good Luck!")
                return  # If user keeps settings, return to main
            else:
                self.map_Input['size'] = 0  # If user wants new settings, reset inputs
                self.map_Input['style'] = 0

        self.map_size()  # Calls function to set new Map Dimensions
        self.map_style()  # Calls function to set new Map Tile quantities
        self.player_stats()  # Calls function to set new Player stats
        self.create_config()  # Calls function to save to config file
        self.print_config()  # Calls function to display new settings
        print("Moving Back to Main Menu...")
        print("Good Luck!")

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
                self.map['tree'] = int(self.map['total'] * 0.20)
                self.map['boulder'] = int(self.map['total'] * 0.05)
                self.map['water'] = int(self.map['total'] * 0.05)
                self.map['blackberry'] = int(self.map['total'] * 0.05)
                self.map['mud'] = int(self.map['total'] * 0)
                self.map['trolls'] = int(self.map['total'] * 0)
            elif self.map_Input['style'] == 2:  # Forest: trees 40%, bbush 10%, boulders 5%, water 5%, trolls 1%, mud 0%
                self.map['tree'] = int(self.map['total'] * 0.40)
                self.map['blackberry'] = int(self.map['total'] * 0.10)
                self.map['boulder'] = int(self.map['total'] * 0.05)
                self.map['water'] = int(self.map['total'] * 0.05)
                self.map['mud'] = int(self.map['total'] * 0)
                self.map['trolls'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 3:  # RockyForest: trees 40%, bbush 20%, boulders 20%, water 5%, trolls
                # 1%, mud 0%
                self.map['tree'] = int(self.map['total'] * 0.40)
                self.map['blackberry'] = int(self.map['total'] * 0.20)
                self.map['boulder'] = int(self.map['total'] * 0.20)
                self.map['water'] = int(self.map['total'] * 0.05)
                self.map['mud'] = int(self.map['total'] * 0)
                self.map['trolls'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 4:  # RainForest: trees 50%, bbush 10%, boulders 5%, water 10%, mud 10%,
                # trolls 1%
                self.map['tree'] = int(self.map['total'] * 0.50)
                self.map['blackberry'] = int(self.map['total'] * 0.10)
                self.map['boulder'] = int(self.map['total'] * 0.05)
                self.map['water'] = int(self.map['total'] * 0.10)
                self.map['mud'] = int(self.map['total'] * 0.10)
                self.map['trolls'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 5:  # Bog: trees 20%, bbush 5%, boulders 5%, water 20%, mud 40%, trolls 1%
                self.map['tree'] = int(self.map['total'] * 0.20)
                self.map['blackberry'] = int(self.map['total'] * 0.05)
                self.map['boulder'] = int(self.map['total'] * 0.05)
                self.map['water'] = int(self.map['total'] * 0.20)
                self.map['mud'] = int(self.map['total'] * 0.40)
                self.map['trolls'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 6:  # StonySwamp: trees 10%, bbush 2%, boulders 20%, water 20%, mud 40%,
                # trolls 1%
                self.map['tree'] = int(self.map['total'] * 0.10)
                self.map['blackberry'] = int(self.map['total'] * 0.02)
                self.map['boulder'] = int(self.map['total'] * 0.20)
                self.map['water'] = int(self.map['total'] * 0.20)
                self.map['mud'] = int(self.map['total'] * 0.40)
                self.map['trolls'] = int(self.map['total'] * 0.01)
            elif self.map_Input['style'] == 7:  # Quarry: trees 5%, bbush 2%, boulders 50%, water 10%, mud 5%, trolls 1%
                self.map['tree'] = int(self.map['total'] * 0.05)
                self.map['blackberry'] = int(self.map['total'] * 0.02)
                self.map['boulder'] = int(self.map['total'] * 0.50)
                self.map['water'] = int(self.map['total'] * 0.10)
                self.map['mud'] = int(self.map['total'] * 0.05)
                self.map['trolls'] = int(self.map['total'] * 0.01)
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
                 "(S) Map Size: " + '(' + str(self.map['height']) + "x" + str(
                     self.map['width']) + ' SQ. Yards) or ' + str(
                     self.map['total']) + " Tiles", "Water: " + str(self.map['water']) + " SQ. Yards",
                 "Mud: " + str(self.map['mud']) + " SQ. Yards", "Trees: " + str(self.map['tree']) + " SQ. Yards",
                 "Blackberry Bushes: " + str(self.map['blackberry']) + " SQ. Yards",
                 "Boulders: " + str(self.map['boulder']) + " SQ. Yards",
                 "Troll(s): " + str(self.map['troll']) + " SQ. Yards", "\n", "(Q) Exit Config"]

        return r_str
