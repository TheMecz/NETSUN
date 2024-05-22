print("==="*30)

# Función str()

pi = 3.14
texto = "El valor de pi es: " + str(pi)
print(texto)
print("---" * 30)

# Función len()

palabra = "Python es un lenguaje de programación"
print(len(palabra))
print("---" * 30)

# Función find()

texto = "Hola mundo, como están!"
print(texto.find("ed"))
print(texto.find("como")) 
print(texto.find("o")) #devuelve la posición del primer valor que encuentra 
print("---" * 30)

# Función replace()

palabras = "Variables globales y variables locales"
palabras = palabras.replace("locales", "local")
print(palabras)
print("---" * 30)

# Función capitalize()

cadena = "hoy día se estrena doctor strange"
print(cadena.capitalize())
print("---" * 30)

# Función lower()

cadena = "Hoy día se estrena doctor STRANGE"
print(cadena.lower())
print("---" * 30)

#Función upper()
cadena = "Hoy día se estrena doctor STRANGE"
print(cadena.upper())
print("---" * 30)

#Función strip()
cadena = " Hoy día se eStrena doctor Strange "
print(cadena)
print(cadena.strip())
print("---" * 30)

#Función join()
palabra = "Hola"
print("_".join(palabra))
print(",".join(palabra))
print(" - ".join(palabra))
print("==="*30)