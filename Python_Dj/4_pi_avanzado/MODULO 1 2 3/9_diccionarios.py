# Los diccionarios son una estructura de datos que permiten almacenar su contenido en forma de llave y valor.

# Modo 1
diccionario = dict()
print(diccionario)

# Modo 2
d1 = {
    "Nombre": "Jorge",
    "Edad": 25,
    "Documento":10203040
}
print(d1)
# Modo 3
d2 = dict([
    ('Nombre','Jorge'),
    ('Edad',25),
    ('Documento',10203040)
])
print(d2)
# Modo 4
d3 = dict(Nombre='Jorge',
          Edad=25,
          Documento=10203040
          )
print(d3)