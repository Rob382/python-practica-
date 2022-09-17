#diccionarios contando palabras
counts = dict()
line = input('enter a line of text:\n')
words = line.split()
print('words', words)
print('counting...')
for word in words:
    counts[word] = counts.get(word,0)+1
print('counts: ', counts)
print()
# cuenta las palabras e imprime la palabra que se repite mas veces y cuantas veces se repite
name = input('cual texto?\n')
handle = open(name)
counts2 = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts2[word] = counts2.get(word,0)+1
bigcount = None
bigword = None
for word,count in counts2.items():              #ocupamos dos variables porque dict.items() nos da dos valores:key y value
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)