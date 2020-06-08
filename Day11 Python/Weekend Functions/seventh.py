# Define a function that can accept two strings as input and print the string 
# with maximum length in console. If two strings have the same length, 
# then the function should print all strings line by line.

def length_of_string(str1, str2):
	if (len(str1) == len(str2)):
		print(str1)
		#print("\n")
		print(str2)

	elif (len(str1) < len(str2)):
		print(str2)
	
	else:
		print(str1)

stri1 = input(str("enter First String: "))
stri2 = input(str("enter Second String: "))

print("\n")

length_of_string(stri1, stri2)