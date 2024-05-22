# listas por compresión
# Es una forma de instrucción que permite de manera concisa la contrucción de una colección secuencial.
# La compresión se basa en la notación por comprensión de conjuntos. Desde la perspectiva computacional, la compresión
# utiliza un estilo declarativo y funcional.

# Estructura
# lista = [expresion for item in iterable]
# lista = [expresion for item in iterable if condition]

numeros = [1,2,3,4,5,6,7,8]
r1 = []

for item in numeros:
    valor = item*2
    r1.append(valor)
    
print("Listas utilizando for normal")
print(r1)

print("---"*30)

print("Lista por compresión")
r2 = [e*2 for e in numeros]
print(r2)

print("---"*30)

r2 = [e for e in numeros if e%2 == 0]
print(r2)
