salario = float(input("Salário do Colaborador: "))
print()

if salario <= 280:
    reajuste = 20

elif salario <= 700:
    reajuste = 15

elif salario <= 1500:
    reajuste = 10

else:
    reajuste = 5

aumento = salario * (reajuste / 100)
salario_novo = salario + aumento

print(f"Salário antes do reajuste: {salario}")
print(f"Reajuste aplicado: {reajuste}%")
print(f"Valor do aumento: {aumento}")
print(f"Novo salário: {salario_novo}")