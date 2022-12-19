class Canal(object):
    """
    Esta classe define canais na topologia de uma rede quântica. Um objeto da classe
    Canal conecta dois objetos da classe Nó.

    Atributos:
            nó1 (Nó): primeiro nó da conexão realizada pelo canal
            nó2 (Nó): segundo nó da conexão realizada pelo canal
            tipo (str): indica se o canal é clássico ou quântico
            comprimento (float): comprimento (em metros) do canal
            ruído (list): ruído introduzido pelo canal na comunicação
            ocupado (bool): indica se o canal está ocupado ou livre
            identificador (str): nome utilizado para referenciar o objeto:
                (nó1, nó2) - tipo

    """
    def __init__(self,
                 nó1,
                 nó2,
                 tipo,
                 comprimento=0,
                 ruído=None):
        """
        Construtor da classe Canal.

        Parâmetros:
            nó1 (Nó): primeiro nó da conexão realizada pelo canal
            nó2 (Nó): segundo nó da conexão realizada pelo canal
            tipo (str): indica se o canal é clássico ou quântico
            comprimento (float): comprimento (em metros) do canal
                padrão: 0, para permitir a criação de canais 'vazios' a serem configurados
            ruído (list): ruído introduzido pelo canal na comunicação
                padrão: []
        """
        self.nó1 = nó1
        self.nó2 = nó2
        self.comprimento = comprimento
        self.tipo = tipo
        if ruído is None:
            self.ruído = []
        self.ruído = ruído
        self.ocupado = False
        self._adicionar_aos_nós()
        self.identificador = str((self.nó1.identificador, self.nó2.identificador))
        if self.tipo == 'clássico':
            self.identificador += ' - clássico'
        else:
            self.identificador += ' - quântico'

    def _adicionar_aos_nós(self):
        """
        Durante a construção de um objeto da classe, adiciona o canal criado
        à lista de canais dos nós conectados.

        Parâmetros:
            não recebe parâmetros

        Retorno:
            não retorna nada

        """
        self.nó1.adicionar_canal(self)
        self.nó2.adicionar_canal(self)



