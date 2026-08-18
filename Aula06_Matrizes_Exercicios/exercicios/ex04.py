n = int(input("Digite um número: "))
divisiveis = []

for i in range(1, n + 1):
    if n % i == 0:
        divisiveis.append(i)

print(divisiveis)