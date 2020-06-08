# 12 #12 Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError:
    print ("Cant divide by zero as its denominator ")