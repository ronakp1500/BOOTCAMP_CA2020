# 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 
import operator     
from functools import reduce    
list = [[1, 2, 3], [4, 5], [6, 7, 8]]  
joinlist = reduce(operator.add, list)  
print(joinlist)                        
str1=""
for i in joinlist:
    str1+=str(i)
print (int(str1))