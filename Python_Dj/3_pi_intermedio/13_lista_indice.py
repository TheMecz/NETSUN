dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]

#positivo
print("Valor que se encuentra en el índice 1: ", dias[1])
print("Valores que se encuentran desde el índice inicial 0 hasta 2: ", dias[:3])
print("Valores que se encuentran desde el índice 3 hata el 6 que es el indice final: ", dias[3:])
print("Valores desde el índice 3 hasta el índice 4: ", dias[3:5])

print("---"*30)

#negativos
print("Valores que se encuentran en el último índice: ", dias[-1])
print("Valores que se encuentran en el primer índice: ", dias[-7])
print("Valores que se encuentran en el índice 4: ", dias[-3])
print("Valores que se encuentran desde el índice 4 hasta el 6 que es el indice final: ", dias[-3:])

print("---"*30)

#Utilizando len()
print("Cantidad de elementos", len(dias))
print(dias[len(dias)-1])