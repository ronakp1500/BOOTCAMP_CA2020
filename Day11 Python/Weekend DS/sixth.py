# 6. Write a program in Python to iterate through the list of numbers in the range of 1,100
#  and print the number which is divisible by 3 and a multiple of 2.

list=range(1,101)
def func(list1):
    for i in list1:
        if (i%3==0 or i%2==0):
            print (i)
func(list)