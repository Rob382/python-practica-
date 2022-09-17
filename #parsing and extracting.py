#parsing and extracting

#queremos extraer la escuela desde la que envian el email
data='From stephen.marquard@uct.ac.za Sat Jan  5 9:14:16 2008'
atpos=data.find('@')                #encontramos la posicion del arroba
print(atpos)
spacepos=data.find(' ',atpos)       #encontramos la posision del siguiente espacio despues del arroba
print(spacepos)
host=data[atpos+1:spacepos]         #guardamos todo lo que esta entre esas dos posiciones
print(host)
