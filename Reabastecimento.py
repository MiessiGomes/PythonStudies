ComprP = float(input("Comprimento da pista em metros: "))
NVoltas = float(input("Número total de voltas a ser percorridas: "))
NReabast = float(input("Número de reabastecimento desejados: "))
NConsumo = float(input("Consumo de combustível do carro em Km/L: "))

total_percurso = ComprP / 1000 * NVoltas
reabast_dist = total_percurso / (NReabast + 1)
litros_n = reabast_dist / NConsumo

print("O número mínimo de litros necessários para percorrer até o primeiro reabastecimento é de", litros_n, "Km/L")