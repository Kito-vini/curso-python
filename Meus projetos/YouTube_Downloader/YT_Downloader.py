from pytube import YouTube
import PySimpleGUI as sg

# Criando as janelas e layouts
def janelaInicial():
    sg.theme('reddit')
    layout = [
        [sg.Text('Bem vindo ao YouTube Downloader'), sg.Text('            '), sg.Text('By Kito-Vini')], 
        [sg.Text('Digite o link do vídeo: '), sg.Input(key='url1')],
        [sg.Text('Digite o caminho que deseja salvar o vídeo: '), sg.Input(key='dir1')],
        [sg.Button('Continuar')]
    ]
    return sg.Window('YouTube Downloader', layout=layout, finalize=True)

def janelaInfo():
    sg.theme('reddit')
    title = 'Título: ' + yt.title
    views = 'Visualizações: ' + str(yt.views)
    length = 'Tamanho do vídeo: ' + str(yt.length)
    rating = 'Avaliação: ' + str(round(yt.rating, 2))
    layout = [
        [sg.Text(title)],
        [sg.Text(views)],
        [sg.Text(length)],
        [sg.Text(rating)],
        [sg.Button('Download'), sg.Button('Sair')]
    global link = values['url1']
    ]
    return sg.Window('Informações do vídeo', layout=layout, finalize=True)

# Criando a janela inicial para exibição
janela1, janela2 = janelaInicial(), None

# Loop de eventos para leitura da janela
while True:
    # Colhendo as informações das janelas
    window, event, values = sg.read_all_windows()
    link = (values['url1'])
    path = (values['dir1'])
    yt = YouTube(link)
    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela1 and event == 'Continuar':
        janela2 = janelaInfo()
        janela1.hide()
    elif window == janela2 and event == 'Download':
        link = (values['url1'])
        path = (values['dir1'])
        yt = YouTube(link)
        # Pegar resolução máxima
        ys = yt.streams.get_highest_resolution()
        # Iniciando o download
        sg.popup('Iniciando Download...')
        ys.download(path)
        sg.popup('Download concluído')
    elif window == janela2 and event == 'Sair':
        break 




