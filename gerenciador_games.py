##pra rodar tem que ser no terminal, entrando no diretorio da pasta e escrevendo python gerenciador_games.py input1.txt op1.txt temp1.txt saida1.txt
import sys

def adicionaRegistro(arq, game):
    with open(arq, 'a') as file:
        file.write(game + '\n')
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def procuraRegistro(arq, chave):
    with open(arq, 'r') as file:
        registros = file.readlines()
    for i, registro in enumerate(registros):
        if chave in registro:
            return (i, registro)
    return (-1, None)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def removeRegistro(arq, chave):
    rrn, registro = procuraRegistro(arq, chave)
    if rrn != -1:
        registros[rrn] = '*' + registros[rrn][1:]
        with open(arq, 'w') as file:
            file.writelines(registros)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def storageCompaction(arq):
    with open(arq, 'r') as file:
        registros = file.readlines()
    registros = [registro for registro in registros if registro[0] != '*']
    with open(arq, 'w') as file:
        file.writelines(registros)
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def processarOperacoes(entrada, operacoes, temporario, saida_final):
    with open(entrada, 'r') as file:
        registros = file.readlines()

    for operacao in operacoes:
        partes = operacao.split(', ')
        if partes[0] == 'i':
            novo_registro = ', '.join(partes[1:])
            if novo_registro not in registros:
                registros.append(novo_registro + '\n')
        elif partes[0] == 'd':
            chave = partes[1]
            removeRegistro(entrada, chave)

    with open(temporario, 'w') as file:
        file.writelines(registros)

    storageCompaction(temporario)

    with open(temporario, 'r') as file:
        registros = file.readlines()

    with open(saida_final, 'w') as file:
        file.writelines(registros)
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
