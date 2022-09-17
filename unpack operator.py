x = [1,23,4,543,6,3]

print(*x)           #el operador de unpack imprime cada valor de la lista por separado
print(x)            # a diferencia de esto que solo imprime la lista

#uso en funciones
#tengo varios pares de datos que quiero pasar a la funcion y hacer el mismo proceso en todos
def funct(x,y):
    print(x,y)

pairs = [(1,2),(3,4),(5,6)]
for pair in pairs:
    funct(*pair)       # asi no necesito escribir cada subindice ya que el operador los desenpaqueto solo

#para usarlos con diccionarios se ocupan ** dos asteriscos en lugar de solo uno (debes llamar a las keys igual que los argumentos)
#un solo * asterisco es para tuples o listas

print()
#imaginemos que tenemos una funcion que no sabemos cuantos argumentos (positional or keyword arguments)
#podemos usar *args y **kwargs para pasar una cantidad ilimitada de argumentos regulares y argumentos keyword
def funct1(*args, **kwargs):
    print(args, kwargs)

funct1(1,2,3,4,5,one=0,two=1)   #al imprimirlo nos resulta un tuple con todos los positional arguments y una lista con todos los keword arguments

