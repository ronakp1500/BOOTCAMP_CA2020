#Swap two numbers using the third variable as the result name and do the same task without using any third variable.
x=10+5j
y=10
name=x
x=y
y=name
print(x,y) 


#Without using third variable
x,y = y,x
print(x,y)