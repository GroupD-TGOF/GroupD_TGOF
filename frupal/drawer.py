import crayons
import os
import time

class Drawer:
	a = None
	width = os.get_terminal_size().columns
	height = os.get_terminal_size().lines
	middle = height // 2

	def __init__(self):
		x = 20
		y = 20
		self.a = [' '] * y
		for i in range(y):
			self.a[i] = [u"\u25A0"] * x
		
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
		
	def printstats(self):
		for i in range(4):
			print()
		print(crayons.yellow("Energy: " + "          " + "Money: "))

	def printmap(self):
		for j in range(len(self.a)):
			for k in range(len(self.a[j])):
				print(crayons.green(self.a[j][k]), end = ' ')
			print()
