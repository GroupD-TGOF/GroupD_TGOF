import os
import crayons

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
middle = height // 2

def titlescreen():
	for i in range(middle):
		print()
	print(crayons.green("The Game of Frugal!".center(width)))
	for i in range(middle):
		print()
	
def menuscreen():
	for i in range(middle - 2):
		print()
	print(crayons.green("The Game of Frugal!".center(width)))
	print("Start Game!".center(width))
	for i in range(middle - 2):
		print()