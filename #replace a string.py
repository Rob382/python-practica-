#replace a string
word='amigos y shabos'
inclusivo=word.replace('o','x')
print(inclusivo)

word2='    amigos y shabos     '
print(word2.lstrip()) #quita los espacios a la izquierda
print(word2.rstrip()) #quita los espacios a la derecha
print(word2.strip()) #quita de los dos lados

#prefijos
print('empieza con please?', word.startswith('please'))
print('empieza con ami?', word.startswith('ami'))