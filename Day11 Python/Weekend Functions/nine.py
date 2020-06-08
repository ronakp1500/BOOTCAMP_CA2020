#  Write a function called showNumbers that takes a parameter called limit. 
# It should print all the numbers between 0 and limit with a label to 
# identify the even and odd numbers.
def numbers(limit):
        count_odd = 0   
        count_even = 0
        for x in range(0,limit+1):
                if not x % 2:
                        count_even+=1
                        print(x, " is even")
                else:
                        count_odd+=1
                        print(x," is odd")
        
        print("Number of even numbers :",count_even)
        print("Number of odd numbers :",count_odd)
print("Enter a limit: ")
l=int(input())
numbers(l)