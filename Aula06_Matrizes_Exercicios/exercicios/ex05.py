import math

intervalo = 2000
numPrimos = []

def primo(numero):
    raiz = math.sqrt(numero)

    if numero < 2:
        return False

    for i in range(2, int(raiz) + 1):
        if numero % i == 0:
            return False
    return True

for i in range(2, intervalo + 1):
    if primo(i):
        numPrimos.append(i)

print(f"Os números primos de 2 até {intervalo} são = {numPrimos}")