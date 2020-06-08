# Write a program which can filter() to make a list whose elements are even number
#  between 1 and 20 ( both included)
# Python code to filter even values from a list 


list = [1,2,3,4,5.6,7,8] 
output = [] 
for num in list:
    if num % 2 == 0:
        output.append(num) 

print(output) 