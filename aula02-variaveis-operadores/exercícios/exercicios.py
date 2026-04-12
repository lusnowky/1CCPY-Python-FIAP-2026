# EXERCICIO 1
raio = int(input("Qual o raio do círculo?: "))
pi = 3.14159
area = pi * raio**2
print("A área do círculo é", area)

# EXERCICIO 2
fahrenheit = int(input("Qual a temperatura em Fahrenheit?: "))
celsius = (fahrenheit - 32) * 5/9
print("A temperatura em Grau Celsius é", celsius)

# obs: O EXERCICIO 3 é o mesmo que o EXERCICIO 2

# EXERCICIO 4
livro = 25
caneta = 5
print(f"O valor de cada livro é de R${livro}")
print(f"O valor de cada caneta é de R${caneta}")
qntd_livros = int(input("Quantos livros você comprou?: "))
qntd_caneta = int(input("Quantas canetas você comprou?: "))
total_livros = livro * qntd_livros
total_caneta = caneta * qntd_caneta
total = total_livros + total_caneta
print(f"Você gastou ao todo R${total}")

# EXERCICIO 5
distancia = int(input("Você foi viajar de carro, qual a distância percorrida?: " ))
velocidade = int(input("Qual foi velocidade média do carro durante o percurso?: "))
tempo = distancia / velocidade
print(f"O carro demorou {tempo} horas para percorrer {distancia}km")

# EXERCICIO 6
A = int(input("Nota da atividade 1: "))
B = int(input("Nota da atividade 2: "))
media = (A + B) / 2
print("A média das atividades é", media)

# EXERCICIO 7
nota_a = int(input("Nota da prova 1: "))
peso_a = int(input("Peso da prova 1: "))
nota_b = int(input("Nota da prova 2: "))
peso_b = int(input("Peso da prova 2: "))
media = (((nota_a * peso_a) + (nota_b * peso_b)) / (peso_a + peso_b))
print("A média das provas é", media)

# EXERCICIO 8
peca1 = 15
pecas2 = 9
print(f"O valor unitário da peça1 é de R${peca1}")
print(f"O valor unitário da peças2 é de R${pecas2}")
qntd_peca1 = int(input("Quantos peças1 você quer?: "))
qntd_pecas2 = int(input("Quantas peças2 você quer"))
total_peca1 = peca1 * qntd_peca1
total_pecas2 = pecas2 * qntd_pecas2
total_pecas = total_peca1 + total_pecas2
print(f"Você deverá pegar R${total_pecas}")

# EXERCICIO 9
dinheiro = 50
pastel_queijo = 10.99
pastel_carne = 11.99
pastel_frango = 13.99
pastel_especial = 19.99
print("Você foi a feira com uma nota de R$50 para comer pastel")
print(f"Pastel de Queijo - R${pastel_queijo}")
print(f"Pastel de Carne - R${pastel_carne}")
print(f"Pastel de Frango - R${pastel_frango}")
print(f"Pastel de Especial - R${pastel_especial}")
sabor = (input("Qual o sabor de pastel você quer? (Queijo/Carne/Frango/Especial): ")).strip().capitalize()
if sabor == "Queijo":
    print(f"Ok, você comprou seu pastel e seu troco é de R${dinheiro - pastel_queijo}")
elif sabor == "Carne":
    print(f"Ok, você comprou seu pastel e seu troco é de R${dinheiro - pastel_carne}")
elif sabor == "Frango":
    print(f"Ok, você comprou seu pastel e seu troco é de R${dinheiro - pastel_frango}")
elif sabor == "Especial":
    print(f"Ok, você comprou seu pastel e seu troco é de R${dinheiro - pastel_especial}")
else:
    print("Sabor de pastel não encontrado")