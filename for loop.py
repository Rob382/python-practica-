for i in range(10, -2, -1):
    print(i)

print('--------------------------------------')

for i in [3,2,1,4,'eke','dkdo',3,True]:
    print(i)

print('--------------------------------------')

x = [3,4,5,True,'hello']
for i in range(len(x)):
    print(x[i])

print('--------------------------------------')

print('fanzy panzy')
for i, element in enumerate(x):
    print(i, element)
