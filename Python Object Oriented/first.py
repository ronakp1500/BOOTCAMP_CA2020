import math
C= 50
H = 30
D2 = []
result =[]
D1=input("enter the value of D\n")
D2=D1.split(",")
D2 = [int(i) for i in D2]
i=0
l = len(D2)
while(i<l):
    Q = round(math.sqrt((2*C*D2[i])/H))
    result. append(Q)
    i+=1
print("output=",result)