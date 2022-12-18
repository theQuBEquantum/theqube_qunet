import PySimpleGUI as sg

from exportar_arquivo import exportar_arquivo
from recebe_novo_canal import recebe_novo_canal
from recebe_novo_nó import recebe_novo_nó
from topologia import Topologia

rede = dict()
nós = rede['nó'] = dict()
canais = rede['canal'] = dict()
canais_clássicos = canais['clássico'] = dict()
canais_quânticos = canais['quântico'] = dict()
altura = 400
largura = 120
identificação_canais_quânticos = list()
identificação_canais_clássicos = list()

col1 = sg.Column([[sg.Frame('Nós', [[sg.Column([[sg.Listbox([list(nós)],
                                                            key='-LISTA-NÓS-', size=(30, 30))]],
                                               size=(largura, altura))]])]], pad=(0, 0))

col2 = sg.Column([[sg.Frame('Canais quânticos', [[sg.Column([[sg.Listbox([identificação_canais_quânticos],
                                                                         key='-LISTA-CANAIS-QUÂNTICOS-',
                                                                         size=(30, 30)), ]],
                                                            size=(largura, altura))]])]], pad=(0, 0))

col3 = sg.Column([[sg.Frame('Canais clássicos', [[sg.Column([[sg.Listbox([identificação_canais_quânticos],
                                                                         key='-LISTA-CANAIS-CLÁSSICOS-',
                                                                         size=(30, 30)), ]],
                                                            size=(largura, altura))]])]], pad=(0, 0))

col4 = sg.Column([[sg.Frame('Ações:',
                            [[sg.Column([[sg.Button('Novo nó'),
                                          sg.Button('Novo canal'),
                                          sg.Button('Simular'),
                                          sg.Button('Salvar'),
                                          sg.Button('Sair')]],
                                        size=(largura * 3 + 60, 45), pad=(0, 0))]])]], pad=(0, 0))
sg.Text()
layout = [[sg.T('QuNET', font='_ 18')],
          [col1, col2, col3],
          [col4]]

janela = sg.Window('QuNET', layout, finalize=True)

while True:
    evento, valores = janela.read()
    if evento in (sg.WIN_CLOSED, 'Sair'):
        break
    elif evento == 'Novo nó':
        novo_nó = recebe_novo_nó()
        nós.update(novo_nó)
        janela['-LISTA-NÓS-'].update(nós)
        continue
    elif evento == 'Novo canal':
        novo_canal = recebe_novo_canal(nós)
        if novo_canal == (None, None, None):
            continue
        nó1 = list(novo_canal[0].keys())[0]  # TODO: Melhorar (possivelmente colocar no retorno de novo_canal())
        if novo_canal[1] == 'quântico':
            if canais_quânticos and nó1 in canais_quânticos:
                canais_quânticos[nó1].update(novo_canal[0][nó1])
            else:
                canais_quânticos.update(novo_canal[0])
            identificação_canais_quânticos.append(novo_canal[2])
            janela['-LISTA-CANAIS-QUÂNTICOS-'].update(identificação_canais_quânticos)
        elif novo_canal[1] == 'clássico':
            if canais_clássicos and nó1 in canais_clássicos:
                canais_clássicos[nó1].update(novo_canal[0][nó1])
            else:
                canais_clássicos.update(novo_canal[0])
            identificação_canais_clássicos.append(novo_canal[2])
            janela['-LISTA-CANAIS-QUÂNTICOS-'].update(identificação_canais_clássicos)
        continue
    elif evento == 'Simular':
        rede_teste = Topologia('rede_teste', rede)
        rede_teste.descrever_rede()  # TODO: Imprimir saída em tela da GUI
        break
    elif evento == 'Salvar':
        exportar_arquivo(rede)
        break

janela.close()
