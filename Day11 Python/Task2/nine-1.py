#Modify the program so that it asks users whether they want to guess again each time. 
#Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. 
#The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)
luckynumber = 143
number=int(input('Guess your Lucky Number\t'))
i=1
answer='.'
while(i):
     if(number==luckynumber or answer=='no' ):
         print('You got Lucky Number')
         break
     else:
         print('Sorry Unlucky')
         answer=input('Do you want to continue guessing\t')
         number=int(input('Guess your Lucky Number\t'))
         
   
