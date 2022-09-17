#sets

x = set()             #para crear un set vacio
s = {4,32,2,2}        #los guarda sin orden y elimina los duplicados
print(s)
#set operators        #estas operaciones son mucho más rápidas en sets que en listas cunado hay muchos datos
s.add(5)
print(s)
s.remove(4)
print(s)
print(32 in s)

# mas operaciones
s2 = {3,4,22,1}
print(s.union(s2))  #une los dos sets en uno solo
print(s.difference(s2))
print(s.intersection(s2))
