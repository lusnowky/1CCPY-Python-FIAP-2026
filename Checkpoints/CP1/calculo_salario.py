# CP1 Uma empresa quer um programa inicial para calcular o salário líquido de um estagiário programador

nome = str(input("Nome do Colaborador: "))
valor_hora = float(input("Valor da hora trabalhada: "))
qntd = int(input("Quantidade de horas trabalhadas: "))
bonus = int(input("Valor do bônus fixo do mês: "))
desconto = float(input("Valor do desconto total do mês: "))

salario_bruto = qntd * valor_hora + bonus
salario_liquido = salario_bruto - desconto

print(f"Colaborador: {nome}")
print(f"Salário Bruto: {salario_bruto}")
print(f"Salário Líquido: {salario_liquido}")