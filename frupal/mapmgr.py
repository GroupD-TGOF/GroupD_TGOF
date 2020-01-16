import crayons
import os;

def createmap():
	x = os.get_terminal_size().columns
	y = os.get_terminal_size().lines
	a = ['L'] * y
	for i in range(y):
		a[i] = ['L'] * x
	return a;

def printmap(a):
	for j in range(len(a)):
		for k in range(len(a[j])):
			print(crayons.green(a[j][k]), end='');
		#print()