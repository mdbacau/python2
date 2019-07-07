a = 0

while a < 5:
    print(f'Value of a is {a}')
    a += 1
else:
    print('Value of a is not smaller than 5')

x = [1,2,3]

# testing pass
for item in x:
    pass
print ('end of the script')

# testing continue
y = 'Iulian'
for letter in y:
    if letter == 'a':
        continue
    print(letter)

# testing break
z = 'Alexandra'
for lit in z:
    if lit == 'e':
        break
    print(z)

f = 0

# while if
while f < 3:
    if f == 2:
        break
    print(f)
    f += 1