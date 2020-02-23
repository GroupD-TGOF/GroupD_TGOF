from .player import Direction
from .config import Config
from .drawer import Drawer

import os
import crayons
import readchar
import time


class User:

    def __init__(self, window: tuple, config: Config):
        self.width = window[0]
        self.height = window[1]
        self.middle = self.height // 2
        self.store = config.store

    def config_menu(self, config: Config):
        sp = config.print_config()
        for i in range(self.middle - (len(sp)//2)):
            print()
        for i in range(len(sp)):
            print(sp[i].center(self.width))
        for i in range(self.middle - ((len(sp) // 2)-1)):
            print()
        key = readchar.readkey()
        if key == 'p':
            config.player_stats()
            self.config_menu(config)
        elif key == 's':
            config.map_Input['size'] = 0
            config.map_Input['style'] = 0
            config.map_size()
            config.map_style()
            self.config_menu(config)
        elif key == 'q':
            config.create_config()
            sp = config.print_config()
            for i in range(self.middle - (len(sp)//2)):
                print()
            for i in range(len(sp)):
                print(sp[i].center(self.width))
            for i in range(self.middle - ((len(sp) // 2)-1)):
                print()
            time.sleep(2)
        else:
            self.config_menu(config)

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
            return True
        if key == 'c':
            self.config_menu(config)
            return self.main_menu(config)
        if key == 'q' or key == '\033':
            return False
        else:
            return self.main_menu(config)

    def store_menu(self, player):
        for i in range(self.middle):
            print()
        while True:
            print("Welcome to the Store. Your money: {}".format(player.get_money()))
            index = 1
            keys = []
            for key in self.store:
                if not player.has_item(key):
                    keys.append(key)
                    print("Enter " + str(index) + " to buy: " + str(key) + " price: " + str(self.store[key]))
                    index += 1
            print()
            print("Enter 0 to leave the store")
            for i in range(self.middle - len(self.store)):
                print()
            try:
                choice = int(input("What do you want to buy: "))
            except:
                continue
            choice -= 1
            if choice == -1:
                return
            if choice < len(keys):
                if player.add_inv(keys[choice], self.store[keys[choice]]):
                    print("Added: " + str(keys[choice]) + " to inventory")
                    time.sleep(1)
                else:
                    print("Not enough money to purchase item")
                    time.sleep(1)
            print("\n\n\nprevious transactions above this line-------------\n\n\n")

    def control(self, player, game_map):
        if player.get_energy() == 0:
            game_map.map_reveal()
            return 2
        # code that returns 3 for game win if game conditions are met
        if player.has_item('jewels'):
            game_map.map_reveal()
            return 3;
        # end of game win conditions
        key = readchar.readkey()
        if key == 'w':
            player.move(Direction.NORTH, game_map)
            return 1
        elif key == 'a':
            player.move(Direction.WEST, game_map)
            return 1
        elif key == 'd':
            player.move(Direction.EAST, game_map)
            return 1
        elif key == 's':
            player.move(Direction.SOUTH, game_map)
            return 1
        elif key == 'c':
            game_map.map_reveal()
            return 3
        elif key == 'b':
            self.store_menu(player)
            return 1
        elif key == 'q' or key == '\033':
            return 0
        else:
            return 1
