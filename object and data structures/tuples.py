# Tuples are lists but are IMMUTABLE - can not be reassigned later
my_tuple = (1,2,3)
my_list = [1,2,3]
print(type(my_tuple))
print(type(my_list))

# We can have INDEX and COUNT methods
my_tuple2 = ('test string', 100)
print(my_tuple2[0])
my_tuple3 = ('apple', 'google', 'microsoft')
# .count() tells us how many times the term is in the tuple
print('It was found' + ' ' + str(my_tuple3.count('apple')) + ' ' + 'times')
# .index() gives us the index number of the found query
print('Index number for query is' + ' ' + str(my_tuple3.index('apple')))
print('Index number for query is' + ' ' + str(my_tuple3.index('microsoft')))