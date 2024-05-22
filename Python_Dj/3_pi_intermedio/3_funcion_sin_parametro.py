def suma():
    a = int(input("Digite el numero 1: "))
    b = int(input("Digite el numero 2: "))
    suma = a + b
    return suma

print(suma())


def suma():
    a = int(input("Digite el numero 1: "))
    b = int(input("Digite el numero 2: "))
    suma = a + b
    print(suma)

suma()

def calculadora(x, y):
    suma = x + y
    resta = x - y
    multi = x * y
    return suma, resta, multi

a, b, c = calculadora(10, 5)
print(a, b, c)