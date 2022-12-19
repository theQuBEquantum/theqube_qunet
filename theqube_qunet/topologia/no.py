class Nó(object):
    """
    Esta classe define nós na topologia de uma rede quântica. Um objeto da classe
    Nó é conectado a outros Nós por canais.

    Atributos:
        identificador (str): nome utilizado para referenciar o objeto
        num_qubits (int): número de qubits armazenados no nó
        tipo (str): tecnologia usada na construção do nó
        processador (bool): indica se o nó possui um processador
        detector (bool): indica se o nó possui um detector
        ruído (?): ruído introduzido pelo nó na comunicação
        canais (list): lista de canais aos quais o nó está conectado
        nó_final (bool): indica se o nó é final (end-node)
    """

    def __init__(self,
                 identificador,
                 num_qubits=0,
                 tipo='supercondutor',
                 processador=True,
                 detector=True,
                 ruído=None,
                 canais=None,
                 nó_final=False):
        """
        Construtor da classe Nó.

        Parâmetros:
            identificador (str): nome utilizado para referenciar o objeto
            num_qubits (int): número de qubits armazenados no nó
            tipo (str): tecnologia usada na construção do nó
            processador (bool): indica se o nó possui um processador
            detector (bool): indica se o nó possui um detector
            ruído (?): ruído introduzido pelo nó na comunicação
            canais (list): lista de canais aos quais o nó está conectado
            nó_final (bool): indica se o nó é final (end-node)
        """
        self.identificador = identificador
        self.num_qubits = num_qubits
        self.tipo = tipo
        self.processador = processador
        self.detector = detector
        if ruído is None:
            ruído = []
        self.ruído = ruído
        if canais is None:
            canais = []
        self.canais = canais
        self.nó_final = nó_final

    def adicionar_canal(self, canal):
        """
        Adiciona um canal à lista de canais do nó.

        Parâmetros:
            canal (Canal): canal a ser incluído na lista de canais do nó

        Retorno:
            não retorna nada
        """
        if canal in self.canais:
            raise SyntaxError(f'Canal já está conectado ao nó {self.identificador}')
        else:
            self.canais.append(canal)
        # if canal not in self.canais:
        #     self.canais.append(canal)
        # else:
        #     print(f'Canal já está conectado ao nó {self.identificador}')

    def listar_conexões(self):
        """
        Imprime na tela todas as conexões do nó.

        Parâmetros:
            não recebe parâmetros

        Retorno:
            não retorna nada
        """
        conexões = '\n*-----------------------------*\nNó ' + self.identificador
        print(f'O nó {self.identificador} possui conexões com os seguintes nós:')
        for canal in self.canais:
            conexões += '\n ' + canal.nó2.identificador + canal.identificador
            if canal.nó1 == self:
                print(f'{canal.nó2.identificador} pelo canal {canal.identificador}')
            elif canal.nó2 == self:
                print(f'{canal.nó1.identificador} pelo canal {canal.identificador}')
        return conexões

    def listar_canais(self):
        """
        Imprime na tela todos os canais que possuem conexão com o nó.

        Parâmetros:
            não recebe parâmetros

        Retorno:
            não retorna nada
        """
        print(f'O nó {self.identificador} está conectado aos seguintes canais:')
        for canal in self.canais:
            print(canal.identificador)

    def tornar_nó_final(self):
        """
        Torna o nó um nó final (end-node).

        Parâmetros:
            não recebe parâmetros

        Retorno:
            não retorna nada
        """
        self.nó_final = True
