# Autor: Gerson Ferreira dos Anjos Neto
# Componente Curricular: Algoritmos I
# Concluído em: 16/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou
# de outro autor, tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet.
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código e estou ciente que estes trechos não serão considerados para fins de avaliação.
import random as rd

# Gera um vetor "MenuInicial", que será utilizado por outras funções responsáveis pela
# estetica e funcionamento do jogo.
def setDifficulty(vetorMenuInicial):
    if vetorMenuInicial[1] == "f":
        return [4, 30, 8, 21, 29, 20, 38, 37]
    elif vetorMenuInicial[1] == "i":
        return [5, 60, 12, 29, 26, 27, 24, 23]
    else:
        return [6, 100, 15, 35, 22, 34, 10, 9]

# Gera um vetor com "n" números "aleatórios" que serão utilizados para preencher a matriz.
def generateNumbers(vetorDificuldade):
    listNum = []
    # Tamanho do vetor é definido pelo tamanho da matriz elevado ao quadrado.
    lenListNum = (vetorDificuldade[0] - 1) ** 2
    # O limite da função "randint" e dado pela dificuldade selecionada.
    limitRandom = vetorDificuldade[1]
    for i in range(lenListNum):
        num = rd.randint(1, limitRandom)
        while num in listNum:
            num = rd.randint(1, limitRandom)
        listNum.append(num)
    return listNum

# Utiliza o vetor com os números "aleatórios" para preencher a "rMatrix" (Matriz de Resultados).
def getRMatrix(vetorNumeros, vetorDificuldade):
    # Uma matriz com zeros e criada para armazenar os números supracitados e, futuramente,
    # a soma das linhas e colunas.
    rMatrix = [[0 for i in range(vetorDificuldade[0])] for j in range(vetorDificuldade[0])]
    for i in range(vetorDificuldade[0] - 1):
        for j in range(vetorDificuldade[0] - 1):
            rMatrix[i][j] = vetorNumeros[j]
        vetorNumeros = vetorNumeros[(vetorDificuldade[0] - 1):]
    return rMatrix

# Cria a "iMatriz" (Matriz de Entradas) que será visualizada pelos jogadores.
def getIMatrix(vetorDificuldade):
    iMatrix = [["X" for i in range(vetorDificuldade[0] - 1)] for j in range(vetorDificuldade[0] - 1)]
    return iMatrix

# Calcula a soma de cada linha/coluna da "rMatrix".
def calculateSum(rMatriz):
    for i in range(len(rMatriz) - 1):
        somaLinha, somaColuna = 0, 0
        for j in range(len(rMatriz) - 1):
            somaLinha += rMatriz[i][j]
            somaColuna += rMatriz[j][i]
        rMatriz[i][j + 1] += somaLinha  # Armazena a soma na frente da linha.
        rMatriz[j + 1][i] += somaColuna  # Armazena a soma abaixo da coluna.
    return rMatriz

# Combina as funções criadas até o momento para gerar o(s) tabuleiro(s) dos jogadores.
def getBoards(vetorMenuInicial):
    return calculateSum(getRMatrix(generateNumbers(setDifficulty(vetorMenuInicial)), setDifficulty(vetorMenuInicial)))

# Coleta as entradas de cada jogador e as armazena em um vetor.
def getChoice(Msg, vetorMenuInicial):
    vetorDificuldade = setDifficulty(vetorMenuInicial)
    print(Msg)
    linhaColuna = input("Linha ou Coluna?\n"
                        "> ").lower().replace(" ", "")
    while linhaColuna not in ["linha", "coluna"]:
        linhaColuna = input("Por favor, digite uma opção válida:\n"
                            "> ").lower().replace(" ", "")

    posicaoEscolhida = "linha" if linhaColuna[0] == "l" else "coluna"
    numero = input("Qual?\n"
                   "> ")
    while not numero.isnumeric():
        numero = input("Por favor, digite apenas números!\n"
                       "> ")

    while int(numero) not in range(1, vetorDificuldade[0]):
        numero = input(f"Por favor, insira um número de {posicaoEscolhida} entre 1 e {vetorDificuldade[0] - 1}:\n"
                       f"> ")

    valorSoma = input("Qual o valor da soma?\n"
                      "> ")
    while not valorSoma.isnumeric():
        valorSoma = input("Por favor, insira um valor válido para a soma:\n"
                          "> ")

    return [linhaColuna[0], int(numero), int(valorSoma)]

# Verifica se a linha/coluna selecionada pelo jogador já foi totalmente revelada, retorna "True" ou "False".
def isComplete(iMatriz, vetorSoma):
    quantElementos = len(iMatriz)
    nLinha, nColuna = vetorSoma[1] - 1, vetorSoma[1] - 1
    if vetorSoma[0] == "l":
        for i in range(len(iMatriz)):
            if iMatriz[nLinha][i] != "X":
                quantElementos -= 1
    else:
        for i in range(len(iMatriz)):
            if iMatriz[i][nColuna] != "X":
                quantElementos -= 1
    return quantElementos == 0

# Verifica se a soma do jogador foi exata, retorna "True" ou "False" e o valor correto da soma.
def checkSum(rMatriz, vetorSoma):
    nLinha = vetorSoma[1] - 1
    nSoma = len(rMatriz) - 1
    if vetorSoma[0] == "l":
        return [vetorSoma[2] == rMatriz[nLinha][nSoma], rMatriz[nLinha][nSoma]]
    else:
        return [vetorSoma[2] == rMatriz[nSoma][nLinha], rMatriz[nSoma][nLinha]]

# Calcula a diferença entre o palpite do jogador e a soma correta.
def getDiff(vetorSoma, rMatrix):
    somaCorreta = checkSum(rMatrix, vetorSoma)[1]
    diffSoma = vetorSoma[2] - somaCorreta
    if diffSoma < 0:
        diffSoma *= -1
    return diffSoma

# Coleta o maior valor da linha/coluna escolhida pelo jogador.
def getBiggestNumber(vetorSoma, rMatriz, iMatriz):
    maiorValorLinha, maiorValorColuna = 0, 0
    nLinha, nColuna = vetorSoma[1] - 1, vetorSoma[1] - 1
    if vetorSoma[0] == "l":
        for i in range(len(rMatriz) - 1):
            if rMatriz[nLinha][i] == iMatriz[nLinha][i]:
                continue
            else:
                if rMatriz[nLinha][i] > maiorValorLinha:
                    maiorValorLinha = rMatriz[nLinha][i]
        return maiorValorLinha
    else:
        for i in range(len(rMatriz) - 1):
            if rMatriz[i][nColuna] == iMatriz[i][nColuna]:
                continue
            else:
                if rMatriz[i][nColuna] > maiorValorColuna:
                    maiorValorColuna = rMatriz[i][nColuna]
        return maiorValorColuna

# Coleta o menor valor da linha/coluna escolhida pelo jogador.
def getLowestNumber(vetorSoma, rMatriz, iMatriz):
    menorValorLinha, menorValorColuna = 1000, 1000
    nLinha, nColuna = vetorSoma[1] - 1, vetorSoma[1] - 1
    if vetorSoma[0] == "l":
        for i in range(len(rMatriz) - 1):
            if rMatriz[nLinha][i] == iMatriz[nLinha][i]:
                continue
            else:
                if rMatriz[nLinha][i] < menorValorLinha:
                    menorValorLinha = rMatriz[nLinha][i]
        return menorValorLinha
    else:
        for i in range(len(rMatriz) - 1):
            if rMatriz[i][nColuna] == iMatriz[i][nColuna]:
                continue
            else:
                if rMatriz[i][nColuna] < menorValorColuna:
                    menorValorColuna = rMatriz[i][nColuna]
        return menorValorColuna

# Calcula os pontos feitos pelo jogador na rodada.
def getPoints(iMatrix, rMatrix, vetorSoma, Pontos):
    if vetorSoma[0] == "l":
        if checkSum(rMatrix, vetorSoma)[0]:
            nLinha = vetorSoma[1] - 1
            for i in range(len(iMatrix[nLinha])):
                if iMatrix[nLinha][i] == "X":
                    Pontos += 1
        else:
            Pontos += 1
        return Pontos
    else:
        if checkSum(rMatrix, vetorSoma)[0]:
            nColuna = vetorSoma[1] - 1
            for i in range(len(iMatrix)):
                if iMatrix[i][nColuna] == "X":
                    Pontos += 1
        else:
            Pontos += 1
        return Pontos

# Revela todos os elementos de uma linha/coluna escolhida.
def revealAll(iMatrix, rMatrix, vetorSoma):
    if vetorSoma[0] == "l":
        nLinha = vetorSoma[1] - 1
        for i in range(len(rMatrix[nLinha]) - 1):
            iMatrix[nLinha][i] = rMatrix[nLinha][i]
        return iMatrix
    else:
        nColuna = vetorSoma[1] - 1
        for i in range(len(rMatrix) - 1):
            iMatrix[i][nColuna] = rMatrix[i][nColuna]
        return iMatrix

# Revela um elemento da linha/coluna escolhida, utiliza o retorno das funções "getLowestNumber" e "getBiggestNumber".
def revealOne(iMatrix, rMatrix, elementoEscolhido, vetorSoma):
    if vetorSoma[0] == "l":
        for i in range(len(rMatrix) - 1):
            for j in range(len(rMatrix[i]) - 1):
                if rMatrix[i][j] == elementoEscolhido:
                    iMatrix[i][j] = rMatrix[i][j]
        return iMatrix
    else:
        for i in range(len(rMatrix) - 1):
            for j in range(len(rMatrix[i]) - 1):
                if rMatrix[j][i] == elementoEscolhido:
                    iMatrix[j][i] = rMatrix[j][i]
        return iMatrix

# Verifica se o tabuleiro está completo.
def verifyBoardIsComplete(iMatrix):
    quantX = 0
    for i in range(len(iMatrix)):
        for j in range(len(iMatrix[i])):
            if iMatrix[i][j] == "X":
                quantX += 1
    return quantX > 0

# Cria um dicionário que armazenara o histórico de jogadas, iniciando as chaves com a quantidade
# de linhas/colunas equivalentes ao tamanho da "rMatrix".
def createHistory(vetorMenuInicial):
    Historico = {}
    tamanhoDicionario = setDifficulty(vetorMenuInicial)[0]
    HistoricoLinhas = {f"Linha {i}": [] for i in range(1, tamanhoDicionario)}
    HistoricoColunas = {f"Coluna {i}": [] for i in range(1, tamanhoDicionario)}
    Historico.update(HistoricoLinhas)
    Historico.update(HistoricoColunas)
    return Historico

# ¹Função utilizada para preencher o historico:
# Compara o palpite do jogador com a soma correta, retorna "<', ">" ou "=" a depender do resultado da comparação.
def operRelational(escolhaJogador, resultadoJogador):
    if escolhaJogador[2] < resultadoJogador[1]:
        OperRelacional1 = ">"
    elif escolhaJogador[2] > resultadoJogador[1]:
        OperRelacional1 = "<"
    else:
        OperRelacional1 = "="
    return OperRelacional1

# Atualiza o historico do jogador. ²Evita a repetição de jogadas no histórico.
def updateHistory(Historico, escolhaJogador, OperRelacional):
    posicaoEscolhida = "Linha" if escolhaJogador[0] == "l" else "Coluna"
    # ¹:
    if OperRelacional == "<":
        relacaoSoma = "menor do que"
    elif OperRelacional == ">":
        relacaoSoma = "maior do que"
    else:
        relacaoSoma = "igual a"
    # ²:
    if f"É {relacaoSoma} {escolhaJogador[2]}" not in Historico[f"{posicaoEscolhida} {escolhaJogador[1]}"]:
        Historico[f"{posicaoEscolhida} {escolhaJogador[1]}"].append(f"É {relacaoSoma} {escolhaJogador[2]}")
    return Historico

# Imprimi o historico, dividindo-o por linhas e colunas já escolhidas.
def printHistory(Historico):
    for chave, valor in Historico.items():
        if valor:
            print(f"A soma em {chave}:")
            for elemento in valor:
                print(elemento)

# Imprimi a "iMatrix" para o jogador (1 Tabuleiro).
def printMatrixSingle(iMatriz, vetorMenuInicial):
    # Os valores do "vetorMenuInicial" gerados pela função "setDifficulty" são utilizados
    # para formatar a saida das matrizes.
    for i in range(len(iMatriz)):
        print(end=" " * setDifficulty(vetorMenuInicial)[4])
        for j in range(len(iMatriz)):
            print("[{:^4}]".format(iMatriz[i][j]), end=" ")
        print()

# Imprimi as "iMatrix" para os jogadores (2 Tabuleiros).
def printMatrixSideBySide(iMatrix1, iMatrix2, nomeJogador1, nomeJogador2, vetorMenuInicial):
    # Os valores do "vetorMenuInicial" gerados pela função "setDifficulty" são utilizados
    # para formatar a saida das matrizes.
    formatTerm = [setDifficulty(vetorMenuInicial)[5], setDifficulty(vetorMenuInicial)[6], setDifficulty(vetorMenuInicial)[7]]
    print(f"- {nomeJogador1}", " " * (formatTerm[0] - (len(nomeJogador1) + 2)), sep ="", end ="")
    print(" " * formatTerm[1], end="")
    print(f"- {nomeJogador2}", " " * (formatTerm[0] - (len(nomeJogador2) + 2)), sep ="")
    for i in range(len(iMatrix1)):
        for j in range(len(iMatrix1[i])):
            print("[{:^4}]".format(iMatrix1[i][j]), end=" ")
        print(end = " " * formatTerm[2])
        for k in range(len(iMatrix2[i])):
            print("[{:^4}]".format(iMatrix2[i][k]), end=" ")
        print()