import crayons
import os
import time


class Drawer:
    def __init__(self):
        if os.get_terminal_size().columns != 0 and os.get_terminal_size().lines != 0:
            self.width = os.get_terminal_size().columns
            self.height = os.get_terminal_size().lines
        else:
            self.width = 60
            self.height = 50

        self.middle = self.height // 2

    def title_screen(self):
        for i in range(self.middle):
            print()
        print(crayons.green("The Game of Frupal!".center(self.width)))
        for i in range(self.middle):
            print()
        time.sleep(3)

    def final_screen(self, playing):
        for i in range(self.middle):
            print()
        if playing == 3:
            print(crayons.green("You Win!".center(self.width)))
        if playing == 2:
            print(crayons.green("You Lose!".center(self.width)))
        for i in range(self.middle):
            print()
        time.sleep(3)

    def print_map(self, player, game_map):
        border = u"\u25A0"
        b = player.get_position()    
        map_size = game_map.get_size()
        for l in range(map_size[0] + 2):
            print(crayons.blue(border), end=' ')
        print()
        for j in range(map_size[0]):
            print(crayons.blue(border), end=' ')
            for k in range(map_size[1]):
                if k == b[0] and j == b[1]:
                    print(crayons.red(u"\u25CF"), end=' ')
                else:
                    if game_map[j][k].seen_status():
                        if game_map[j][k].get_name() == 'tile':
                            print(crayons.green(game_map[j][k].get_icon()), end=' ')
                        if game_map[j][k].get_name() == 'water':
                            print(crayons.blue(game_map[j][k].get_icon()), end=' ')
                        if game_map[j][k].get_name() == 'tree':
                            print(crayons.yellow(game_map[j][k]).get_icon(), end=' ')
                    else:
                        print('X', end=' ')
            print(crayons.blue(border), end=' ')
            print()
        for l in range(map_size[0] + 2):
            print(crayons.blue(border), end=' ')
        print()

    def print_stats(self, player):
        for i in range(2):
            print()
        print(
            crayons.yellow("Energy: " + str(player.get_energy()) + "          " + "Money: " + str(player.get_money())))
