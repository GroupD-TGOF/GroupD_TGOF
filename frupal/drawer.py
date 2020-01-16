import crayons
import os
import time

class Drawer:
	a = None
	width = os.get_terminal_size().columns
	height = os.get_terminal_size().lines
	middle = height // 2

	def __init__(self):
        #x = os.get_terminal_size().columns
		#y = os.get_terminal_size().lines
		x = 20
		y = 20
		self.a = ['T'] * y
		for i in range(y):
			self.a[i] = ['T'] * x
		
	def titlescreen(self):
		for i in range(self.middle):
			print()
		print(crayons.green("The Game of Frugal!".center(self.width)))
		for i in range(self.middle):
			print()
		time.sleep(2)
	
	def menuscreen(self):
		for i in range(self.middle - 2):
			print()
		print(crayons.green("The Game of Frugal!".center(self.width)))
		print("Start Game!".center(self.width))
		for i in range(self.middle - 2):
			print()
		time.sleep(2)

	def printmap(self):
		for j in range(len(self.a)):
			for k in range(len(self.a[j])):
				print(crayons.green(self.a[j][k]), end = ' ')
			print()