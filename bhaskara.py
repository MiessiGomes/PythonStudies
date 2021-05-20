import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

x = (b ** 2) - (4 * a * c)
if x < 0:
    print("Raíz negativa não pode ser extraída")
    exit()
else:
    x = math.sqrt(x)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
    
print("A primeira raíz é: ", x1)
print("A a raíz é: ", x2)