import PySimpleGUI as sg

from recebe_ruido import recebe_ruído


def recebe_novo_nó(nós_rede):
    """
    Recebe os parâmetros de um novo nó a ser inserido na rede quântica.

    Retorna:
        dict (nome_nó: {parâmetros})

    """
    ruído = None
    layout = [[sg.Text('Identificador do nó:'), sg.InputText(key='-ID-')],
              [sg.Spin([i for i in range(1, 21)], initial_value=1, key='-NUM_QUBITS-', enable_events=True), sg.Text('Número de qubits')],
              [sg.Text('Sistema físico: '), sg.Combo(['Supercondutor',
                                                      'Vacância de Diamante', 'Sistema 3',
                                                      'Sistema 4'],
                                                     default_value='Supercondutor',
                                                     key='-SISTEMA-')],
              [sg.Checkbox('Processador', key='-PROCESSADOR-'), sg.Checkbox('Detector', key='-DETECTOR-')],
              [sg.Button('Ok', bind_return_key=True), sg.Button('Inserir ruído'), sg.Button('Sair')]]

    janela = sg.Window('Parâmetros do nó', layout)
    while True:
        evento, valores = janela.read()
        print(evento)
        if evento in (sg.WIN_CLOSED, 'Sair'):
            janela.close()
            return None
        elif evento == 'Inserir ruído':
            ruído = recebe_ruído(valores['-NUM_QUBITS-'])

        elif evento == 'Ok':
            nome_nó = valores['-ID-']
            if not nome_nó:
                sg.popup('Nó sem identificador')
                continue
            if nome_nó in nós_rede:
                sg.popup('Já existe um nó na rede com este identificador.')
                continue
            nó = dict()
            nó[str(nome_nó)] = atributos = dict()
            atributos["num_qubits"] = valores['-NUM_QUBITS-']
            atributos["tipo"] = valores['-SISTEMA-']
            atributos["processador"] = valores['-PROCESSADOR-']
            atributos["detector"] = valores['-DETECTOR-']
            atributos["ruído"] = ruído
            break
    janela.close()
    return nó
