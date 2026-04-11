# imagina... um sistema que recolha a escolhea do usuário
# escolha usuário
# se...
# 0 --> sair do programa
# 1 --> entrar do programa
# ----> erro!

escolha_usuário = 0

match escolha_usuário:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("Erro!")

# A diferença de match case do if, é que no if é possível
# criar relações, enquanto no match case funciona apenas com valores fixos