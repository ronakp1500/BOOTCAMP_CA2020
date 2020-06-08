#8 Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.
string1="hello my name is abcde"
string1=string1.split()
for i in string1:
    if (len(i)%2==0):
        print (i)