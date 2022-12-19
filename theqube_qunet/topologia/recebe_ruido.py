import PySimpleGUI as sg


def recebe_ruído(num_qubits):
    layout = [[[sg.Text(f"Posição {k}"), sg.Listbox(['Ruído 1', 'Ruído 2', 'Ruído 3'],
                                                    key=f'-RUÍDO{k}-')] for k in range(num_qubits)],
              [sg.Button('Ok'), sg.Button('Sair')]]
    janela = sg.Window('Ruído', layout)
    while True:
        evento, valores = janela.read()
        print(evento)
        print(valores)
        print(list(valores.values()))
        if evento in (sg.WIN_CLOSED, 'Sair'):
            janela.close()
            return None
        elif evento == 'Ok':
            ruído = list(valores.values())
            break
    janela.close()
    return ruído
