print("Ejemplos con POP")

# Si se necesita eliminar un elemnto por su posición en la lista, se puede utilizar la función pop.
# Por defecto, pop eliminará el último elemento de la lista y retornará el valor del elemento eliminado

lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(lista_letras)
x = lista_letras.pop()
print(x)

x = lista_letras.pop()
print(lista_letras)
print(x)
