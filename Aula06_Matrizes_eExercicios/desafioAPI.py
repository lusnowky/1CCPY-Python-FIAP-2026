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
        prox_codigo = codigos[i + 1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

def estavel(listaCodigos)
    if listaCodigos