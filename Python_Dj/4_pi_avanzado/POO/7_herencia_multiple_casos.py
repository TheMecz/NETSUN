class Clase1: #Clase 1 es padre
    pass

class Clase2(Clase1): #Clase 2 hijo de Clase 1
    pass

class Clase3(Clase2): #Clase 3 es hijo de Clase 2  -> también es hijo de Clase 1
    pass

print(Clase3.__mro__)