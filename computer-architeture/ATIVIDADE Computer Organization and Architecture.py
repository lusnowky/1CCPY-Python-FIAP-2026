# ATIVIDADE 1
print("ATIVIDADE 1")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print()

a_and_b = a & b
a_or_b = a | b

print(f"Primeiro número -> {a}")
print(f"Segundo número -> {b}")
print()

print(f"Resultado da operação AND -> {bin(a_and_b)}")
print(f"Resultado da operação OR -> {bin(a_or_b)}")
print("FIM DA ATIVIDADE 1")
print()
print()


# ATIVIDADE 2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
op = int(input("Selecione sua operação (1 = AND / 2 = OR): "))
print()

a_and_b = a & b
a_or_b = a | b

print(f"Primeiro número -> {a}")
print(f"Segundo número -> {b}")
print()

if op == 1:
    print("Operação escolhida -> AND")
    print(f"Resultado da operação AND -> {bin(a_and_b)}")
elif op == 2:
    print("Operação escolhida -> OR")
    print(f"Resultado da operação OR -> {bin(a_or_b)}")
else:
    print("ERRO")
print("FIM DA ATIVIDADE 2")


