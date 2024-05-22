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
    
    def hablar(self):
        print("Guau")
    
    def moverse(self):
        print("Caminando con 4 patas")
    
class Vaca(Animal):
    
    def hablar(self):
        print("Muu!")
        
class Abeja(Animal):
    def hablar(self):
        print("Bzzz!")
    def moverse(self):
        print("Volando")
    # Nuevo Método
    def picar(self):
        print("Picar!")
        
mi_perro = Perro("mamífero", 10)
mi_vaca = Vaca("mamífero", 23)
mi_abeja = Abeja("insecto", 1)

mi_perro.hablar()
mi_vaca.hablar()

mi_vaca.describeme()
mi_abeja.describeme()

mi_abeja.picar()

print(mi_perro.edad)
print(mi_perro.especie)