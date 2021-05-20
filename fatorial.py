def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def fatorial_test():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")