# range()
for num in range(0,11,2):
    print(num)

# enumerate()
word = 'Alexandra'
for item in enumerate(word):
    print(item)

# zip()
id = [1,2,3]
produse = ['Telefoane','Laptopuri','TV']
print (id)
print (produse)
for items in zip(id,produse):
    print(items)

# in operator
print('a' in 'iulian')

dictionar = {'key1':'value1'}
print('value1' in dictionar.values())

# min and max
numere = [20,30,40,50,100]
print(min(numere))
print(max(numere))

# random - functions: shuffle, randint
from random import shuffle
lista = [1,2,3,4,5,6,7,8,9,10]
shuffle(lista)
print(lista)

from random import randint
print(randint(0,100))
mynum = (randint(0,100))
print(mynum)

# input
result = int(input('Enter a number here:'))
print(int(result / 2))
print(type(result))
