#an http request using ullib
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
#se puede hacer lo mismo que con los documentos locales ya se hizo