#Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
x=[1,2,3,4,5,6,7,8,9]
print(x)
for i  in x:
	if(i%2 == 0):
	    x.remove(i)
print(f'After removing Even number from List {x}')