#Create a dictionary that contains a number (between 1 and n) in the form(x,x*x).
#Sample data (n=5)
#Expected Output: {1:1,2:4,3:9,4:16,5:25}
n=int(input("How many items you like to input in Dictionary\t"))
y = dict()
for x in range(1,n+1):
    y[x]=x*x
print(y) 
