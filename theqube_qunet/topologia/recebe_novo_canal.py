import PySimpleGUI as sg


def recebe_novo_canal(nós_rede):
    canal = dict()
    nós_disponíveis_1 = list(nós_rede.keys())
    layout = [[sg.Text('Nó 1:'), sg.Combo(nós_disponíveis_1, key='-NÓ1-', enable_events=True)],
              [sg.Text('Nó 2:'), sg.Combo(values=nós_disponíveis_1, key='-NÓ2-', enable_events=True)],
              [sg.Radio('Quântico', 'RADIO1', default=True, key='-QUÂNTICO-'), sg.Radio('Clássico',
                                                                                        'RADIO1', key='-CLÁSSICO-')],
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
        print(f'Eventos: {evento}')
        print(f'Valores: {valores}')
        print(f'Nós disp: {nós_disponíveis_1}')
        nome_nó_1 = valores['-NÓ1-']
        print(f'N No 1: {nome_nó_1}')
        nome_nó_2 = valores['-NÓ2-']
        if evento in (sg.WIN_CLOSED, 'Sair'):
            janela.close()
            return None, None, None
        elif evento == '-NÓ1-':
            nós_disponíveis_2 = [nó for nó in nós_disponíveis_1 if nó != nome_nó_1]
            print(f'Nó 1, Nó 2: {nome_nó_1}, {nome_nó_2}')
            print(f'Evento, nós disponíveis : {evento}, {nós_disponíveis_1}')
            janela['-NÓ1-'].update(disabled=True)
            janela['-NÓ2-'].update(values=nós_disponíveis_2)
        elif evento == 'Ok':
            if not nome_nó_1 or not nome_nó_2:
                sg.popup('Escolha os dois nós a serem conectados.')
                continue
            if nome_nó_1 not in nós_rede or nome_nó_2 not in nós_rede:
                sg.popup('Nó selecionado não existe na rede.')
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
    print(canal, tipo, identificação)
    return canal, tipo, identificação
