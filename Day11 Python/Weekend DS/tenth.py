# Write a program in Python to complete the following task:
# ●	Create two different list as in even_list and odd_list
# ●	Ask user to enter the number in the range of 1,50 and make sure
#  if the entered number is even append it to the even_list and 
# if the entered number is odd append it to the odd list.
# ●	Keep that in mind you can only add 5 items in each list
# ●	Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)
print("Sum of Even List is",sum(even))
print("Sum of odd list is",sum(odd))