import crayons
import os

def createmap():
	#x = os.get_terminal_size().columns
	#y = os.get_terminal_size().lines
	x = 20
	y = 20
	a = ['T'] * y
	for i in range(y):
		a[i] = ['T'] * x
	a[2][1] = 'W'
	return a

def printmap(a):
	margin = 40;
	for j in range(len(a)):
		for k in range(0, len(a[j])):
			print(crayons.green(a[j][k]), end = ' ')
			margin += 2
		print()
	