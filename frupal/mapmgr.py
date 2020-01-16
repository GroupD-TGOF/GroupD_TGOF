import crayons
x = 50
y = 30
a = ['L'] * y
for i in range(y):
	a[i] = ['L'] * x

for j in range(len(a)):
	for k in range(len(a[j])):
		print(crayons.green(a[j][k]), end=' ');
	print()