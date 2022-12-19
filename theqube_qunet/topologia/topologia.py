from no import Nó
from canal import Canal
import PySimpleGUI as sg


# TODO: Docstrings

class Topologia(object):
    """
    Esta classe define a topologia de uma rede quântica.
    """

    def __init__(self, nome, dados):
        """
        Construtor da classe Topologia.

        Parâmetros:
            nome (str): nome utilizado para identificar a rede
            dados (dict): dicionário contendo os dados sobre os nós e canais que compõem a rede
        """
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
        """
        Chama a função criar_nó() para cada nó identificado nos dados da rede.
        
        Parâmetros:
            identificação (dict): dados dos nós que compõem a rede

        Retorno:
            não retorna nada
        """
        for nó in identificação:
            self.nós.append(self.criar_nó(nó, identificação[nó]))

    def criar_todos_canais(self, tipo, nós1):
        """
        Chama a função criar_canais() para cada nó da rede.

        Parâmetros:
            tipo (str): indica se os canais a serem criados são clássicos ou quântico
            nós1 (dict): dados sobre os canais a serem criados

        Retorna:
            não retorna nada
        """
        for nó1 in nós1:
            self.criar_canais(nó1, nós1[nó1], tipo)

    def criar_nó(self, identificador, parâmetros):
        """
        Inicializa e configura um objeto da classe Nó

        Parâmetros:
            identificador (str): nome utilizado para referenciar o objeto
            parâmetros (dict): configuração do nó

        Retorno:
            novo_nó (Nó): objeto da classe Nó a ser adicionado aos nós da topologia
        """
        if not self._checa_nó_único(identificador):
            return None
        novo_nó = Nó(identificador)
        self.configura_nó(novo_nó, parâmetros)
        return novo_nó

    def criar_canais(self, nó1, nós2, tipo):
        """
        Inicializa e configura os canais de um determinado nó.
        
        Parâmetros:
            nó1 (str): identificador do nó principal 
            nós2 (dict): dados dos nós a serem conectados a nó1 e as configurações do canal a ser criado
            tipo (str): indica se o canal é clássico ou quântico

        Retorna:
            não retorna nada
        """
        n1 = self.selecionar_nó(nó1)
        for nó2 in nós2:
            if nó1 == nó2:
                print(f"Não é possível criar canal entre {nó1} e {nó2}.")
                raise SyntaxError("Não é possível criar canal entre de um canal para ele mesmo.")
            else:
                n2 = self.selecionar_nó(nó2)
                novo_canal = Canal(n1, n2, tipo)
                self.configura_canal(novo_canal, nós2[nó2])
                self.canais.append(novo_canal)

    @staticmethod
    def configura_nó(nó, parâmetros):
        # Preenche os parâmetros do nó com os dados recebidos da topologia
        for i in vars(nó):
            if i in parâmetros:
                setattr(nó, i, parâmetros[i])

    @staticmethod
    def configura_canal(canal, parâmetros):
        # Preenche os parâmetros do canal com os dados recebidos da topologia
        for i in vars(canal):
            if i in parâmetros:
                setattr(canal, i, parâmetros[i])

    def criar_conexão(self, a, b, tipo, comprimento):
        # Retorno de self._checa_nó_único() é (False, identificador do nó existente/True, None)
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
        """
        Verifica se um nó com este identificador já existe na rede

        Parâmetros:
            identificador (str): nome do nó a verificar

        Retorno:
            único, nó (bool, Nó): True, None se o nó for único; False, identificador se um nó com este identificador
             já existir na rede
        """
        if self.selecionar_nó(identificador):
            return False, self.selecionar_nó(identificador)
        return True, None

        # for i in range(len(self.nós) - 1):
        #     if identificador == self.nós[i].identificador:
        #         print(f'Um nó com identificador {self.nós[i].identificador} já existe na rede!')
        #         return False, self.nós[i]
        # return True, None

    def descrever_rede(self):
        # Imprime na tela o nome da rede, os nós e as conexões entre eles.
        print(self.nome)
        print('Nós:')
        self.listar_nós()
        print('Conexões:')
        for nó in self.nós:
            nó.listar_conexões()

    def descrever_rede_interface(self):
        layout = [[sg.T(f'REDE {self.nome}\n*-----------------------------------------------------------------------'
                        '--------------------------------------*\n')],
                  [sg.Text(f'Nós: {self.listar_nós()}')],
                  [sg.Text(f'Conexões: {self.listar_conexões()}')],
                  [sg.Button('Ok')]]
        janela = sg.Window('Topologia criada com sucesso!', layout)
        while True:
            evento, valores = janela.read()
            if evento in (sg.WIN_CLOSED, 'Ok'):
                janela.close()
                return None

    def selecionar_nó(self, identificador):
        # Recebe um identificador e retorna o nó da rede com este identificador, caso exista.
        for nó in self.nós:
            if identificador == nó.identificador:
                return nó
        return None

    def selecionar_canal(self, identificador):
        # Recebe um identificador e retorna o canal da rede com este identificador, caso exista.
        for canal in self.canais:
            if identificador == canal.identificador:
                return canal
        return None

    def _checa_canal_único(self, identificador):
        # Verifica se um canal com este identificador já existe na rede.
        for canal in self.canais:
            if identificador == canal.identificador:
                print(f'Canal {canal} já existe na rede!')
                return False
        return True

    def listar_conexões(self):
        # Imprime e retorna as conexões da topologia.
        conexões = ''
        for nó in self.nós:
            conexões += nó.listar_conexões()
        return conexões

    def listar_nós(self):
        # Imprime e retorna os nós existentes na topologia.
        lista_nós = ''
        for nó in self.nós:
            print(nó.identificador)
            lista_nós += '\n' + nó.identificador
        return lista_nós
