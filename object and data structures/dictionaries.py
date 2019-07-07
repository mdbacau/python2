# Dictionarele sunt tip key:value pair, dar nu pot fi indexat/sliceuite
dictionar = {'key1':'value1','key2':'value2'}
print(dictionar['key1'])

prices = {'pret':2900,'stoc':1}
print('Pretul este de' + ' ' + str(prices['pret']) + ' '
      +
'iar in stoc se afla' + ' ' + str(prices['stoc']) + ' produs')

# Putem avea dictionare in interiorul altor dictionare
# Ele suporta o diversitate de tipuri de date, integers, strings, lists, etc.
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':1000}}
# Stacking index calls
print(str(d['k2'][2]))
# Stacking key calls
print(str(d['k3']['insideKey']))

# Putem sorta prin stacking
apa = {'marca':['aqua', 'borsec', 'dorna']}
print(apa)
# Putem folosi .upper() si alte functii doar prin indexing, daca folosim slicing outputul nu ne permite
apa_buna = apa['marca'][0].upper()
print(apa_buna)

# Putem adauga oricand mai tarziu alte valori in dictionar, fara a il edita pe cel initial
music = {'key1':'YouTube', 'key2':'Spotify'}
print(music)
music['key3'] = 'Apple'
print(music)
# We can also overwrite
music['key1'] = 'GeckoMusic'
print(music)

# Listing all keys or key values / paired
print(music.keys())
print(music.values())
print(music.items())