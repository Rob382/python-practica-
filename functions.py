#las funciones son objetos tecnicamente
def run():
    print('run')

run()

def run2(x,y):
    print('run2',x,y)

run2(5,6)

#lo de arriba es diferente ya que la funcion se encarga de imprimir lo que tiene programado pero
#podemos hacer que solo haga operaciones y regrese el resultado a la variable que asignamos
def run3(x,y):
    return x*y

print(run3(3,5))

def run4(x,y):          #si retornamos varios valores los regresa como un tuple
    return x*y, x+y, x*x/y

print(run4(3,5))

print(run4(3,5)[0])     #si queremos sacar los valores por separado
print(run4(3,5)[1])
print(run4(3,5)[2])

r1, r2, r3 = run4(3,5)  #una forma mas limpia y bonita para hacer lo mismo 
print(r1)
print(r2)
print(r3)

print()
#para poner un parametro opcional que tal vez no queramos usar o tal vez si
def funct(x,y,z=None):
    return(x,y,z)

print(funct(3,4))   #esto no nos va a causar un traceback como si lo hicieramos omitiendo uno de los primeros
