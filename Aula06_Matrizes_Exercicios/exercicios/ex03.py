# Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números
# inteiros entre 1 e n.
# Valide a entrada do usuário, só aceite números positivos!!

n = int(input("Digite um número inteiro: "))
soma = 0

while n <= 0:
    print("Valor inválido! Digite apenas números inteiros")
    n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")