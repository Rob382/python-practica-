#matching and extracting data
from distutils.filelist import findall
import re                       #importa la libreria de regular expresions

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)     #[0-9] significa que solo uno cualquier digito entre 0 a 9 y el + hace que sean grupos de numeros (42)
print(y)

y = re.findall('[AEIOU]+', x)      #lo mismo pero ahoa buscando vocales mayusculas separadas o juntas
print(y)                            #como no hay te devuelve tu lista de nada