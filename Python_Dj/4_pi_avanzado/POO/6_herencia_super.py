class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
        
    # Métodos genéricos pero con implementación particular.
    def hablar(self):
        #Método vacío
        pass
    def moverse(self):
        #Método vacío
        pass
    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)
        
class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        
        #Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño
        
        #Alternativa 2        
        super().__init__(especie, edad)
        self.dueño = dueño
    

mi_perro =  Perro("Poodle", 9, "Max")
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)

    