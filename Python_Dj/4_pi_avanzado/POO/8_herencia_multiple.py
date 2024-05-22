class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    #Método genérico pero con implementación particular 
    def hablar(self):
        #Método vacío
        pass
    #Método genérico pero con implementación particular
    def moverse(self):
        #Método vacío
        pass
    #Método genérico pero con implemetación particular
    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
    
class Mamífero(Animal):
    def __init__(self, especie, edad):
        super().__init__(especie, edad)
    
class Perro(Mamífero): #Clase Perro es hijo de Mamífero, pero por herencia múltiple Perro es herredo lo que tenga la clase Animal.
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
    
mi_perro = Perro("Toby", "Bulldog", "Max")
mi_perro.describeme() 