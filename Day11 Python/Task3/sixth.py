#Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
def printValues():
	x =list()
	for i in range(1,31):
		x.append(i**2)
	print(x[:5])
	print(x[-5:])

printValues()