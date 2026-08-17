# EXERCÍCIO 1 - WHILE
# Faça um programa que exiba a mensagem “Olá, Mundo”.
# Essa mensagem deverá ser exibida repetidamente.
# Ao final de toda iteração da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
# novamente.
# Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”

while True:
    print("Olá, Mundo")

    continuar = int(input("Deseja exibir a mensagem novamente? SIM [1] | Não [2]: "))

    if continuar == 1:
        continue
    elif continuar == 2:
        print("Mensagem cancelada com sucesso!")
        break
    else:
        break