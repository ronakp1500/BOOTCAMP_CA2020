#2 Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
    #Expected Output:
    #No. of Upper case characters : 3
    #No. of Lower case Characters : 12

def function(x):
    y={"upper case":0, "lower case":0}
    for c in x:
        if c.isupper():
           y["upper case"]+=1
        elif c.islower():
           y["lower case"]+=1
        else:
           pass
    print ("Original String : ", x)
    print ("Total no. of Upper case characters : ", y["upper case"])
    print ("Total no. of Lower case Characters : ", y["lower case"])

function("Consulatdd is doing Great Work")