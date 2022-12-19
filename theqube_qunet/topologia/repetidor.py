from no import Nó


# Gerações de repetidores
#   1 - Heralding (conexão anunciada) -> canal clássico e purificação é necessária
#   2 - CQE (Correção quântica de erros)
#   3 - "Redundância" da informação quântica
class Repetidor(Nó):
    def __init__(self, identificador, tipo, geração=1, ruído=None, canais=None):
        super().__init__(identificador=identificador,
                         num_qubits=1,
                         tipo=tipo,
                         ruído=ruído,
                         canais=canais,
                         nó_final=False)
        self.geração = geração

    # TODO: Função para garantir que haja um canal clássico para sinalização
    # TODO: Função para simular purificação do emaranhamento (provavelmente só necessária na estrutura física)

