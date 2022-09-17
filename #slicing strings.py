#slicing strings
from ctypes.wintypes import HLOCAL


word = 'monty python'
print(word[0:6])
print(word[6:7])
print(word [6:40])

print(word[:8])
print(word[8:])
print(word[:])

#concatenation
otraword='hola'
print(word,otraword)
print(word+otraword)