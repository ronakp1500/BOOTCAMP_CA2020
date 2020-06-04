#In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue
#guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

luckynumber = 143
number=int(input('Guess your Lucky Number\t'))
i=1
answer='.'
while(i<5):
     if(number==luckynumber or answer=='no' ):
         print('You got Lucky Number')
         break
     else:
         print('Sorry but that was not very successful')
         answer=input('Do you want to continue guessing\t')
         number=int(input('Guess your Lucky Number\t'))
         i=i+1