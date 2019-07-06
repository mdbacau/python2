make = "Xiaomi"
model = "Redmi Note 7"
year = 2019
store_name = make + ' ' + model + ' ' + str(year) + ' '
print (store_name)

temp_name = store_name[0:]
store_name_2 = 'Reducere!' + ' ' + temp_name
print (store_name_2)

store_name_lowercase = store_name_2.lower()
print(store_name_lowercase)

print(store_name_2.split())

descriere_meta = 'Telefonul de noua generatie {} a fost lansat in anul {}'.format('Xiaomi Redmi Note','2019')
print(descriere_meta)

print('This is a string {}'.format('INSERTED'))

print ('The {2} {1} {0}'.format('fox','brown','quick'))
print('The' + ' ' + make[0:] + ' ' + '{b} {q}'.format(b='brown', q='quick'))

result = 100 / 777
print('The result was {r:1.3f}'.format(r=result))

price = 2650.99
print('Pretul telefonului' + ' ' + make + ' ' + model + ' ' + str(year) + ' ' + 'este {p:1.2f}'.format(p=price))


reducere = price * 0.9
currency = "lei"
print('Redus la {r:1.2f}'.format(r=reducere) + ' ' + currency)

numele = 'Jose'
print(f'Hello, his name is {numele}')
prenumele = 'Mata'
print(f'Hello, his prenume is {prenumele}')

exemplu1 = "Test"
exemplu2 = 6
print(f'Avem {exemplu1} cu {exemplu2}')

print('Versiunea veche este {} {}'.format(exemplu1, exemplu2))