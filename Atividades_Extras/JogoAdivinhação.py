# Jogo da Adivinhação

TENTATIVAS_MAX = 6

palavras = {
    "frutas": ["banana", "morango", "abacaxi", "melancia"],
    "cores": ["azul", "verde", "amarelo", "vermelho"]
}

categorias = {1: "frutas", 2: "cores"}

print("Escolha uma categoria:")
print("1 - Frutas")
print("2 - Cores")

opcao = int(input("Digite a opção: "))
categoria = categorias[opcao]
lista_palavras = palavras[categoria]

print(f"\nA categoria possui {len(lista_palavras)} palavras.")
posicao = int(input("Escolha a posição da palavra: "))


palavra = lista_palavras[posicao - 1]

letras_descobertas = ["_"] * len(palavra)
letras_tentadas = set()
tentativas = TENTATIVAS_MAX

print(f"\nVocê terá {tentativas} tentativas para descobrir a palavra.\n")

while "_" in letras_descobertas and tentativas > 0:
    print("Palavra: " + " ".join(letras_descobertas))
    print(f"Tentativas restantes: {tentativas}")
    letra = input("Digite uma letra: ").lower()

    if letra in letras_tentadas:
        print("Você já tentou essa letra!\n")
        continue
    letras_tentadas.add(letra)

    if letra in palavra:
        for i, c in enumerate(palavra):
            if c == letra:
                letras_descobertas[i] = letra
    else:
        print("Você errou!")
        tentativas -= 1

    print()

if "_" not in letras_descobertas:
    print(f"Parabéns! Você descobriu a palavra: {palavra}")
else:
    print(f"Suas {TENTATIVAS_MAX} tentativas terminaram.")
    print(f"A palavra era: {palavra}")
