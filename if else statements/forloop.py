mylist = [1,2,3,4,5,6,7,8,9,10]

for item in mylist:
    print('hi')

for num in mylist:
    # Checking for even
    if not num % 2 == 0:
        print(f'Odd number: {num}')
    else:
        print(f'Even number: {num}')

list_sum = 0

for num in mylist:
    list_sum += num

print(list_sum)

mystringlist = 'Hello World'
for letter in mystringlist:
    print(letter)

mylist2 = [(1,2),(3,4),(5,6),(7, 8)]
for a,b in mylist2:
    print(b)

mylist3 = {(1,2,3),(4,5,6),(7,8,9)}
for a,b,c in mylist3:
    print(b)

dictionary = {'cheie1':'valoare1','cheie2':'valoare2','cheie3':'valoare3'}
for key,value in dictionary.items():
    print(value)