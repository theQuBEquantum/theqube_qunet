from no import Nó
from canal import Canal


# TODO: Docstrings

class Topologia(object):

    def __init__(self, nome, dados):
        self.nome = nome
        self.dados = dados
        self.nós = []
        self.canais = []
        for entidade, identificação in self.dados.items():
            if entidade == 'nó':
                self.criar_nós(identificação)
            if entidade == 'canal':
                for tipo in identificação.keys():
                    self.criar_todos_canais(tipo, identificação[tipo])

    def criar_nós(self, identificação):
        for nó in identificação:
            self.nós.append(self.criar_nó(nó, identificação[nó]))

    def criar_todos_canais(self, tipo, nós1):
        for nó1 in nós1:
            self.criar_canais(nó1, nós1[nó1], tipo)

    def criar_nó(self, identificador, parâmetros):
        if self._checa_nó_único(identificador):
            novo_nó = Nó(identificador)
            self.configura_nó(novo_nó, parâmetros)
            return novo_nó
        return None

    def criar_canais(self, nó1, nós2, tipo):
        # TODO: verificar necessidade de checar canal único
        n1 = self.selecionar_nó(nó1)
        for nó2 in nós2:
            n2 = self.selecionar_nó(nó2)
            novo_canal = Canal(n1, n2, tipo)
            self.configura_canal(novo_canal, nós2[nó2])
            self.canais.append(novo_canal)

    @staticmethod
    def configura_nó(nó, parâmetros):
        for i in vars(nó):
            if i in parâmetros:
                setattr(nó, i, parâmetros[i])

    @staticmethod
    def configura_canal(canal, parâmetros):
        for i in vars(canal):
            if i in parâmetros:
                setattr(canal, i, parâmetros[i])

    def criar_conexão(self, a, b, tipo, comprimento):
        # Retorno de self._checa_nó_único() é (False, identificador do nó existente/True, None)
        # TODO: verificar se um canal é a conexão entre dois nós apenas
        # TODO: verificar a necessidade da função (será possível adicionar uma nova conexão a uma rede existente?)

        aux = self._checa_nó_único(a)
        if aux[0]:
            nó1 = Nó(str(a))
            self.nós.append(nó1)
        else:
            nó1 = aux[1]
        aux = self._checa_nó_único(b)
        if aux[0]:
            nó2 = Nó(str(b))
            self.nós.append(nó2)
        else:
            nó2 = aux[1]
        canal = Canal(nó1, nó2, tipo, comprimento)
        self.canais.append(canal)
        print(f'Uma nova conexão foi criada entre o nó {nó1} e o nó {nó2} por meio do canal {canal}.')
        return nó1, nó2, canal

    def _checa_nó_único(self, identificador):
        for i in range(len(self.nós) - 1):
            if identificador == self.nós[i].identificador:
                print(f'Um nó com identificador {self.nós[i].identificador} já existe na rede!')
                return False, self.nós[i]
        return True, None

    def descrever_rede(self):
        for nó in self.nós:
            nó.listar_conexões()


    def selecionar_nó(self, identificador):
        for nó in self.nós:
            if identificador == nó.identificador:
                return nó
        return None

    def selecionar_canal(self, identificador):
        for canal in self.canais:
            if identificador == canal.identificador:
                return canal
        return None

    def _checa_canal_único(self, identificador):
        for canal in self.canais:
            if identificador == canal.identificador:
                print(f'Canal {canal} já existe na rede!')
                return False
        return True

    def listar_conexões(self):
        for nó in self.nós:
            nó.listar_conexões()
