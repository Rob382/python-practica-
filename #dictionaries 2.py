#dictionaries 2
x = {'key1': 4}
x['key2'] = 5
x[2] = [3,2,6,4]
print(x)

#obtener keys y values
for key,value in x.items():
    print(key,value)

#obtener solo las keys
for key in x:
    print(key)

# otra forma de obtener keys y values usando comandos mas sencillos
for key in x:
    print(key, x[key])



