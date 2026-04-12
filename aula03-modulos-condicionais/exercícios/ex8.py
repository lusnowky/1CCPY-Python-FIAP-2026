salario = float(input("Salário do colaborador: "))
print()

if salario <= 280:
    reajuste = 20
    aumento = salario * (reajuste / 100)
    salario_novo = salario + aumento
    print(f"Salário antes do reajuste: {salario}")
    print(f"Reajuste aplicado: {reajuste}%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salário: {salario_novo}")

if 280 < salario <= 700:
    reajuste = 15
    aumento = salario * (reajuste / 100)
    salario_novo = salario + aumento
    print(f"Salário antes do reajuste: {salario}")
    print(f"Reajuste aplicado: {reajuste}%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salário: {salario_novo}")

if 700 < salario <= 1500:
    reajuste = 10
    aumento = salario * (reajuste / 100)
    salario_novo = salario + aumento
    print(f"Salário antes do reajuste: {salario}")
    print(f"Reajuste aplicado: {reajuste}%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salário: {salario_novo}")

if salario > 1500:
    reajuste = 5
    aumento = salario * (reajuste / 100)
    salario_novo = salario + aumento
    print(f"Salário antes do reajuste: {salario}")
    print(f"Reajuste aplicado: {reajuste}%")
    print(f"Valor do aumento: {aumento}")
    print(f"Novo salário: {salario_novo}")