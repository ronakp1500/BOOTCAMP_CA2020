#its combined solution of fourth and fifth question
a=float(input('Enter first no\t'))
b=float(input('Enter second no\t'))
c=float(input('Enter third no\t'))
avg=float((a+b+c)/3)
if(a<0 or b<0 or c<0):
    print('Its Over')
else:
    print('Good Going')
    if(avg>a and avg>b and avg>c):
        print('avg is higher than a,b,c')
    elif(avg>a and avg>b):
        print('avg is higher than a,b')
    elif(avg>a and avg>c):
        print('avg is higher than a,c')
    elif(avg>b and avg>c):
        print('avg is higher than b,c')
    elif(avg>a):
        print('avg is higher than a')
    elif(avg>b):
        print('avg is higher than b')
    elif(avg>c):
        print('avg is higher than c')