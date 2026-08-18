import random

num = int(input("Digite um número inteiro: "))
print()

numsRandom = [random.randint(1, num) for i in range(num)]
numsRandomInvertido = numsRandom[::-1]

print(f"Vetor original com números aleatórios: {numsRandom}")
print(f"Vetor invertido: {numsRandomInvertido}")
print()