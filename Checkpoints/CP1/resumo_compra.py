# CP1 Uma loja online quer um programa simples para gerar o resumo de uma compra

produto = str(input("Nome do Produto: "))
preco = float(input("Preço Unitário: "))
qntd = int(input("Quantidade: "))
desconto = float(input("Percentual de Desconto: "))
bruto = preco * qntd
valor_desconto = bruto * (desconto / 100)
valor_final = bruto - valor_desconto

print(f"Produto: {produto}")
print(f"Valor Bruto: {preco}")
print(f"Desconto: {valor_desconto}")
print(f"Valor Final: {valor_final}")