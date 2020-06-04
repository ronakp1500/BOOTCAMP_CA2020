#The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
luckynumber = 143
number=int(input('Guess your Lucky Number\t'))
i=1
answer='.'
while(i<5):
     if(number==luckynumber or answer=='no' ):
         print('You got Lucky Number')
         break
     else:
         print('Sorry Unlucky')
         answer=input('Do you want to continue guessing\t')
         number=int(input('Guess your Lucky Number\t'))
         i=i+1
         
   
