# Escreva um programa que dado um inteiro n positivo calcula e imprime a soma de todos os números
# inteiros entre 1 e n.
# Valide a entrada do usuário, só aceite números positivos!!

n = input("Digite um número inteiro: ")
soma = 0

while n % n == 0:
    for i in range(n):
        soma = soma + i

# pensar depois