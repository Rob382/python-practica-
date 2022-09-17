#contador de palabras que el usuario ingrese

archivo = input('nombre del archivo? ')
archivo2 = archivo+'.txt'
try:                                    #para evitar traceback lo abrimos con try except
    leer = open(archivo2)
except:
    print('no se puede abrir el archivo: ', archivo2, '\n\nya no quiero nada!!! >:(\n'.upper())
    quit()

palabra = input('que palabra buscas? ')
print()
print('instancias con coincidencia: ')
count = 0
for line in leer:
    line2 = line.lower()                  #convierte la linea en minusculas para que no haya problemas de case sensitive
    if palabra in line2:                  #busca coincidencias en cada linea con la palabra que le dimos de input
        count += 1                        #cuenta cuantas veces encontró coincidencias
        linestrip = line.rstrip()         #quita el último carácter (\n) y mantiene las mayúsculas por eso se usan line y line2
        print(linestrip)                  #imprime todas las lineas en las que se haya encontrado coincidencia
print('\nse encontró ', count, 'veces la palabra', palabra, '\n')