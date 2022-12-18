import PySimpleGUI as sg


def recebe_novo_canal(nós_rede):
    canal = dict()

    layout = [[sg.Text('Nó 1:'), sg.Combo(list(nós_rede.keys()), key='-NÓ1-')],
              [sg.Text('Nó 2:'), sg.Combo(list(nós_rede.keys()), key='-NÓ2-')],
              [sg.Radio('Quântico', 'RADIO1', default=True, key='-QUÂNTICO-'), sg.Radio('Clássico', 'RADIO1', key='-CLÁSSICO-')],
              [sg.Text('Comprimento (km):'), sg.Input(key='-COMPRIMENTO-')],
              [sg.Text('Material:'), sg.Combo(['Fibra óptica',
                                               'Material 2', 'Material 3',
                                               'Material 4'],
                                              default_value='Fibra óptica', key='-MATERIAL-')],
              [sg.Text('Ruído:'), sg.Input(key='-RUÍDO-')],
              [sg.Button('Ok'), sg.Button('Sair')]]

    janela = sg.Window('Parâmetros do canal', layout)
    while True:
        if len(nós_rede) < 2:
            sg.popup('Não há nós suficientes na rede para criar um canal.')
            return None, None, None
        evento, valores = janela.read()
        nome_nó_1 = valores['-NÓ1-']
        nome_nó_2 = valores['-NÓ2-']
        if evento in (sg.WIN_CLOSED, 'Sair'):
            return None, None, None
        elif evento == 'Ok':
            if not nome_nó_1 or not nome_nó_2:
                sg.popup('Escolha os dois nós a serem conectados.')
                continue
            conexão = canal[nome_nó_1] = dict()
            atributos = conexão[nome_nó_2] = dict()
            atributos['comprimento'] = valores['-COMPRIMENTO-']
            atributos['tipo'] = valores['-MATERIAL-']
            atributos['ruído'] = valores['-RUÍDO-']
            break
    identificação = str(nome_nó_1 + '->' + nome_nó_2)
    tipo = 'quântico' if valores['-QUÂNTICO-'] else 'clássico'
    janela.close()
    return canal, tipo, identificação
