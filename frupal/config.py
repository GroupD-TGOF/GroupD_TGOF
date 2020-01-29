from enum import Enum
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

class Config:
    static = None

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
        print("input size of map(1-3): ")
        inputSize = int(raw_input())


        for case in switch(inputSize):
            if case(1):
                self.map["height"] = 10
                self.map["width"] = 10
                break
            if case(2):
                self.map["height"] = 20
                self.map["width"] = 20
                break
            if case(3):
                self.map["height"] = 20
                self.map["width"] = 40
                break
        self.map["total"] = self.map["height"] * self.map["width"]

    def map_difficulty(self):
        print("1. Park")
        print("2. Forest")
        print("3. Rocky Forest")
        print("4. Rain Forest")
        print("5. Marsh")
        print("6. Rocky Swamp")
        print("7. Quarry")
        print("Please select what kind of map you would like (ranked by difficult (1-7): ")
        difficulty: int(raw_input())

        for case in switch(difficulty):
            if case(1):
                self.map['trees'] = self.map['total']/5
                self.map['boulder'] = self.map['total']/20
                self.map['water'] = self.map['total']/20
                self.player['energy'] = self.map['total']*.8
                break
            if case(2):
                self.map['trees'] = self.map['total'] / 2
                self.map['boulder'] = self.map['total'] / 20
                self.map['water'] = self.map['total'] / 20
                self.player['energy'] = self.map['total'] / 2
                break
            if case(3):
                self.map['trees'] = self.map['total'] / 2
                self.map['boulder'] = self.map['total'] / 5
                self.map['water'] = self.map['total'] / 20
                self.player['energy'] = self.map['total'] / 2
                break
            if case(4):
                self.map['trees'] = self.map['total'] / 2
                self.map['boulder'] = self.map['total'] / 20
                self.map['water'] = self.map['total'] / 10
                self.map['mud'] = self.map['total'] / 10
                self.player['energy'] = self.map['total'] / 2
                break
            if case(5):
                self.map['trees'] = self.map['total'] / 5
                self.map['boulder'] = self.map['total'] / 20
                self.map['water'] = self.map['total'] / 6
                self.map['mud'] = self.map['total'] / 2
                self.player['energy'] = self.map['total'] * .8
                break
            if case(6):
                self.map['trees'] = self.map['total'] / 10
                self.map['boulder'] = self.map['total'] / 6
                self.map['water'] = self.map['total'] / 6
                self.map['mud'] = self.map['total'] / 2
                self.player['energy'] = self.map['total'] * .8
                break
            if case(7):
                self.map['trees'] = self.map['total'] / 20
                self.map['boulder'] = self.map['total'] / 6
                self.water['water'] = self.map['total'] / 10
                self.mud['mud'] = self.map['total'] / 20
                self.player['energy'] = self.map['total'] * .8
                break
            if case():  # default, could also just omit condition or 'if True'
                print("something else!")

    def printSettings(self):
        print("Creating " + size(inputSize).name + " " + style(difficulty).name + "...")
        print(self.map['trees'] + " trees, " + self.map['boulder'] + " boulders, " + self.map['water'] + " sqrft of water, and " + self.map['mud'] + " sqrft of mud.")
        