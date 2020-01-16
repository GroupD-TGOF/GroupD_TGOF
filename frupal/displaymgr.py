import os

width = os.get_terminal_size().columns
height = os.get_terminal_size().lines
middle = height // 2

def titlescreen():
	for i in range(middle):
		print()
	print("The Game of Frugal!".center(width))
	for i in range(middle):
		print()
	