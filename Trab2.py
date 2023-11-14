#python Trab2.py input1.txt op1.txt temp0.txt output0.txt
import sys
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Game:
    # construtor do objeto Game
    def __init__(self, nome=None, produtora=None, genero=None,
        plataforma=None, ano=None, classificacao=None, preco=None,
        midia=None, tamanho=None):
        self.nome = nome
        self.produtora = produtora
        self.genero = genero
        self.plataforma = plataforma
        self.ano = ano
        self.classificacao = classificacao
        self.preco = preco
        self.midia = midia
        self.tamanho = tamanho

    def __str__(self):
        return f"{self.nome}|{self.produtora}|{self.genero}|" \
               f"{self.plataforma}|{self.ano}|{self.classificacao}|" \
               f"{self.preco}|{self.midia}|{self.tamanho}"
    
    def chaveJogo(self):
        chave = (self.nome+self.ano).upper()
        return ''.join(chave.split())
    
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return (self.nome)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def procuraRegistro(nome=None, ano=None, registros=None, chave=None):
    if registros is None:
        return None
    if chave is None:
        novo_registro = (nome.strip() + ano.strip()).upper()
        novo_registro = ''.join(novo_registro.split())
    else:
        novo_registro = chave
    for i, game in enumerate(registros, start=1):
        if novo_registro == game.chaveJogo():
            return i, game
    return None
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def removeRegistro(arq=None, nome=None, ano=None, registros=None, chave=None, espacos_reusaveis=None):
    rrn, registro = procuraRegistro(nome, ano, registros, chave)
    registros[rrn-1].setNome(f"*{espacos_reusaveis}{registro.getNome()}")
    espacos_reusaveis = rrn
    print(registros[rrn-1])
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def processarOperacoes(entrada, operacoes, temporario, saida_final):
    registros = []
    #le o cabecalho e joga os registro na ram
    with open(entrada, 'r') as file:
        cabecalho = file.readline().strip()
        for linha in file:
            dados=linha.strip().split('|')
            game=Game(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
            registros.append(game)
            
    #arruma o cabecalho nas variavel
    partes_cabecalho = cabecalho.split()
    for parte in partes_cabecalho:
        if 'REG.N=' in parte:
            num_registros = int(parte.split('=')[1])
        elif 'TOP=' in parte:
            espacos_reusaveis = int(parte.split('=')[1])

    #faz as op
    for operacao in operacoes:
        partes = operacao.split(',')
    #insere
        if partes[0] == 'i':
            if procuraRegistro(partes[1], partes[5], registros, None)==None:
                partes[1] = partes[1][1:] #tira o espaco q ta no comeco
                game=Game(partes[1], partes[2], partes[3], partes[4], partes[5], partes[6], partes[7], partes[8], partes[9])
                registros.append(game)
    #deleta
        elif partes[0] == 'd':
            if procuraRegistro(None, None, registros, partes[1][1:].strip())!=None:
                removeRegistro(entrada, None, None, registros, partes[1][1:].strip(), espacos_reusaveis)

    #escreve o final
#    with open(saida_final, 'w') as arquivo:
#        for game in registros:
#            registro=f"{game.nome}|{game.produtora}|{game.genero}|{game.plataforma}|{game.ano}|{game.classificacao}|{game.preco}|{game.midia}|{game.tamanho}"
#            arquivo.write(registro+'\n')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Uso: python programa.py [arquivo de entrada] [arquivo de operacoes] [arquivo de saida temporario] [arquivo de saida final]")
        sys.exit(1)

    #Pega os nome
    entrada = sys.argv[1]
    operacoes = []
    with open(sys.argv[2], 'r') as op_file:
        operacoes = op_file.readlines()
    temporario = sys.argv[3]
    saida_final = sys.argv[4]

    processarOperacoes(entrada, operacoes, temporario, saida_final)
