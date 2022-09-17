#matching and extracting data
from distutils.filelist import findall
import re                       #importa la libreria de regular expresions

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)     #[0-9] significa que solo uno cualquier digito entre 0 a 9 y el + hace que sean grupos de numeros (42)
print(y)

y = re.findall('[AEIOU]+', x)      #lo mismo pero ahoa buscando vocales mayusculas separadas o juntas
print(y)                            #como no hay te devuelve tu lista de nada


#greedy matching
z = 'From: using the: character'
y = re.findall('^F.+:', z)      #[F] va a buscar cualquier string que comience con F [.+]uno o mas caracteres[:]termine en ':' 
print(y)                        #como encuentra dos veces ':' va a tomar el string mas largo dejando dentro la primera aparicion de ':'

#non greedy matching
y = re.findall('^F.+?:', z)     #el signo '?' le dice al + y al * "yo chill man" y le bajan a su pedo
print(y)                        #entonces solo agarra el string mas corto

#fine-tuning extraction
xx = 'From stephen.marquard@uct.ac.za Sat Jan509:14:16 2008'
y = re.findall('\S+@\S+', xx)   #[\S] one non-withespace caracter [+] mas de uno de esos
print(y)                        #entonces busca cualquier caracter hasta encontrar un espacio al rededor de un @

#forma 2 de lo mismo
y = re.findall('^From (\S+@\S+)', xx)   #hace lo mismo que el de arriba pero busca especificamente que empiece con "From " (tambien el espacio cuenta)
print(y)                                #pero solo va a guardar en la variable lo que esta entre parentecis

#obtener el host com habiamos hecho pero mas eficaz
y = re.findall('^From .*@([^ ]*)', xx)  #([^ ]*)a partir del @ extrae todos los non-blank caracters si la linea comienza con 'From '
print(y)

#escape character
zz = 'we just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', zz)         #para usar algun character de los regex porque ese queremos buscar le ponemos un \ antes
print(y)                                #\$ a real dollar sign, [0-9.] a digit or period, + at least one or more