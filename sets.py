# Sets are UNORDERED collections of UNIQUE elements
myset = set()
myset.add(1)
print(myset)

myset.add(2)
print(myset)

# Adding a value that already is in the set, it will not repeat it
myset.add(2)
print(myset)

# We can retrieve the unique variables in lists and other things
mylist = [1,1,1,1,1,1,2,2,2,2,2]
print(mylist)
print(set(mylist))
