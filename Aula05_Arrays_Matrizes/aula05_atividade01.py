# Criar uma lista de nomes e exibir todas as combinações entre eles sem repeti-los

nomes = ["Lucas", "Gabi", "Laura", "João"]

for i in range(len(nomes)):
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])