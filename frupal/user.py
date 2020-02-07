from .player import Direction
from .config import Config
from .drawer import Drawer
import os
import crayons


class User:

    def __init__(self):
        '''
        if os.get_terminal_size().columns != 0 and os.get_terminal_size().lines != 0:
            self.width = os.get_terminal_size().columns
            self.height = os.get_terminal_size().lines

        else:
        '''
        self.width = 40
        self.height = 30
        self.middle = self.height // 2
        self.store = {  # Creates Store Library
            'axe': 1,  # Initializes player stats
            'boat': 1,
        }

    @staticmethod
    def config_menu(config: Config):
        config.print_config()
        config.map_Input['size'] = 0  # If user wants new settings, reset inputs
        config.map_Input['style'] = 0 # If user wants new settings, reset inputs
        config.map_size()  # Calls function to set new Map Dimensions
        config.map_style()  # Calls function to set new Map Tile quantities
        config.player_stats()  # Calls function to set new Player stats
        config.create_config()  # Calls function to save to config file
        config.print_config()

    def main_menu(self, config: Config):
        cont = True
        choice = 1
        while cont:
            for i in range(self.middle - 4):
                print()
            print(crayons.green("The Game of Frupal!".center(self.width)))
            print(crayons.yellow("1. Start Game!".center(self.width)))
            print(crayons.yellow("2. Configuration?".center(self.width)))
            print(crayons.yellow("3. Exit Game.".center(self.width)))
            for i in range(self.middle - 5):
                print()

            choice = int(input("Enter your choice: ".center(self.width)))
            if choice == 1:
                cont = False
            if choice == 2:
                self.config_menu(config)
                cont = True
            if choice == 3:
                cont = False
        if choice == 1 or choice == 2:
            return True
        else:
            return False

    @staticmethod
    def move_menu(player, game_map):
        dir_inp = input("What choice do you want to make (north, east, south, west): ")
        dir_inp = dir_inp.lower()
        if dir_inp == "north":
            direction = Direction.NORTH
        elif dir_inp == "west":
            direction = Direction.WEST
        elif dir_inp == "east":
            direction = Direction.EAST
        elif dir_inp == "south":
            direction = Direction.SOUTH
        else:
            direction = Direction.NULL
        player.move(direction, game_map)

    def store_menu(self):
        for i in range(self.middle):
            print()
        print("boat: ")
        print(self.store['boat'])
        print("axe: ")
        print(self.store['axe'])
        for i in range(self.middle - 4):
            print()

    def game_menu(self, player, game_map):
        choice = int(input("What choice do you want to make (1: Move, 2: Store, or 3: Quit): "))
        if choice == 1:
            # Access Menu for Move
            self.move_menu(player, game_map)
            return True
        if choice == 2:
            # Access Menu for Store
            self.store_menu()
            return True
        if choice == 3:
            return False


