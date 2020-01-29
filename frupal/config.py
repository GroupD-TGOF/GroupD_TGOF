from enum import Enum


class Config:
    static = None

    class Size(Enum):
        Small = 1
        Medium = 2
        Large = 3

    class Style(Enum):
        Park = 1
        Forest = 2
        Rocky_Forest = 3
        Rain_Forest = 4
        Marsh = 5
        Rocky_Swamp = 6
        Quarry = 7

    input_size: 0
    difficulty: 0

    def __init__(self):
        self.map = {
            'total': 0,
            'height': 0,
            'width': 0,
            'trees': 0,
            'boulders': 0,
            'water': 0,
            'mud': 0
        }
        self.player = {
            'health': 0,
            'energy': 0,
            'money': 10
        }

    def map_size(self):
        print("1. Small (10 x 10")
        print("2. Medium (20 x 20")
        print("3. Large (20 x 40")
        self.input_size = int(input("input size of map(1-3): "))  # User inputs size choice
        while self.input_size < 1 or self.input_size > 3:
            print("Must be 1, 2, or 3")                           # Ensures proper input
            self.input_size = int(input("input size of map(1-3): "))
            choices = {1: (10, 10),  # Height, width
                       2: (20, 20),
                       3: (20, 40)}
            (self.map["height"],     # Sets map size based on input choice
             self.map["width"]) = choices.get(self.map["input_size"], ('default1', 'default2'))
        self.map["total"] = self.map["height"] * self.map["width"]

    def map_difficulty(self):
        print('1. Park')
        print('2. Forest')
        print('3. Rocky Forest')
        print('4. Rain Forest')
        print('5. Marsh')
        print('6. Rocky Swamp')
        print('7. Quarry')                           # User inputs difficulty choice
        self.difficulty = int(input('Please select what kind of map you would like (ranked by difficult (1-7): '))
        while self.difficulty < 1 or self.difficulty > 7:
            print("Must be 1-7")                     # Ensures proper input
            self.difficulty = int(input('Please select what kind of map you would like (ranked by difficult (1-7): '))
        choices = {1: (int(self.map['total'] / 5),   # Park: trees 20%, boulders 5%, water 5%, mud 0%
                       int(self.map['total'] / 20),  # energy 80%
                       int(self.map['total'] / 20), 0,
                       int(self.map['total'] * .8)),
                   2: (int(self.map['total'] / 2),   # Forest: trees 50%, boulders 5%, water 5%, mud 0%
                       int(self.map['total'] / 20),  # energy 50%
                       int(self.map['total'] / 20), 0,
                       int(self.map['total'] / 2)),
                   3: (int(self.map['total'] / 2),   # RockyForest: trees 50%, boulders 20%, water 5%, mud 0%
                       int(self.map['total'] / 5),   # energy 50%
                       int(self.map['total'] / 20), 0,
                       int(self.map['total'] / 2)),
                   4: (int(self.map['total'] / 2),   # RainForest: trees 50%, boulders 5%, water 10%, mud 10%
                       int(self.map['total'] / 20),  # energy 50%
                       int(self.map['total'] / 10),
                       int(self.map['total'] / 10),
                       int(self.map['total'] / 2)),
                   5: (int(self.map['total'] / 5),   # Marsh: trees 20%, boulders 5%, water 20%, mud 50%
                       int(self.map['total'] / 20),  # energy 80%
                       int(self.map['total'] / 5),
                       int(self.map['total'] / 2),
                       int(self.map['total'] * .8)),
                   6: (int(self.map['total'] / 10),  # RockySwamp: trees 10%, boulders 20%, water 20%, mud 50%
                       int(self.map['total'] / 5),   # energy 80%
                       int(self.map['total'] / 5),
                       int(self.map['total'] / 2),
                       int(self.map['total'] * .8)),
                   7: (int(self.map['total'] / 20),  # Quarry: trees 5%, boulders 33%, water 10%, mud 5%
                       int(self.map['total'] / 3),   # energy 80%
                       int(self.map['total'] / 10),
                       int(self.map['total'] / 20),
                       int(self.map['total'] * .8))
                   }
        (self.map['trees'],         # Selects choice based on input
         self.map['boulder'],
         self.map['water'],
         self.map['mud'],
         self.player['energy']) = choices.get(self.difficulty,
                                              ('default1', 'default2', 'default3', 'default4', 'default5'))

    def print_settings(self, enum):
        print("Creating ",                                # Prints map size and style
              enum.size(self.input_size).name, " ",
              enum.style(self.difficulty).name, "...")
        print(self.map['trees'], " trees, ",              # Prints quantity of each tile user can expect to find
              self.map['boulder'], " boulders, ",
              self.map['water'], " sqrft of water, and ",
              self.map['mud'], " sqrft of mud.")
        print("Creating player with ",                    # Prints user starting energy and money
              self.player['energy'], " starting energy and ",
              self.player['money'], " starting Ethereum.")
