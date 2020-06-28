class ronak():
    def sumtozero(self, arg, x):
        for i in range(0, x-2):       
            for j in range(i+1, x-1): 
                for k in range(j+1, x): 
                    if (arg[i] + arg[j] + arg[k] == 0): 
                        print("The three elements that sum to zero are:", +arg[i], arg[j], arg[k]) 
Sum1=ronak()
arg=[-25,-10,-7,-3,2,4,8,10]
print(f"Length of List is {len(arg)}")
Sum1.sumtozero(arg, len(arg))  