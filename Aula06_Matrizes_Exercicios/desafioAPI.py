endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# FUNÇÃO QUE VERIFICA SE 1 CÓDIGO HTTP DE UMA
# REQUISIÇÃO É SUCESSO OU NÃO
# 200 --> VERDADEIRO
# 401 --> FALSO

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO QUE VERIFICA SE TEM 2 ERROS SEGUIDOS EM UMA LISTA DE REQUISIÇÕES
# DE UM ENDPOINT
# [200, 200, 401, 200, 500] --> FALSO
# [201, 500, 502, 201, 500] --> VERDADEIRO

def erros_seguidos(codigos):
    for i in range(len(codigos) - 1):
        codigo_atual = codigos[i]
        prox_codigo = codigos[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# LISTA DE REQUISIÇÕES DE 1 ENDPOINT
# [200, 200, 401, 200, 500]

def analisar_endpoint(codigos_endpoint):
    qntdSucessos = 0

    for codigo in codigos_endpoint:
        if eh_sucesso(codigo):
            qntdSucessos += 1

    qtdTotal = len(codigos_endpoint)
    qtdErros = qtdTotal - qntdSucessos
    porcentagemSucesso =  (qntdSucessos / qtdTotal) * 100

    temErrosSeguidos = erros_seguidos(codigos_endpoint)

    if temErrosSeguidos:
        classificacao = "CRÍTICO"
    elif porcentagemSucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qntdSucessos, qtdErros, porcentagemSucesso, classificacao)


# PERCORRENDO A MATRIZ

maiorErro = 0
endpointMaiorErro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_http = status[i]

    qtdSucessos, qtdErros, porcentagemSucesso, classificacao = analisar_endpoint(codigos_http)

    if qtdErros > maiorErro:
        maiorErro = qtdErros
        endpointMaiorErro = nome_endpoint

    print(f"ENDPOINT {nome_endpoint}")
    print(f"Requisições {codigos_http}")
    print(f"Sucessos {qtdSucessos}")
    print(f"Erros {qtdErros}")
    print(f"Porcentagem de Sucesso {porcentagemSucesso}")
    print(f"Classificacao {classificacao}")
    print("-" * 30)
    print()

print(f"Endpoint maior erro: {endpointMaiorErro} ({maiorErro})")