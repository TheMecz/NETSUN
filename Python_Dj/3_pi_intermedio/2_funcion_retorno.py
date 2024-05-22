def suma(a, b):
    suma = a + b
    return suma

def resta(a,b):
    resta = a - b
    return resta

def multiplicacion(a,b):
    multi = a * b
    return multi

a = float(input("Digite el primer número: "))
b = float(input("Digite el segundo número: "))

print("La suma es: ", suma(a,b))
print("La resta es: ", resta(a,b))
print("La multiplicación es: ", multiplicacion(a,b))
