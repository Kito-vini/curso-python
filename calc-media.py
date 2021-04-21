import PySimpleGUI as sg

# Criando as janelas e layouts
def janelaApresentacao():
    sg.theme('Reds')
    layout = [
        [sg.Text('Calculadora de média escolar'), sg.Text('       '), sg.Text('Program by Kito-Vini')],
        [sg.Text('Digite seu nome:')],
        [sg.Input('nome')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('name', layout=layout, finalize=true)

def janelaCalculadora():
    sg.theme('Reds')
    layout = [
        [sg.Text('Digite a nota da AV1'), sg.Input('av1', key='av1')],
        [sg.Text('Digite a nota da AV2'), sg.Input('av2', key='av2')],
        [sg.Text('Digite a nota da AV3'), sg.Input('av3', key='av3')],
        [sg.Button('Calcular')]
    ]
    return sg.Window('notas', layout=layout, finalize=true)

# Criar janelas iniciais
janela1, janela2 = janelaApresentacao(), None

# loop de eventos para leitura das janelas
while true:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        janela2 = janelaCalculadora()
        janela1.hide()
    if window == janela2 and event == 'Calcular'
        