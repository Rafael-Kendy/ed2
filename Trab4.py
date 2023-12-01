import sys
import csv
import re
#Musica=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Musica:
    def __init__(self, id, nome, album, album_id, artists, artists_id, track_number, disc_number, explicit, danceability, 
                 energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, 
                 duration, time_signature, year, release_date):
        self.id = id
        self.nome = nome
        self.album = album
        self.album_id = album_id
        self.artists = artists
        self.artists_id = artists_id
        self.track_number = track_number
        self.disc_number = disc_number
        self.explicit = explicit
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration = duration
        self.time_signature = time_signature
        self.year = year
        self.release_date = release_date
#-----------------------------------------------
    def __str__(self):
        return f'{self.nome} - {self.artists}, {self.year}'
        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def leCSV(entrada, database, tupla_primaria, tupla_nome, tupla_album, tupla_artists, tupla_track_number, tupla_disc_number, 
          tupla_explicit, tupla_key, tupla_mode, tupla_year):
    try:
        with open(entrada, 'r', encoding="utf-8") as arq:
            leitor = csv.reader(arq)
            cabeçalho = next(leitor, None)

            for rrn, linha in enumerate(leitor, start=1):
                nova_mus = Musica(*linha)       #o * quebra linha em varios argumentos
                database.append(nova_mus)
                tupla_primaria.append((nova_mus.id, rrn))
                tupla_nome.append((nova_mus.id, nova_mus.nome))
#-----------------------------------------------
    except Exception as e:
        print(f"Erro ao fazer a leitura do arquivo '{arq}' - {e}")
        sys.exit(1)
        
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def criaArqTuplas(tupla_primaria, tupla_nome):
    with open("indicesPrimarios.txt", 'w') as arq:
        for id, rrn in tupla_primaria:
            arq.write(f'{id},{rrn}\n')
            
    with open("indicesNome.txt", 'w') as arq:
        for id, nome in tupla_nome:
            arq.write(f'{id},{nome}\n')


#Main=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == '__main__':
    if len(sys.argv) != 4:
        #python Trab4.py tracks_features.csv query1.txt output.txt
        print("Uso: python Trab4.py [arquivo de musicas] [arquivo de consulta] [arquivo de saida]")
        sys.exit(1)

    entrada = sys.argv[1]
    consulta = sys.argv[2]
    saida = sys.argv[3]
    
    #tem q fazer as tuplas, id|secundario, um arquivo desse pra cada secundario, busca sequencial aqui
    #um com id|rrn com tem q ta organizado

    database = []
    tupla_primaria = []
    tupla_nome = []
    tupla_album = []
    tupla_artists = []
    tupla_track_number = []
    tupla_disc_number = []
    tupla_explicit = []
    tupla_key = []
    tupla_mode = []
    tupla_year = []
    
    leCSV(entrada, database, tupla_primaria, tupla_nome, tupla_album, tupla_artists, tupla_track_number, tupla_disc_number, 
          tupla_explicit, tupla_key, tupla_mode, tupla_year)
    
    tupla_primaria = sorted(tupla_primaria)
    tupla_nome = sorted(tupla_nome)
    criaArqTuplas(tupla_primaria, tupla_nome)
    
