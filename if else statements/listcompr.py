mystring = 'Alexandra'
mylist = [letter for letter in mystring]

print(mylist)

lista = [element for element in 'Word']
print(lista)

numere = [x**2 for x in range(0,5)]
print(numere)

evens = [y**2 for y in range(0,11) if not y % 2 == 0]
print(evens)