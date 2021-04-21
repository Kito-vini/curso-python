import PySimpleGUI as sg

# Criando as janelas e layouts
def janelaApresentacao():
    sg.theme('Reds')
    layout = [
        [sg.Text('Calculadora de média escolar'), sg.Text('       '), sg.Text('Program by Kito-Vini')],
        [sg.Text('Digite seu nome:')],
        [sg.Input('nome', key='nome')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('name', layout=layout, finalize=True)

def janelaCalculadora():
    sg.theme('Reds')
    layout = [
        [sg.Text('Digite a nota da AV1'), sg.Input('av1', key='av1', size=(20,1))],
        [sg.Text('Digite a nota da AV2'), sg.Input('av2', key='av2', size=(20,1))],
        [sg.Text('Digite a nota da AV3'), sg.Input('av3', key='av3', size=(20,1))],
        [sg.Button('Calcular'), sg.Button('Sair')]
    ]
    return sg.Window('notas', layout=layout, finalize=True)

# Criar janelas iniciais
janela1, janela2 = janelaApresentacao(), None

# Criar a função calcular
def calcular():
    media = (float(values['av1']) + float(values['av2']) + float(values['av3'])) / 3
    print(media)
    if media >= 7:
        sg.popup('Sua média é: ', media, 'Parabéns! Você foi aprovado')
    elif media <= 5.9:
        sg.popup('Sua média é: ', media, 'Que pena. Você foi reprovado.')
    else:
        sg.popup('Sua média é: ', media, 'Você está de recuperação. Estude mais!')
    return media

# loop de eventos para leitura das janelas
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        nome = values['nome']
        sg.popup('Olá', nome, 'Vamos calcular sua média?')
        janela2 = janelaCalculadora()
        janela1.hide()
    if window == janela2 and event == 'Calcular':
        calcular()
    if window == janela2 and event == 'Sair':
        break
        
        