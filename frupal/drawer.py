import crayons
import os
import time
from .player import Direction


class Drawer:
    def __init__(self):
        # self.width = os.get_terminal_size().columns
        self.width = 40
        # self.height = os.get_terminal_size().lines
        self.height = 30
        self.middle = self.height // 2

    def title_screen(self):
        for i in range(self.middle):
            print()
        print(crayons.green("The Game of Frugal!".center(self.width)))
        for i in range(self.middle):
            print()
        time.sleep(3)

    def menu_screen(self):
        for i in range(self.middle - 4):
            print()
        print(crayons.green("The Game of Frugal!".center(self.width)))
        print(crayons.yellow("1. Start Game!".center(self.width)))
        print(crayons.yellow("2. Configuration?".center(self.width)))
        print(crayons.yellow("3. Exit Game.".center(self.width)))
        for i in range(self.middle - 5):
            print()
        return int(input("Enter your choice: ".center(self.width)))

    def print_map(self, player, game_map):
        b = player.get_position()
        size = game_map.get_size
        spacer = self.height - size[0]
        spacer = spacer // 2
        map_size = game_map.get_size
        for i in range(spacer):
            print()
        for j in range(map_size[0]):
            for k in range(map_size[1]):
                if k == b[0] and j == b[1]:
                    print(crayons.red(u"\u25CF"), end=' ')
                else:

                    if game_map[j][k].seen_status():
                        if game_map[j][k].get_name() == 'tile':
                            print(crayons.green(u"\u25A0"), end=' ')
                    else:
                        print(' ', end=' ')
            print()
        for i in range(spacer):
            print()

    def print_stats(self, player):
        for i in range(2):
            print()
        print(crayons.yellow("Energy: " + str(player.get_energy()) + "          " + "Money: " + str(player.get_money())))

    # To move to user input module
    def move_menu(self, player, game_map):
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
        for i in range(self.height):
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
