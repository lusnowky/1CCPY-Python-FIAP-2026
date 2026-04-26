print("Queremos saber se seu voto é obrigatório este ano")
ano = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano

if idade < 16:
    print("Seu voto é proibido")
if (16 <= idade < 18) or idade > 70:
    print("Seu voto é opcional")
if 18 <= idade <= 70:
    print("Seu voto é obrigatório")

