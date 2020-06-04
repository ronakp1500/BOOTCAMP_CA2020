#Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
number = 143
answer=int(input('Guess your Lucky Number\t'))
i=1
while(i):
     if(number==answer):
         break
     else:
         i=i+1
         print(i)
         continue
   
