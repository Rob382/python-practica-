archivo = open('texto2.txt')

for line in archivo:
    linesinsalto = line.rstrip() #para quitar el salto de linea del final que trae por defecto el texto
    print(linesinsalto.upper())          #siempre agrega un salto de linea al final
                                        #upper lo pone en mayusculas

