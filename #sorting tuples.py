#sorting tuples
d = {'a':10,'b':1,'c':22}
t = sorted(d.items())                   #sorted toma como entrada una lista
print(t)
for k,v in sorted(d.items()):
    print(k,v)
print()

#sort by value
templist = list()                       #creamos una lista para guardar los datos al reves (v,k)
for k,v in d.items():
    templist.append((v,k))              #rellenamos la lista tuple by tuple
print(templist)
templist = sorted(templist, reverse=True)#sorteamos de mayor a menor, por eso reverse
print(templist, '\n')

#sort the most used words in a text
fhand = open('texto.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
lst = list()
for key,val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val,key in lst[:10]:
    print(key, 'encontrada', val, 'veces')
print()

#version mas corta para sortear
print('esta es una version corta de sort')
clist = {'a':10,'b':1,'c':22}
print(sorted([(va,ke) for ke,va in clist.items()], reverse=True))