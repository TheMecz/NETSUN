def funcion_parametros(a):
    print(a)

funcion_parametros("Soy una función con un parámetro")

#Existen funciones con parametros por defecto

def area_circulo(radio, pi = 3.14):
    area = pi * pow(radio,2)
    return area

print(area_circulo(2))