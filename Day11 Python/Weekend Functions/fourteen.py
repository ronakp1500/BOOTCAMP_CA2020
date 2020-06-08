def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

#output is 2 bcoz finally block is executed even if try block catches any exception