#Las variables globales son aquellas variables que se pueden utilizar durante todo el proyecto.

pi = 3.1415

def area_circulo(radio):
    area = pi*pow(radio,2)
    return area

radio = float(input("Radio: "))
resultado = area_circulo(radio)
print("El area del circulo con radio {} es {}.".format(radio, resultado))
