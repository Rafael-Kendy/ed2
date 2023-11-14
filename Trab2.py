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
            
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def procuraRegistro():
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def processarOperacoes(entrada, operacoes, temporario, saida_final):
    registros = []

    with open(entrada, 'r') as file:
        cabecalho = file.readline().strip()
        for linha in file:
            dados=linha.strip().split('|')
            game=Game(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7], dados[8])
            registros.append(game)

    partes_cabecalho = cabecalho.split()
    for parte in partes_cabecalho:
        if 'REG.N=' in parte:
            num_registros = int(parte.split('=')[1])
        elif 'TOP=' in parte:
            espacos_reusaveis = int(parte.split('=')[1])

    for operacao in operacoes:
        partes = operacao.split(',')
        if partes[0] == 'i':
            novo_registro = (partes[1].strip()+partes[5].strip()).upper()
            novo_registro = ''.join(novo_registro.split())
            chave_existente = any(novo_registro == game.chaveJogo() for game in registros)
            if chave_existente==False:
                partes[1] = partes[1][1:] #tira o espaco q ta no comeco
                game=Game(partes[1], partes[2], partes[3], partes[4], partes[5], partes[6], partes[7], partes[8], partes[9])
                registros.append(game)
            
        elif partes[0] == 'd':
            chave_deleta = partes[1]
            chave_deleta = chave_deleta[1:].strip()
            chave_existente = any(chave_deleta == game.chaveJogo() for game in registros)
            if chave_existente==True:
                removeRegistro(entrada, chave_deleta)
        



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Uso: python programa.py [arquivo de entrada] [arquivo de operacoes] [arquivo de saida temporario] [arquivo de saida final]")
        sys.exit(1)

    entrada = sys.argv[1]
    operacoes = []
    with open(sys.argv[2], 'r') as op_file:
        operacoes = op_file.readlines()
    temporario = sys.argv[3]
    saida_final = sys.argv[4]

    processarOperacoes(entrada, operacoes, temporario, saida_final)