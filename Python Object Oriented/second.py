class Shape():
    def area(self, a,b):
        
        x= a*b
        print(f"The Area of Shape of given value {a} and {b} is:",+x)

class Square():
    def __init__(self, length):
        self.length=  length*length    
        print(f"The Area of square of given value {length} is:",+self.length)   

S= Shape()
S.area(10,20)
sq=Square(50)
sq