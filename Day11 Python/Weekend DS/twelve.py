# 12 Generate and print another tuple whose values 
# are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
x=(1,2,3,4,5,6,7,8,9,10)
list=[]
for i in x:
    if i%2==0:
        list.append(i)
y=tuple(list)
print(y)
print(type(y))