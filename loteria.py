import random

def sorteio_loterica():
    numeros_sorteados = set()

    while len(numeros_sorteados) < 6:
        numero = random.randint(1, 60)
        numeros_sorteados.add(numero)

    numeros_sorteados = sorted(numeros_sorteados)

    print("Números sorteados:", numeros_sorteados)

sorteio_loterica()
