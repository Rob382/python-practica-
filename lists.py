x = [3, True, 'holi']
y = 'hi'
print(len(x))                      #para saber length de la lista
x.append('crayoli')
print(x)
x.extend([3,4,5,'kola',False])     #para poder agregar una lista dentro de la lista
print(x)
print(x[7])                         #selecciona el que queremos sin quitarlo
print(x.pop())
x.pop()                            #quita el ultimo elemento de la lista
print(x.pop(3))                     #quita el que hayamos seleccionado
print(x)
