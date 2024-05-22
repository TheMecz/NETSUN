lista_letras = ['a', 'b', 'c', 'd', 'e']
variable = 'a'

if variable in lista_letras: # Verifico que se encuentre dentro de la lista
    posicion = lista_letras.index(variable) #pido el índice
    print("Esta en la posición: ", posicion)
else:
    print("No hay elemento en la lista")