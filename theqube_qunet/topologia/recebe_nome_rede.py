import PySimpleGUI as sg


def recebe_nome_rede():
    layout = [[sg.T('Insira o nome da rede.')],
              [sg.InputText(key='-NOME-')],
              [sg.Button('Ok')]]

    janela = sg.Window('Nome da rede', layout)
    while True:
        evento, valores = janela.read()
        if evento == 'Ok':
            if valores['-NOME-'] == '':
                continue
            else:
                janela.close()
                return valores['-NOME-']
    janela.close()
    return None
