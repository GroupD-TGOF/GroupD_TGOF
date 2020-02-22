import crayons
import os
import time


class Drawer:
    def __init__(self, window: tuple):
        self.width = window[0]
        self.height = window[1]
        self.middle = self.height // 2

    def title_screen(self):
        for i in range(self.middle):
            print()
        print(crayons.green("The Game of Frupal!".center(self.width)))
        for i in range(self.middle):
            print()
        time.sleep(3)

    def final_screen(self, playing: int):
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
        spacer_lines = (self.height - map_size[0]) // 2
        spacer_columns = (self.width - ((map_size[1]) * 2)) // 2

        # Before Spacer
        for a in range(spacer_lines):
            print()

        # Spacer for centering map
        for m in range(spacer_columns):
            print(' ', end='')

        # Border On Line
        for l in range(map_size[1] + 2):
            print(crayons.blue(border), end=' ')
        print()

        for j in range(map_size[0]):

            # Spacer for centering map
            for m in range(spacer_columns):
                print(' ', end='')

            # Start border for each line
            print(crayons.blue(border), end=' ')

            # Display Map
            for k in range(map_size[1]):
                if k == b[0] and j == b[1]:
                    print(crayons.red("P"), end=' ')
                else:
                    if game_map[j][k].seen_status():
                        if not game_map[j][k].has_item('jewels'):
                            if game_map[j][k].get_name() == 'tile':
                                print(crayons.green(game_map[j][k].get_icon()), end=' ')
                            if game_map[j][k].get_name() == 'water':
                                print(crayons.blue(game_map[j][k].get_icon()), end=' ')
                            if game_map[j][k].get_name() == 'tree':
                                print(crayons.yellow(game_map[j][k]).get_icon(), end=' ')
                            if game_map[j][k].get_name() == 'mud':
                                print(crayons.black(game_map[j][k]).get_icon(), end=' ')
                        else:
                            print(crayons.cyan("J"), end=' ')
                    else:
                        print('X', end=' ')

            # End border for each line
            print(crayons.blue(border), end=' ')
            print()

        # Spacer for centering map
        for m in range(spacer_columns):
            print(' ', end='')

        # Border After End Line of Map
        for l in range(map_size[1] + 2):
            print(crayons.blue(border), end=' ')
        # print()

        # After Spacer
        for a in range(spacer_lines - 1):
            if a == 3:
                print(game_map[b[1]][b[0]].print_tile(player.inventory).center(self.width))
            print()

    def print_stats(self, player):
        s_str = "Energy: "
        s_str += str(player.get_energy())
        s_str += "     Money: "
        s_str += str(player.get_money())
        s_str += "     Inventory: "
        s_str += ' '.join([str(elem).capitalize() for elem in player.inventory])
        print(crayons.yellow(s_str.center(self.width)))
