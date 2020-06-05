#Write a program to replace the last element in a list with another list.
#Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
#Expected output: [1,3,5,7,9,2,4,6,8]
x=[[1,3,5,7,9,10],[2,4,6,8]]
y=x[0]
z=x[1]
y[-1:] = z
print(y)
