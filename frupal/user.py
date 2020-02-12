from .player import Direction
from .config import Config
from .drawer import Drawer
import os
import crayons
import readchar


class User:

    def __init__(self, window):
        self.width = window[0]
        self.height = window[1]
        self.middle = self.height // 2

        self.store = {  # Creates Store Library
            1: 'saw',  # Initializes player stats
            2: 'boat',
            3: 'wood_plank'
        }

    @staticmethod
    def config_menu(config: Config):
        config.print_config()
        config.map_Input['size'] = 0  # If user wants new settings, reset inputs
        config.map_Input['style'] = 0  # If user wants new settings, reset inputs
        config.map_size()  # Calls function to set new Map Dimensions
        config.map_style()  # Calls function to set new Map Tile quantities
        config.player_stats()  # Calls function to set new Player stats
        config.create_config()  # Calls function to save to config file
        config.print_config()

    def main_menu(self, config: Config):
        for i in range(self.middle - 4):
            print()
        print(crayons.green("The Game of Frupal!".center(self.width)))
        print(crayons.yellow("(S) Start Game!".center(self.width)))
        print(crayons.yellow("(C) Configuration?".center(self.width)))
        print(crayons.yellow("(Q) Exit Game.".center(self.width)))
        for i in range(self.middle - 4):
            print()
        key = readchar.readkey()
        if key == 's' or key == '\n':
            return 1
        if key == 'c':
            config.change_config()
            return self.main_menu(config)
        if key == 'q' or key == '\033':
            return 0
        else:
            return self.main_menu(config)

    def store_menu(self, player):
        for i in range(self.middle):
            print()
        print("Welcome to the Store.")
        for key in self.store:
            print(str(key) + ". " + self.store[key])
        for i in range(self.middle - len(self.store)):
            print()
        choice = int(input("What do you want to buy: "))
        if choice == 1:
            # player.add_inv(self.store[choice])
            pass
        elif choice == 2:
            # player.add_inv(self.store[choice])
            pass
        elif choice == 3:
            # player.add_inv(self.store[choice])
            pass

    @staticmethod
    def control(player, game_map):
        if player.get_energy() == 0:
            game_map.map_reveal()
            return 2
        # code that returns 3 for game win if game conditions are met

        # end of game win conditions
        key = readchar.readkey()
        if key == 'w':
            player.move(Direction.NORTH, game_map)
            return 1
        if key == 'a':
            player.move(Direction.WEST, game_map)
            return 1
        if key == 'd':
            player.move(Direction.EAST, game_map)
            return 1
        if key == 's':
            player.move(Direction.SOUTH, game_map)
            return 1
        if key == 'c':
            game_map.map_reveal()
            return 3
        if key == 'q' or key == '\033':
            return 0
        else:
            return 1
