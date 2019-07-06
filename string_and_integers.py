#Cu str() transformam integer in string la print
make = "Xiaomi"
model = "Redmi Note 7"
year = 2019
store_name = make + ' ' + model + ' ' + str(year) + ' '
print(store_name)

#[start:stop:jump] pentru a selecta caractere dintr-o variabila
temp_name = store_name[0:]
store_name_2 = 'Reducere!' + ' ' + temp_name
print(store_name_2)

#.lower() sau .upper()
store_name_lowercase = store_name_2.lower()
print(store_name_lowercase)

#.split() separa caracterele, putem specifica caracterul de la care se separa
print(store_name_2.split())

#Folosim {} si atunci avem variabile care pot fi introduse, cu .format
descriere_meta = 'Telefonul de noua generatie {} a fost lansat in anul {}'.format('Xiaomi Redmi Note','2019')
print(descriere_meta)
print('This is a string {}'.format('INSERTED'))

#Putem da shortcuts la variable, a='plm', b='plt', etc si in {} doar numim shortcutul
print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The' + ' ' + make[0:] + ' ' + '{b} {q}'.format(b='brown', q='quick'))

#Putem folosi {p:width:deep si f la sfarsit ca sa reducem la cate zecimale vrem
result = 100 / 777
print('The result was {r:1.3f}'.format(r=result))
price = 2650.99
print('Pretul telefonului' + ' ' + make + ' ' + model + ' ' + str(year) + ' ' + 'este {p:1.2f}'.format(p=price))

#Putem dupa ce se terminat format() sa mai adaugam si alte variable / input
reducere = price * 0.9
currency = "lei"
print('Redus la {r:1.2f}'.format(r=reducere) + ' ' + currency)

#De la Python3.6 in sus exista scurtatura pentru {}, doar punem print(f'') si putem folosi variabilele cu {variabila}
numele = 'Jose'
print(f'Hello, his name is {numele}')
prenumele = 'Mata'
print(f'Hello, his prenume is {prenumele}')

exemplu1 = "Test"
exemplu2 = 6
print(f'Avem {exemplu1} cu {exemplu2}')

#Inainte de Python 3.6, avem versiunea veche
print('Versiunea veche este {} {}'.format(exemplu1, exemplu2))