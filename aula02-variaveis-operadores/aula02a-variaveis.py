from mypyc.irbuild.util import is_dataclass_decorator

print("ola mundo")

print(7+4)
print("7+4")
print("7" "+" "4") # CONCATENAÇÃO DE STRINGS

# Comentários de 1 linha em python

'''
Comentários de
múltiplas
linhas
'''
# VARIÁVEIS
nome = "Guanabara" # string - texto
idade = 25 # int - número
peso = 75.8 # float - num. decimal

print(nome, idade, peso)
print(f"Oiiii, {nome}!!!!")

# INPUTS - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Oii", nome, "! Você tem", idade, "anos")
print(f"Oii {nome}! Você tem {idade} anos")

nova_idade = idade + 1
print(nova_idade)