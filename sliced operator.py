x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'ofbua']
z = 'holi'

sliced = x[0:7:2]
print(sliced)
sliced2 = x[6:1:-1]
print(sliced2)
sliced3 = y[4:1:-1]
print(sliced3)

reverselist = x[::-1]
print(reverselist)

#tambien funcionan en tuples
sliced4 = (1,2,4,6,8,5,4)[::-1]
print(sliced4)