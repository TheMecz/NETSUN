# remove - eliminia un elemento específico dentro de la lista
# Es otra forma de eliminar elementos de una lista

print("Ejemplos con remove")

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(letras)

if 'a' in letras:
    letras.remove('a')
else:
    print("No está dentro de la lista")

print(letras)