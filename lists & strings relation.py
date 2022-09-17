#relation between strings and lists
abc = 'four words one string'
stuff = abc.split()                 #divide los strings en cada espacio y convierte en lista de varios strings
print(stuff)                        #default es con espacios, tabs, \n y esos pero se puede especificar cual usar en el metodo
print(len(stuff))
print(stuff[2])


#imprimir el dia desde el texto guardado
fhand = open('texto.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])