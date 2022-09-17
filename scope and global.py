x = 'nombre'

def funct(name):
    x = name

print(x)
funct('changed')
print(x)            #el valor no cambia porque el valor para x dentro de la funcion es solamente valido dentro de la funcion
                    #el valor que si cambio fue el de x DENTRO de la funcion

#para volver una variable dentro de una funcion se puede hacer asi
y = 'nombre'

def funct(name):
    global y        #pero esto nunca se debe hacer, es ilegal a menos que sea completamente necesario
    y = name

print(y)
funct('changed')
print(y)            #podemos ver que ahora si cambio pero repito
                    #NO SE DEBE HACER, lo mejor es mantener las variables dentro de la fucion unicas