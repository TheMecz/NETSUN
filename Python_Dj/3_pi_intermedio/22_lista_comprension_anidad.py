# Estructura
# lista = [expresion for item1 in iterable for item2 in iterable]

# Matriz lista de lista
m = [[2, 3, 4],
    [40, 50, 60],
    [100, 200, 300]
]

# equivalente usando for

total = 0
for row in m:
    for x in row:
        total += x
print(total)

# suma total
total_compresion = [x for row in m for x in row]
print(total_compresion)
print(sum(total_compresion))