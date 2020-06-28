class Person:
    def __init__(self,initialAge):
        if initialAge <0:
            self.age= 0
            print('Age is not valid, setting age to 0.')
        else:
            self.age=initialAge
    def amIOld(self):
        if self.age<13:
            print('You are young.')
        elif self.age>=13 and self.age<18:
            print('You are a teenager.')
        else:
            print('You are old.')
    def yearPasses(self):
        self.age+=1
y = int(input())
for i in range(0, y):
    age = int(input())         
    x = Person(age)  
    x.amIOld()
    for j in range(0, 3):
        x.yearPasses()       
    x.amIOld()
    print("")