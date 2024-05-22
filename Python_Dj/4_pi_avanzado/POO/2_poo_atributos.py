class Perro:
    #El método _init_ es llamado al crear el objeto
    def __init__(self, nombre, raza, edad):
        print(f"Creando perro {nombre}, {raza}")
        
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        

class Alumno:
    def __init__(self, nombre, apellido, edad):
        print(f"Creando alumno {nombre} {apellido}, con {edad} años.")
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
alumno_1 = Alumno("Max", "Ponce", 25)
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)
    
mi_perro = Perro("Toby", "Bulldog", 5)
print(type(mi_perro))

# Creando perro Toby, Bulldog
# <class '_name_.Perro'>    

print(mi_perro.nombre) #Toby
print(mi_perro.raza) #Bulldog
print(mi_perro.edad)
