#diccionarios
#son como las listas pero sin un orden es especifico, por eso se le agregan etiquetas
purse = dict()
purse['money'] = 12
purse['candy']=7
purse['cotonetes'] = 45
print(purse)
print('hay ', purse['candy'], 'dulces')
purse['candy'] = purse['candy'] + 3
print(purse)
print()
#se pueden crear con {} para agregar varios elementos de una sola vuelta
dictio = {'chuck' : 1, 'jijo':3, 'lanyster':45}
print(dictio)
dicc_vacio = {}
print(dicc_vacio)
print()

#two iteration variables
jjj = {'chuck':1, 'fred':34, 'jan':22}
for key,value in jjj.items():               #si solo usars el jjj te va a dar solo las keys pero si usas jjj.items
    print(key,value)                        #te da key y value que debes tener donde guardar, dos variables normalmente
print()

#get method para diccionarios
counts = dict()
names = ['jose','juan','oracio','juan','jose','ronisio','jose']
for name in names:
    counts[name]=counts.get(name,0)+1
print('histograma:')
print(counts)