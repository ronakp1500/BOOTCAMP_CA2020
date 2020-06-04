x=int(input('Enter First no\t'))
y=int(input('Enter Second no\t'))
print('Enter 1 - Addition\nEnter 2 - Subtraction\nEnter 3 - Division\nEnter 4 - Multiplication\nEnter 5 - Average\n')
option=int(input('enter your option'))
if(option==1):
    result=print(f'Addition is: {x+y}')
elif(option==2):
    result=(print(f'Subtraction is: {x-y}')
elif(option==3):
    result=print(f'Divison is: {x/y}')
elif(option==4):
    result=print(f'Multiplicaton is: {x*y}')
elif(option==5):
    p=int(input('Enter third number'))
    q=int(input('Enter fourth number'))
    result=print(f'AVERAGE is: {(x+y+p+q)/4}')
result=int(result)
if(result<0):
    print('ZSA')
    

