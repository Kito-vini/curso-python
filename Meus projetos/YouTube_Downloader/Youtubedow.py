from pytube import YouTube

#Digitar o link do vídeo e o local que deseja salvar o vídeo
link = input('Digite o link do vídeo que deseja baixar: ')
path = input('Digite o local que deseja salvar o vídeo: ')
yt = YouTube(link)

#Mostrar detalhes do vídeo
print('Título: ', yt.title)
print('Número de views: ', yt.views)
print('Tamanho do vídeo: ', yt.length, 'Segundos')
print('Avaliação do vídeo', yt.rating)

#Usar a maior resolução
ys = yt.streams.get_highest_resolution()

#Iniciar download do vídeo
print('Iniciando Download...')
ys.download(path)
print('Download Completo')
