import crayons
import os
import time
from .player import Direction
from .map import Map


class Drawer:
	def __init__(self):
		self.width = os.get_terminal_size().columns
		self.height = os.get_terminal_size().lines
		self.middle = self.height // 2
		
	def titlescreen(self):
		for i in range(self.middle):
			print()
		print(crayons.green("The Game of Frugal!".center(self.width)))
		for i in range(self.middle):
			print()
		time.sleep(3)

	def menuscreen(self):
		for i in range(self.middle - 4):
			print()
		print(crayons.green("The Game of Frugal!".center(self.width)))
		print(crayons.yellow("1. Start Game!".center(self.width)))
		print(crayons.yellow("2. Configuration?".center(self.width)))
		print(crayons.yellow("3. Exit Game.".center(self.width)))
		for i in range(self.middle - 5):
			print()
		return int(input("Enter your choice: ".center(self.width)))
		
	def printstats(self, player):
		for i in range(2):
			print()
		print(crayons.yellow("Energy: " + str(player.getenergy()) + "          " + "Money: " + str(player.getmoney())))

	def printmap(self, player, map):
		b = player.getposition()
		for j in range(map.get_columns()):
			for k in range(map.get_rows()):
				if(k == b[0] and j == b[1]):
					print(crayons.red(u"\u25CB"), end = ' ')
				else:
					if(map.get_seen(j, k) == True):
						print(crayons.green(map.get_tile(j, k).name), end = ' ')
					else:
						print(' ', end = ' ')
			print()
	
	def storemenu(self):
		for i in range (self.height):
			print()
	
	def movemenu(self, player, map):
		direction = input("What choice do you want to make (north, east, south, west): ")
		player.move(direction.lower(), map)
		
	def gamemenu(self, player, map):
		choice = int(input("What choice do you want to make (1: Move, 2: Store, or 3:Quit): "))
		if(choice == 1):
			#Access Menu for Move
			self.movemenu(player, map)
			return True
		if(choice == 2):
			#Access Menu for Store	
			self.storemenu()
			return True
		if(choice == 3):
			return False
		
