import math

intervalo = 2000
numPrimos = []

def primo(numero):
    raiz = math.sqrt(numero)

    for i in range(3, int(raiz) + 1, 2):
        if numero % i == 0:
            return False
        else:
            return True
    return False

for i in range(2, intervalo + 1):
    if primo(i):
        numPrimos.append(i)

print(numPrimos)

# TA ERRADO
