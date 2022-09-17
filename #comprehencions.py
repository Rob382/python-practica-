#comprehencions
#una caracteristica de python que no esta en otros lenguajes
x = [x for x in range(5)]       #define un loop for dentro de una lista x y lo que tenga del lado izq es lo que va a agreagar a la lista
print(x)

x = [x+5 for x in range(5)]       
print(x)

x = [0 for x in range(5)]       
print(x)

x = [[0 for x in range(5)] for x in range(5)]  #nos da 5 listas con 5 0s cada una 
print(x)

y = [i for i in range(100) if i %5 == 0]       #si i es divisible por 5 lo agregamos a la lista
print(y)
print()
#esto mismo se puede hacer para dictionaries
z = {i:0 for i in range(100) if i%5 == 0}      #diccionario donde i es el key y todos tienen 0 de value
print('esto es un diccionario',z)
print()
#tambien para sets
z = {i for i in range(100) if i%5 == 0}
print('esto es un set',z)
print()
#tamnien para tuples
z = tuple(i for i in range(100) if i%5 == 0)
print('esto es un tuple',z)