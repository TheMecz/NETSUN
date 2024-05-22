def numero_mayor(num1, num2):
    respuesta = False
    if num1 > num2:
        respuesta = True
    
    return respuesta

x = int(input("Digite el primer número: "))
y = int(input("Digite el segundo número: "))

if numero_mayor(x,y):
    print("El número {} es mayor a {}".format(x, y))
    
else:
    print("El número {} es mayor a {}".format(y,x))