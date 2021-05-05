import sys
import PySimpleGUI as sg
from pytube import YouTube
import threading


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


IniciarInterface()
