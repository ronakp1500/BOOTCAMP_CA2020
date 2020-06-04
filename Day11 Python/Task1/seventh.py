#If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. 
#Will it change the value. If Yes then Why?
x=10 
y=20.0
a=type(x)
print(a)
a=type(y)
print(a)
##here datatype value of a of x variable was int and after that if assign different data type i.e y to a its changes its type to float
#because 'a' takes the latest updated value and replaces the older datatype with new one.
