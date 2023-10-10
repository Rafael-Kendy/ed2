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
#-------------------------------------------------------------------------
#Metodo 1


#Metodo 2: quantidade definida de campos
#lista_games2=[]
#with open('H:\\ED2\\Games\\gamesDatabase.txt', 'r') as arquivo2:
#    for linha in arquivo2:
#        partes=linha.strip().split('|')
#        
#        cont=0
#        games2=Game()
#        games2.nome=partes[cont]
#        cont+=1
#        games2.produtora=partes[cont]
#        cont+=1
#        games2.genero=partes[cont]
#        cont+=1
#        games2.plataforma=partes[cont]
#        cont+=1
#        games2.ano=partes[cont]
#        cont+=1
#        games2.classificacao=partes[cont]
#        cont+=1
#        games2.preco=partes[cont]
#        cont+=1
#        games2.midia=partes[cont]
#        cont+=1
#        games2.tamanho=partes[cont]
#        cont+=1
#        
#        lista_games2.append(games2)
#        
#with open('H:\\ED2\\Games\\gamesDatabase2.txt', 'w') as arquivo2:
#    for i in range(len(lista_games2)):
#        linha=f"{lista_games2[i].nome}|{lista_games2[i].produtora}|{lista_games2[i].genero}|{lista_games2[i].plataforma}|{lista_games2[i].ano}|{lista_games2[i].classificacao}|{lista_games2[i].preco}|{lista_games2[i].midia}|{lista_games2[i].tamanho}|"
#        arquivo2.write(linha)

#Metodo 5: usando delimitadores
lista_games5=[]
with open('H:\\ED2\\Games\\gamesDatabase.txt', 'r') as arq5:
    for linha in arq5:
        partes=linha.strip().split('|')
        
        games5=Game()
        
        games5.nome=partes[0]
        games5.produtora=partes[1]
        games5.genero=partes[2]
        games5.plataforma=partes[3]
        games5.ano=partes[4]
        games5.classificacao=partes[5]
        games5.preco=partes[6]
        games5.midia=partes[7]
        games5.tamanho=partes[8]
        
        lista_games5.append(games5)
        
with open('H:\\ED2\\Games\\gamesDatabase5.txt', 'w') as arq5:
    for games5 in lista_games5:
        linha=f"{games5.nome}|{games5.produtora}|{games5.genero}|{games5.plataforma}|{games5.ano}|{games5.classificacao}|{games5.preco}|{games5.midia}|{games5.tamanho}"