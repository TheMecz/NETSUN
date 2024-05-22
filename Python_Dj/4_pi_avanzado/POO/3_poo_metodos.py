class Perro:
    
    #Atributos
    especie = "mamífero"
    
    #El método _init_ es llamado al crear el objeto
    def __init__(self, nombre, raza, edad):
        if edad <= 1:
            print(f"Creando perro {nombre}, {raza}, de edad {edad} año.")
        else:
            print(f"Creando perro {nombre}, {raza}, de edad {edad} años.")
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")
        
    def ladra(self):
        print("Guau")
        
mi_perro = Perro("Toby", "Bulldog", 1)
mi_perro.ladra()
mi_perro.camina(10)


class Alumno:
    def __init__(self, nombre, apellido, edad):
        print(f"Creando alumno {nombre} {apellido}, con {edad} años.")
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def rendir_examen(self):
        print("Tomando examen en aula")
    
    def asistir(self):
        print("Asistiendo puntual")
        
alumno_1 = Alumno("Max", "Ponce", 25)
print(alumno_1.nombre)
print(alumno_1.apellido)
print(alumno_1.edad)

alumno_1.rendir_examen()
alumno_1.asistir()