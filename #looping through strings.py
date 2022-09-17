#looping through strings
fruit='banana'
index=0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index+1
print('fiinnn')

for otraletra in fruit:
    print(otraletra)
print('otrofin')


contador = 0
for letras in fruit:
    if letras == 'a':
        contador = contador + 1
print('hay', contador,'letras "a"')