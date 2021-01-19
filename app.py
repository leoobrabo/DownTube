# Realizar download de video unico ou playlist do youtube via Python

import pytube  # /usr/bin/pip3 install pytube
from pytube import Playlist

# DOWNLOAD UNICO - INFORMAR LINK DO VIDEO


def downloadURL(url):

    youtube = pytube.YouTube(url)

    # traz lista de formato disponiveis
    i = 1
    for lista in youtube.streams.order_by('resolution'):
        try:
            print(lista)
            i += 1
        except:
            pass

    # Conecta para preparar o video
    video = youtube.streams.filter(
        progressive=True, file_extension="mp4").order_by('resolution').last()

    # Titulo do video
    title = video.title
    print("Iniciando Download : " + str(title))

    # Path do Download
    video.download("/home/pinheirocfc/Downloads/")

    print("Download Concluido!")

# DOWNLOAD DE PLAYLIST


def downloadPlaylist(url_playlist):
    pl = Playlist(url_playlist)
    i = 1
    print("Iniciando Download Playlist")
    for video in pl.videos:
        video.streams.filter(progressive=True, file_extension="mp4").order_by(
            'resolution').get_highest_resolution().download("/home/pinheirocfc/Downloads/")
        try:
            # Titulo do video
            title = video.title
            print("Video " + str(i) + ": " +
                  str(title) + " concluído com sucesso!")
            i += 1
        except:
            pass
    print("Iniciando")


# chamar funcao para download unico
downloadURL("https://www.youtube.com/watch?v=DJVPIlDT2zw&list=RDMM&index=2")
# downloadPlaylist("https://www.youtube.com/watch?v=UrT0zCmsN8c&list=PLsEx1ZKe8IpVY9ltdnBW60FOiPqtiMAMD") #download de playlist, copiar url d playlist
exit()
