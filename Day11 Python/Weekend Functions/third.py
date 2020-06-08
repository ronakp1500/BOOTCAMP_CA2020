# Create a function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,44,556,76,45,333,444,333,444,44,8,8,8,8,1,1,1])) 