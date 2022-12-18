import PySimpleGUI as sg


# TODO: incluir mais parâmetros e refazer entrada de ruído
# TODO: trocar números por keys nos valores
def recebe_novo_nó():
    """
    Recebe os parâmetros de um novo nó a ser inserido na rede quântica.

    Retorna:
        dict (nome_nó: {parâmetros})

    """
    layout = [[sg.Text('Identificador do nó:'), sg.InputText()],
              [sg.Spin([i for i in range(1, 21)], initial_value=1), sg.Text('Número de qubits')],
              [sg.Text('Sistema físico: '), sg.Combo(['Supercondutor',
                                                      'Vacância de Diamante', 'Sistema 3',
                                                      'Sistema 4'],
                                                     default_value='Supercondutor')],
              [sg.Checkbox('Processador'), sg.Checkbox('Detector')],
              [sg.Text('Ruído:'), sg.Input()],
              [sg.Button('Ok'), sg.Button('Sair')]]

    janela = sg.Window('Parâmetros do nó', layout)
    while True:
        evento, valores = janela.read()
        if evento in (sg.WIN_CLOSED, 'Sair'):
            return None
        elif evento == 'Ok':
            nome_nó = valores[0]
            if not nome_nó:
                sg.popup('Nó sem identificador')
                continue
            nó = dict()
            nó[str(nome_nó)] = atributos = dict()
            atributos["num_qubits"] = valores[1]
            atributos["tipo"] = valores[2]
            atributos["processador"] = valores[3]
            atributos["detector"] = valores[4]
            atributos["ruído"] = valores[5]
            break
    janela.close()
    return nó
