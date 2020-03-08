from .player import Direction
from .config import Config

import crayons
import readchar
import time


class User:

    def __init__(self, window: tuple, config: Config, debug: bool):
        self.width = window[0]
        self.height = window[1]
        self.middle = self.height // 2
        self.store = config.store
        self.debug = debug

    def update_store(self, config, debug):
        self.store = config.store
        self.debug = debug

    def __print_config_menu(self, config: Config):
        sp = config.print_config()
        for i in range(self.middle - (len(sp) // 2)):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        for i in range(len(sp)):
            if sp[i] == '^':
                print()
            else:
                print(sp[i].center(self.width))
        for i in range(self.middle - (len(sp) // 2)):
            if self.debug:
                print("+ " + str(i))
            else:
                print()

    def config_menu(self, config: Config):
        self.__print_config_menu(config)
        key = readchar.readkey().lower()
        if key == 'p':
            config.change_stats()
            self.config_menu(config)
            config.system_finder()
        elif key == 's':
            config.map_size()
            config.map_style()
            config.system_finder()
            config.jewel_change()
            self.config_menu(config)
        elif key == 't':
            config.change_tile()
            config.system_finder()
            self.config_menu(config)
        elif key == 'c':
            config.reset_config()
            self.config_menu(config)
        elif key == 'b':
            config.change_price()
            self.config_menu(config)
        elif key == 'r':
            config.create_config()
            time.sleep(2)
        else:
            self.config_menu(config)

    def main_menu(self, config: Config):
        for i in range(self.middle - 2):
            if self.debug:
                print("+ ".rstrip("\n") + str(i))
            else:
                print()
        print(crayons.green("The Game of Frupal!\n".center(self.width)))
        print(crayons.yellow("(Press S) Start Game!".center(self.width)))
        print(crayons.yellow("(Press C) Configuration?".center(self.width)))
        print(crayons.yellow("(Press Q) Exit Game.".center(self.width)))
        for i in range(self.middle - 2):
            if self.debug:
                print("+ " + str(i))
            else:
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
        spacer = (len(self.store) + 4) // 2
        while True:
            for i in range(self.middle - spacer):
                if self.debug:
                    print("+ " + str(i))
                else:
                    print()
            print("Welcome to the Store.".center(self.width))
            print("Your Money: {}".format(player.get_money()).center(self.width))
            index = 1
            keys = []
            for key in self.store:
                if not player.has_item(key):
                    keys.append(key)
                    print(("Enter " + str(index) + " to buy: " + str(key) + " Price: " + str(self.store[key])).center(
                        self.width))
                    index += 1
            print()
            print("Enter 0 to leave the store".center(self.width))
            for i in range(self.middle - (spacer + 1)):
                if self.debug:
                    print("+ " + str(i))
                else:
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
                    print(("Added: " + str(keys[choice]) + " to inventory").center(self.width))
                    time.sleep(1)
                else:
                    print("Not enough money to purchase item".center(self.width))
                    time.sleep(1)
            print("\n\n\nprevious transactions above this line-------------\n\n\n".center(self.width))

    def key_menu(self):
        key_binds = ["Use keys on the keyboard to navigate and control the game and its menus!", "Movements: ",
                     "(W) Move North!", "(A) Move West!               (D) Move East!", "(S) Move South!", "Utilities: ",
                     "(B) Store!", "(C) Cheat!", "(K) Keybindings!", "(Q) Quit!"]
        for i in range(self.middle - (len(key_binds) // 2)):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        for i in range(len(key_binds)):
            print(key_binds[i].center(self.width))
        for i in range(self.middle - (len(key_binds) // 2)):
            if self.debug:
                print("+ " + str(i))
            else:
                print()
        print("(Press R) Return!".center(self.width))
        key = readchar.readkey()
        if key != 'r':
            self.key_menu()
        else:
            return

    def control(self, player, game_map):
        if player.has_item('jewels'):
            game_map.map_reveal()
            return 3
        if player.get_energy() == 0:
            game_map.map_reveal()
            return 2
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
        elif key == 'k':
            self.key_menu()
        elif key == 'b':
            self.store_menu(player)
            return 1
        elif key == 'q' or key == '\033':
            return 0
        else:
            return 1
