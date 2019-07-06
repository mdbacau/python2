# Definim o lista
id = 1,2,3,4
producatori = ['Apple', 'Xiaomi', 'Nokia', 'Samsung']

print(len(producatori))

# Putem selecta din lista folosind concatenarea de baza
ios = producatori[:1]
android = producatori[1:]
print('Producatori cu sistemul de operare iOS:' + str(ios))
print('Producatori cu sistemul de operare Android:' + str(android))

# Putem inlocui prin concatenare obiecte noi in lista - mutating - strings can be changed / affecting elements
producatori[0] = "Toti"
print(producatori)

# Putem de asemenea adauga obiecte noi, nu doar inlocui/afecta cu .append() la sfarsit
producatori.append('Altii')
print(producatori)
#sau cu .insert(index,item) la inceput/oriunde altundeva
haine = [
         'Nike',
         'Adidas'
]
print(haine)
haine.insert(0, 'Primul')
haine_noi = haine
print('Folosind .insert() avem' + str(haine_noi))

# Putem selecta in afara unei liste obiecte folosind .pop(), incepand de la ultimul spre primul
lista_noua = producatori.pop()
print('Items scoase in afara:' + lista_noua)
print('Items ramase:' + str(producatori))

# Putem defini de unde scoatem itemul, prin index position [] la .pop()
scos_afara = producatori.pop(0)
print('Am scos afara \t ' + scos_afara)
print('A ramas' + str(producatori))
# Scot afara si fara a il trece intr-o noua variabila
print('Producatorii sunt' + str(producatori))
producatori.pop(-1)
print('Am scos samsung cu .pop(-1) si acum producatorii sunt' + str(producatori))

# Sort sorteaza in ordine alfabetica ori crescatoare
banci = ['Revolut', 'Libra']
suma = [200, 150]
print(banci)
banci.sort()
print(banci)

print(suma)
suma.sort()
print(suma)

# Nu putem folosi direct
# lista_sortata = lista_veche.sort()
# dar putem folosi urmatoarea metoda:
new_list = [
            'C',
            'B',
            'A'
]

print('Lista nesortata este' + str(new_list))
new_list.sort()
sorted_list = new_list
print('Lista sortata este' + str(sorted_list))

# .reverse()
lista_numere = [1,2,3,4,5]
lista_numere.reverse()
print(lista_numere)

lista_numere.insert(0, 10)
print(lista_numere)