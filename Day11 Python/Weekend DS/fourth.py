# Create a list of thousand number using range and xrange and see the difference between each other.
# Python code to demonstrate range() vs xrange() 
# on basis of return type 

# initializing a with range() 
a = range(1,10000) 

# initializing a with xrange() 
#x = xrange(1,10000) 

# testing the type of a 
print ("The return type of range() is : ") 
print (type(a)) 

# testing the type of x 
#print ("The return type of xrange() is : ") 
#print (type(x)) 

#Python2
#xrange gives xrange object & range gives a static list
#Python3
#xrange - not available in python3
#Range gives a class 'range'