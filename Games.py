#Rafael Kendy, 2478544
#Hugo Massaro, 2383918

class Game:
    # construtor do objeto Game
    def __init__(self, nome=None, genero=None, plataforma=None,
        ano=None, classificacao=None, preco=None, midia=None,
        tamanho=None, produtora=None):
        self.nome = nome
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho
        

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return (self.nome)
#--------------------------------------------------------------
class Indice:
    def _init_(self, inicio_registro, tamanho_registro):
        self.inicio_registro = inicio_registro
        self.tamanho_registro = tamanho_registro
#--------------------------------------------------------------
def imprimiGames(lista):
    for game in lista:
        print(f"Nome: {game.nome}")
        print(f"Produtora: {game.produtora}")
        print(f"Gênero: {game.genero}")
        print(f"Plataforma: {game.plataforma}")
        print(f"Ano: {game.ano}")
        print(f"Classificação: {game.classificacao}")
        print(f"Preço: {game.preco}")
        print(f"Mídia: {game.midia}")
        print(f"Tamanho: {game.tamanho}")
        print("\n")
#------------------------------------------------------------------------------------------
#Le os dados origniais
lista_orig=[]
with open('gamesDatabase.txt', 'r') as arq0:
    for linha in arq0:
        dados=linha.strip().split('|')
        
        games0=Game()
        
        games0.nome=dados[0]
        games0.produtora=dados[1]
        games0.genero=dados[2]
        games0.plataforma=dados[3]
        games0.ano=dados[4]
        games0.classificacao=dados[5]
        games0.preco=dados[6]
        games0.midia=dados[7]
        games0.tamanho=dados[8]
        
        lista_orig.append(games0)
#--------------------------------------------------------------
#Metodo 1: registro de tamanho fixo e campo variavel
#Escrita
tamanho_registro=100
with open('output1.txt', 'w') as arquivo:
    for game in lista_orig:
        registro=f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}|"
        registro=registro.ljust(tamanho_registro-1, ' ')
        registro+='\n'
        arquivo.write(registro)

#Leitura
lista1=[]
with open('gamesDatabase.txt', 'r') as arquivo:
    for linha in arquivo:
        dados=linha.strip().split('|')
        
        games1=Game()
        
        games1.nome=dados[0]
        games1.produtora=dados[1]
        games1.genero=dados[2]
        games1.plataforma=dados[3]
        games1.ano=dados[4]
        games1.classificacao=dados[5]
        games1.preco=dados[6]
        games1.midia=dados[7]
        games1.tamanho=dados[8]
        
        lista1.append(games1)
#imprimiGames(lista1)

#--------------------------------------------------------------
#Metodo 2: quantidade definida de campos
#Escrita
with open('output2.txt', 'w') as arquivo:
    for game in lista_orig:
        registro=f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}|"
        arquivo.write(registro)

#Leitura
with open('output2.txt', 'r') as arquivo:
    dados=arquivo.read()

lista2=[]
registros2=dados.split('|')
registros2.pop() #apaga o ultimo q ta vazio

for i in range(0, len(registros2), 9):
    games2=Game()

    games2.nome=registros2[i]
    games2.produtora=registros2[i+1]
    games2.genero=registros2[i+2]
    games2.plataforma=registros2[i+3]
    games2.ano=registros2[i+4]
    games2.classificacao=registros2[i+5]
    games2.preco=registros2[i+6]
    games2.midia=registros2[i+7]
    games2.tamanho=registros2[i+8]

    lista2.append(games2)    
#imprimiGames(lista2)

#--------------------------------------------------------------
#Metodo 3: começar cada registro com a quantidade de bytes
#Escrita
with open('output3.txt', 'w') as arquivo:
    for game in lista_orig:
        tam=len(game.nome)+len(game.produtora)+len(game.genero)+len(game.plataforma)+len(game.ano)+len(game.classificacao)+len(game.preco)+len(game.midia)+len(game.tamanho)+9
        registro=f"{tam:03d}{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}|"
        arquivo.write(registro)

#Leitura
with open('output3.txt', 'r') as arquivo:
    dados = arquivo.read()

registros3=[]
while dados:
    tam=int(dados[:3])  # Lê os primeiros 3 dígitos como tamanho do registro.
    registro=dados[3:3 + tam]  # Extrai o registro com base no tamanho.
    registros3.append(registro)  # Adiciona o registro à lista.
    dados=dados[3+tam:]  # Move para o próximo registro.

lista3=[]
for reg in registros3:
    campos=reg.split('|')
    games3=Game()

    games3.nome=campos[0]
    games3.produtora=campos[1]
    games3.genero=campos[2]
    games3.plataforma=campos[3]
    games3.ano=campos[4]
    games3.classificacao=campos[5]
    games3.preco=campos[6]
    games3.midia=campos[7]
    games3.tamanho=campos[8]
        
    lista3.append(games3)
#imprimiGames(lista3)

#--------------------------------------------------------------
#Metodo 4: arquivo com os indices
class Indice:
    def __init__(self, inicio_registro, tamanho_registro):
        self.inicio_registro = inicio_registro
        self.tamanho_registro = tamanho_registro

#Escreve o arquivo de indice
def escrever_arquivo_indice(arquivo_dados, arquivo_indice):
    indices = []
    with open(arquivo_dados, 'r') as dados:
        posicao_atual = 0
        while True:
            linha = dados.readline()
            if not linha:
                break
            tamanho_registro = len(linha)
            indices.append(Indice(posicao_atual, tamanho_registro))
            posicao_atual = dados.tell()

    #Escreve os indices no arquivo de indice
    with open(arquivo_indice, 'w') as indice:
        for idx in indices:
            indice.write(f"{idx.inicio_registro}|{idx.tamanho_registro}\n")

#Le o arquivo de indice
def ler_arquivo_indice(arquivo_indice):
    indices = []
    with open(arquivo_indice, 'r') as indice:
        for linha in indice:
            inicio_registro, tamanho_registro = map(int, linha.strip().split('|'))
            indices.append(Indice(inicio_registro, tamanho_registro))
    return indices

#Recupera um registro usando o indice
def recuperar_registro(arquivo_dados, indice):
    with open(arquivo_dados, 'r') as dados:
        dados.seek(indice.inicio_registro)
        registro = dados.read(indice.tamanho_registro)
    return registro


arquivo_dados = 'gamesDatabase.txt'
arquivo_indice = 'output4.txt'

escrever_arquivo_indice(arquivo_dados, arquivo_indice)

indices = ler_arquivo_indice(arquivo_indice)

#--------------------------------------------------------------
#Metodo 5: usando delimitadores
#Escrita
with open('output5.txt', 'w') as arquivo:
    for game in lista_orig:
        registro=f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}"
        arquivo.write(registro+'#')

#Leitura
with open('output5.txt', 'r') as arquivo:
    dados=arquivo.read()
    registros5=dados.split('#')

registros5.pop() #apaga o ultimo registro q ta vazio
lista5=[]
for reg in registros5:
    campos=reg.split('|')
    games5=Game()

    games5.nome=campos[0]
    games5.produtora=campos[1]
    games5.genero=campos[2]
    games5.plataforma=campos[3]
    games5.ano=campos[4]
    games5.classificacao=campos[5]
    games5.preco=campos[6]
    games5.midia=campos[7]
    games5.tamanho=campos[8]
        
    lista5.append(games5)
#imprimiGames(lista5)


