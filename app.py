import sys
import PySimpleGUI as sg
from pytube import YouTube
import threading


'''
# Digite o Link do video e o local que deseja salvar o video #

link = input("Digite o link do video que deseja salvar: ")
#path = input("Digite o diretorio que deseja salvar o video:")
yt = YouTube(link)

# Mostra os detalhes do Video #

print('Titulo: ', yt.title)
print('Numero de views: ', yt.views)
print('Tamanho do video: ', yt.length)
print('Avaliação do video: ', yt.rating)

# Usa a maior resolução #

#ys = yt.streams.get_audio_only
#ys = yt.streams.get_highest_resolution()

# Começa o Download do Video #

print('Baixando')
# ys.download(path)
print('Download Completo!')



from pytube import Playlist
pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")
for video in pl.videos:
    video.streams.first().download()

yt = YouTube(link)

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
         return  # do work

yt.register_on_progress_callback(show_progress_bar)

def convert_to_aac(stream, file_handle):
         return  # do work

yt.register_on_complete_callback(convert_to_aac)'''


def BaixarVideo(janela, valores):
    link = valores['link']
    caminho = valores['caminho']
    tra_caminho = f'{caminho}'
    yt = YouTube(link)
    janela['titulo'].update(yt.title)
    janela['views'].update(yt.views)
    janela['tamanho'].update(yt.length)
    janela['avaliacao'].update(yt.rating)
    janela['status'].update('Baixando')
    ys = yt.streams.get_highest_resolution()
    print('Baixando')
    ys.download(tra_caminho)
    print('Download Completo!')
    janela.write_event_value('fim_thread', link)


def IniciarInterface():

    sg.theme('Reddit')

    layout = [
        [sg.Image(r'G:\Dropbox\OHomemnãoparaNunca\DownTube\imagens\youtube.png')],
        [sg.Text('Digite o Link ')],
        [sg.Input(key='link')],
        [sg.Text('Pasta de Saida ')],
        [sg.Input(key='caminho_arquivo'), sg.FolderBrowse(
            'Procurar Pasta', target='caminho_arquivo', key='caminho')],
        [sg.Button('Baixar', key='baixar'), sg.Text('', key='status')],
        [sg.Text('Titulo do video')],
        [sg.Input(key='titulo')],
        [sg.Text('Numero de views ')],
        [sg.Input(key='views')],
        [sg.Text('Tamanho do Video ')],
        [sg.Input(key='tamanho')],
        [sg.Text('Avaliação do video ')],
        [sg.Input(key='avaliacao')]
    ]

    janela = sg.Window(
        'DownTube', layout, icon=r"G:\Dropbox\OHomemnãoparaNunca\DownTube\imagens\iconfinder_youtube.ico")
    threading_baixar_video = None
    while True:
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED:
            janela.close()
            sys.exit()
        elif evento == 'baixar' and threading_baixar_video == None:

            threading_baixar_video = threading.Thread(
                target=BaixarVideo, args=(janela, valores,), daemon=True)
            threading_baixar_video.start()
        elif evento == 'fim_thread':
            threading_baixar_video.join()
            threading_baixar_video = None
            print('Execuçao bem sucedida')

# Link do Video
# https://www.youtube.com/watch?v=hA2l0TgaZhM&ab_channel=DevAprender


IniciarInterface()
