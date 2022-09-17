#lists methods
#construir una lista vacia
stuff = list()              #le decimos a python que haga una palabra (clase en realidad) reserbada
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)
print()

#is something in? (in operator)
print('cookie' in stuff)
print(15 in stuff)
print('perro' not in stuff)
print()

#ordenar y desordenar (sort)
friends = ['oracio', 'ronicio', 'catemalcensista', 'llorch']
friends.sort()
print(friends)
print(friends[1])
print()

#funciones built-in python
nums = [1,2,3,5,54,34,76,2]
print('len: ',len(nums))
print('max: ',max(nums))
print('min: ',min(nums))
print('sum: ',sum(nums))
print('abg: ',sum(nums)/len(nums))
