from recebe_novo_nó import recebe_novo_nó
# TODO: Função desnecessária... excluir


def recebe_dados_nós(número_nós):
    """
    Chama a função recebe_novo_nó() para receber os dados de todos os nós da rede.

    Parâmetros:
        número_nós: o número de nós existentes na rede.

    Retorna:
        dict contendo os identificadores dos nós e seus atributos.

    """
    nós_rede = dict()
    while número_nós:
        nós_rede.update(recebe_novo_nó(nós_rede))
        número_nós -= 1
    print(nós_rede)
    return nós_rede
