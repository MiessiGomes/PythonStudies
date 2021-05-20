numero = float(input("Digite um número para saber se é par ou ímpar: "))

leftover = numero % 2

if leftover == 0:
    print("Par")
else:
    print("ímpar")
