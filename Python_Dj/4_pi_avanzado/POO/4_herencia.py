# Definimos una clase padre

class Animal:
    pass

# Creamos una clase hijo que hereda de la padre

class Perro(Animal):
    pass

print(Perro.__base__)
# <class '__main__.Animal'>
print(Animal.__subclasses__())
# [<class '__main__.Perro'>]

# La herencia nos permite que la hija pueda heredar los métodos y atributos de la clase padre.
