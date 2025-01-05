# Autor: Gerson Ferreira dos Anjos Neto
# Componente Curricular: Algoritmos I
# Concluído em: 16/05/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum trecho de código de colega ou
# de outro autor, tais como provindos de livros e apostilas, e páginas ou documentos eletrônicos da internet.
# Qualquer trecho de código de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código e estou ciente que estes trechos não serão considerados para fins de avaliação.

from utils import *
from unidecode import unidecode

continuarJogo = " "
while continuarJogo:

    menuInicial = ["", ""]  # Vetor que armazenara respectivamente a quantidade de tabuleiros e a dificuldade do jogo.
    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")  # Escolha da quantidade de tabuleiros.
    quantTabs = input("- Single\n"
                      "- Duo\n"
                      "- Exit\n"
                      "> ").lower().replace(" ", "")
    while unidecode(quantTabs) not in ["single", "duo", "exit"]:
        quantTabs = input("Opção inválida! Por favor tente novamente.\n"
                          "Selecione:\n"
                          "- 'Single' para um tabuleiro.\n"
                          "- 'Duo' para dois tabuleiros.\n"
                          "- 'Exit' para sair do jogo.\n"
                          "> ").lower().replace(" ", "")

    menuInicial[0] = quantTabs[0]  # Armazena a quantidade no indice "0".

    if menuInicial[0] == "e":  # Se o usuário escolher "Exit" o jogo se encerra.
        break

    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")  # Escolha da dificuldade do jogo.
    dificuldadeJogo = input("- Fácil\n"
                            "- Intermediario\n"
                            "- Difícil\n> ").lower().replace(" ", "")
    while unidecode(dificuldadeJogo) not in ["facil", "intermediario", "dificil"]:
        dificuldadeJogo = input("Opção inválida! Selecione uma dificuldade para continuar.\n"
                                "> ").lower().replace(" ", "")

    menuInicial[1] = dificuldadeJogo[0]  # Armazena a dificuldade no indice "1".

    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")  # O usuário escolhe se quer definir um limite de rodadas.
    definirRodadas = input("Deseja definir um número de rodadas?\n"
                           "- Sim\n"
                           "- Não\n"
                           "> ").lower().replace(" ", "")
    while unidecode(definirRodadas) not in ["sim", "nao"]:
        definirRodadas = input("Opção inválida! Por favor, tente novamente.\n"
                               "> ").lower().replace(" ", "")

    if definirRodadas[0] == "s":  # Caso sim, o número de rodadas (que deve ser impar) é solicitado.
        numeroRodadas = input("Insira o número de rodadas:\n"
                              "> ")
        while not numeroRodadas.isnumeric() or int(numeroRodadas) % 2 == 0:
            if not numeroRodadas.isnumeric():
                numeroRodadas = input("Por favor, digite apenas números!\n"
                                      "> ")
            else:
                numeroRodadas = input("O número de rodadas deve ser impar!\n"
                                      "> ")
        numeroRodadas = int(numeroRodadas)
    else:
        numeroRodadas = 1000

    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")  # Definição dos jogadores.
    nomeJogador1, *_1 = input("Jogador 1:\n"
                              "> ").title().split(" ")
    while len(nomeJogador1) == 0 or len(nomeJogador1) > 20:
        if len(nomeJogador1) == 0:
            nomeJogador1, *_1 = input("Por favor, insira um nome válido para\n"
                                      "o jogador 1:\n"
                                      "> ").title().split(" ")
        else:
            nomeJogador1, *_1 = input("O nome do jogador 1 deve ter no máximo\n"
                                      "20 caracteres:\n"
                                      "> ").title().split(" ")

    nomeJogador2, *_2 = input("Jogador 2:\n"
                              "> ").title().split(" ")
    while len(nomeJogador2) == 0 or len(nomeJogador2) > 20:
        if len(nomeJogador2) == 0:
            nomeJogador2, *_2 = input("Por favor, insira um nome válido para\n"
                                      "o jogador 2:\n"
                                      "> ").title().split(" ")
        else:
            nomeJogador2, *_2 = input("O nome do jogador 2 deve ter no máximo\n"
                                      "20 caracteres:\n"
                                      "> ").title().split(" ")

    pontosJogador1, pontosJogador2, rounds = 0, 0, 1  # Inicialização da quantidade de pontos e do número de rounds.

    if menuInicial[0] == "s":  # Inicio do jogo (1 Tabuleiro).
        Historico = createHistory(menuInicial)  # Cria o histórico.
        # Cria os tabuleiros de entrada e de resultado.
        tabuleiroSoloGabarito, tabuleiroSoloEntradas = getBoards(menuInicial), getIMatrix(setDifficulty(menuInicial))
        while numeroRodadas:
            print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
            print(" " * 35, f"ROUND {rounds}", " " * 35)
            printMatrixSingle(tabuleiroSoloEntradas, menuInicial)  # Exibe o tabuleiro de entrada.
            # printMatrixSingle(tabuleiroSoloGabarito, menuInicial)  # Exibe o tabuleiro de resultados.

            escolhaJogador1 = getChoice(f"É a vez de {nomeJogador1}", menuInicial)  # Registra a escolha do jogador.
            posicaoEscolhidaJogador1 = "linha" if escolhaJogador1[0] == "l" else "coluna"
            while isComplete(tabuleiroSoloEntradas, escolhaJogador1):  # Impedi que o jogador escolha uma linha/coluna completa.
                escolhaJogador1 = getChoice(f"Esta {posicaoEscolhidaJogador1} já foi preenchida, tente novamente:", menuInicial)
            resultadoJogador1 = checkSum(tabuleiroSoloGabarito, escolhaJogador1)  # Verifica se a soma está correta.
            relacaoSomaJogador1 = operRelational(escolhaJogador1, resultadoJogador1)  # Compara o palpite com a soma correta.
            Historico = updateHistory(Historico, escolhaJogador1, relacaoSomaJogador1)  # Atualiza o histórico.
            print()
            escolhaJogador2 = getChoice(f"É a vez de {nomeJogador2}", menuInicial)
            posicaoEscolhidaJogador2 = "linha" if escolhaJogador2[0] == "l" else "coluna"
            while isComplete(tabuleiroSoloEntradas, escolhaJogador2):
                escolhaJogador2 = getChoice(f"Esta {posicaoEscolhidaJogador2} já foi preenchida, tente novamente:", menuInicial)
            resultadoJogador2 = checkSum(tabuleiroSoloGabarito, escolhaJogador2)
            relacaoSomaJogador2 = operRelational(escolhaJogador2, resultadoJogador2)
            Historico = updateHistory(Historico, escolhaJogador2, relacaoSomaJogador2)

            if resultadoJogador1[0] and resultadoJogador2[0]:  # Caso 1: Ambos os jogadores acertam.
                print("Ambos os jogadores acertaram!")
                # Os pontos são computados para ambos jogadores.
                pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)
                pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2, pontosJogador2)
                # O tabuleiro de entrada e atualizado e impresso, para cada jogada.
                print(f"Revelando a {posicaoEscolhidaJogador1} escolhida por {nomeJogador1}...")
                tabuleiroSoloEntradas = revealAll(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1)
                printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                print(f"Revelando a {posicaoEscolhidaJogador2} escolhida por {nomeJogador2}...")
                tabuleiroSoloEntradas = revealAll(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2)
                printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
            elif resultadoJogador1[0]:  # Caso 2/3: Apenas um dos jogadores acerta.
                print(f"Parabéns {nomeJogador1}, você acertou!")
                print(f"Revelando a {posicaoEscolhidaJogador1} escolhida...")
                # Os pontos são computados para o jogador vencedor.
                pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)
                # O tabuleiro de entradas e atualizado e impresso.
                tabuleiroSoloEntradas = revealAll(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1)
                printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
            elif resultadoJogador2[0]:
                print(f"Parabéns {nomeJogador2}, você acertou!")
                print(f"Revelando a {posicaoEscolhidaJogador2} escolhida...")
                pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)
                tabuleiroSoloEntradas = revealAll(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2)
                printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
            elif not resultadoJogador1[0] and not resultadoJogador2[0]:  # Caso 4: Nenhum dos jogadores acerta.
                print("Nenhum dos jogadores acertou, calculando o palpite mais próximo...")
                # A diferença entre os palpites e as somas corretas e calculada.
                diffSomaJ1, diffSomaJ2 = getDiff(escolhaJogador1, tabuleiroSoloGabarito), getDiff(escolhaJogador2, tabuleiroSoloGabarito)

                if diffSomaJ1 < diffSomaJ2:  # Caso 4.1/4.2: O jogador com o palpite mais próximo tem uma casa revelada.
                    if escolhaJogador1[2] < resultadoJogador1[1]:  # O palpite foi menor do que a soma, o menor valor da linha/coluna é revelado.
                        print(f"{nomeJogador1} chegou mais próximo! O menor valor será revelado na {posicaoEscolhidaJogador1} escolhida...")
                        menorNumeroTab = getLowestNumber(escolhaJogador1, tabuleiroSoloGabarito, tabuleiroSoloEntradas)  # O menor valor e coletado.
                        pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)  # Os pontos são computados.
                        # O tabuleiro de entradas é atualizado e impresso.
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, menorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                    else:  # O palpite foi maior do que a soma, o maior valor da linha/coluna é revelado.
                        print(f"{nomeJogador1} chegou mais próximo! O maior valor será revelado na {posicaoEscolhidaJogador1} escolhida...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador1, tabuleiroSoloGabarito, tabuleiroSoloEntradas)  # O maior valor e coletado.
                        pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)  # Os pontos são computados
                        # O tabuleiro de entradas é atualizado e impresso.
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, maiorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                elif diffSomaJ2 < diffSomaJ1:
                    if escolhaJogador2[2] < resultadoJogador2[1]:
                        print(f"{nomeJogador2} chegou mais próximo! O menor valor será revelado na {posicaoEscolhidaJogador2} escolhida...")
                        menorNumeroTab = getLowestNumber(escolhaJogador2, tabuleiroSoloGabarito, tabuleiroSoloEntradas)
                        pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2, pontosJogador2)
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, menorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                    else:
                        print(f"{nomeJogador2} chegou mais próximo! O maior valor será revelado na {posicaoEscolhidaJogador2} escolhida...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador2, tabuleiroSoloGabarito, tabuleiroSoloEntradas)
                        pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2, pontosJogador2)
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, maiorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                else:  # Caso 4.3: A diferença das somas foi a mesma, ambos os jogadores tem uma casa revelada na linha/coluna escolhida.
                    print("Ambos os jogadores chegaram bem perto!")
                    if escolhaJogador1[2] < resultadoJogador1[1]:  # O palpite foi menor do que a soma, o menor valor da linha/coluna escolhida é revelado.
                        print(f"O menor valor da {posicaoEscolhidaJogador1} escolhida por {nomeJogador1} será revelado...")
                        menorNumeroTab = getLowestNumber(escolhaJogador1, tabuleiroSoloGabarito, tabuleiroSoloEntradas)  # O menor valor e coletado.
                        pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)  # Os pontos são computados.
                        # O tabuleiro de entradas é atualizado e impresso.
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, menorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                    else:  # O palpite foi maior do que a soma, o maior valor da linha/coluna escolhida e revelado.
                        print(f"O maior valor da {posicaoEscolhidaJogador1} escolhida por {nomeJogador1} será revelado...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador1, tabuleiroSoloGabarito, tabuleiroSoloEntradas)  # O maior valor e coletado.
                        pontosJogador1 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador1, pontosJogador1)  # Os pontos são computados.
                        # O tabuleiro de entradas é atualizado e impresso.
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, maiorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                    if escolhaJogador2[2] < resultadoJogador2[1]:
                        print(f"O menor valor da {posicaoEscolhidaJogador2} escolhida por {nomeJogador2} será revelado...")
                        menorNumeroTab = getLowestNumber(escolhaJogador2, tabuleiroSoloGabarito, tabuleiroSoloEntradas)
                        pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2, pontosJogador2)
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, menorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)
                    else:
                        print(f"O maior valor da {posicaoEscolhidaJogador2} escolhida por {nomeJogador2} será revelado...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador2, tabuleiroSoloGabarito, tabuleiroSoloEntradas)
                        pontosJogador2 = getPoints(tabuleiroSoloEntradas, tabuleiroSoloGabarito, escolhaJogador2, pontosJogador2)
                        tabuleiroSoloEntradas = revealOne(tabuleiroSoloEntradas, tabuleiroSoloGabarito, maiorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroSoloEntradas, menuInicial)

            # O placar parcial e o histórico são exibidos ao fim de cada rodada.
            print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
            print("-Placar Parcial")
            print(f"{nomeJogador1} - {pontosJogador1} Pontos")
            print(f"{nomeJogador2} - {pontosJogador2} Pontos")
            print("-=" * 14, " Historico de Jogadas ", "=-" * 14, sep="")
            printHistory(Historico)

            # Caso o tabuleiro de entrada esteja completo o jogo é encerrado, caso contrário o número de rodadas é decresido de 1.
            if verifyBoardIsComplete(tabuleiroSoloEntradas):
                numeroRodadas -= 1
                rounds += 1
            else:
                numeroRodadas = 0

    else:  # Inicio do jogo (2 Tabuleiros).
        # Os tabuleiros de entrada e de resultados são criados, um par para cada jogador.
        tabuleiroGabaritoJ1, tabuleiroEntradasJ1 = getBoards(menuInicial), getIMatrix(setDifficulty(menuInicial))
        tabuleiroGabaritoJ2, tabuleiroEntradasJ2 = getBoards(menuInicial), getIMatrix(setDifficulty(menuInicial))
        # Um histórico e criado para cada jogador.
        HistoricoJogador1, HistoricoJogador2 = createHistory(menuInicial), createHistory(menuInicial)
        while numeroRodadas:
            print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
            print(" " * 35, f"ROUND {rounds}", " " * 35)
            printMatrixSideBySide(tabuleiroEntradasJ1, tabuleiroEntradasJ2, nomeJogador1, nomeJogador2, menuInicial)  # Exibe os tabuleiros de entrada.
            # printMatrixSideBySide(tabuleiroGabaritoJ1, tabuleiroGabaritoJ2, nomeJogador1, nomeJogador2, menuInicial)  # Exibe os tabuleiros de resultado.

            escolhaJogador1 = getChoice(f"É a vez de {nomeJogador1}", menuInicial)  # Registra a escolha do jogador.
            posicaoEscolhidaJogador1 = "linha" if escolhaJogador1[0] == "l" else "coluna"
            while isComplete(tabuleiroEntradasJ1, escolhaJogador1):  # Impedi que o jogador escolha uma linha/coluna completa.
                escolhaJogador1 = getChoice(f"Esta {posicaoEscolhidaJogador1} já foi preenchida, tente novamente:", menuInicial)
            resultadoJogador1 = checkSum(tabuleiroGabaritoJ1, escolhaJogador1)  # Verifica se a soma está correta.
            relacaoSomaJogador1 = operRelational(escolhaJogador1, resultadoJogador1)  # Compara o palpite com a soma correta.
            HistoricoJogador1 = updateHistory(HistoricoJogador1, escolhaJogador1, relacaoSomaJogador1)  # Atualiza o histórico.
            print()
            escolhaJogador2 = getChoice(f"É a vez de {nomeJogador2}", menuInicial)
            posicaoEscolhidaJogador2 = "linha" if escolhaJogador2[0] == "l" else "coluna"
            while isComplete(tabuleiroEntradasJ2, escolhaJogador2):
                escolhaJogador2 = getChoice(f"Esta {posicaoEscolhidaJogador2} já foi preenchida, tente novamente:", menuInicial)
            resultadoJogador2 = checkSum(tabuleiroGabaritoJ2, escolhaJogador2)
            relacaoSomaJogador2 = operRelational(escolhaJogador2, resultadoJogador2)
            HistoricoJogador2 = updateHistory(HistoricoJogador2, escolhaJogador2, relacaoSomaJogador2)

            # A lógica para a avaliação de jogadas em dois tabuleiros é basicamente a mesma utilizada para um tabuleiro...
            # a unica diferença e que cada jogador tem seu tabuleiro atualizado individualmente.
            if resultadoJogador1[0] and resultadoJogador2[0]:
                print("Ambos os jogadores acertaram!")
                pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                print(f"Revelando a {posicaoEscolhidaJogador1} escolhida por {nomeJogador1}...")
                tabuleiroEntradasJ1 = revealAll(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1)
                printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
                print(f"Revelando a {posicaoEscolhidaJogador2} escolhida por {nomeJogador2}...")
                tabuleiroEntradasJ2 = revealAll(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2)
                printMatrixSingle(tabuleiroEntradasJ2, menuInicial)
            elif resultadoJogador1[0]:
                print(f"Parabéns {nomeJogador1}, você acertou!")
                print(f"Revelando a {posicaoEscolhidaJogador1} escolhida...")
                pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                tabuleiroEntradasJ1 = revealAll(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1)
                printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
            elif resultadoJogador2[0]:
                print(f"Parabéns {nomeJogador2}, você acertou!")
                print(f"Revelando a {posicaoEscolhidaJogador2} escolhida...")
                pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                tabuleiroEntradasJ2 = revealAll(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2)
                printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
            elif not resultadoJogador1[0] and not resultadoJogador2[0]:
                print("Nenhum dos jogadores acertou, calculando o palpite mais próximo...")
                diffSomaJ1, diffSomaJ2 = getDiff(escolhaJogador1, tabuleiroGabaritoJ1), getDiff(escolhaJogador2, tabuleiroGabaritoJ2)

                if diffSomaJ1 < diffSomaJ2:
                    if escolhaJogador1[2] < resultadoJogador1[1]:
                        print(f"{nomeJogador1} chegou mais próximo! O menor valor será revelado na {posicaoEscolhidaJogador1} escolhida...")
                        menorNumeroTab = getLowestNumber(escolhaJogador1, tabuleiroGabaritoJ1, tabuleiroEntradasJ1)
                        pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                        tabuleiroEntradasJ1 = revealOne(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, menorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
                    else:
                        print(f"{nomeJogador1} chegou mais próximo! O maior valor será revelado na {posicaoEscolhidaJogador1} escolhida...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador1, tabuleiroGabaritoJ1, tabuleiroEntradasJ1)
                        pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                        tabuleiroEntradasJ1 = revealOne(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, maiorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
                elif diffSomaJ2 < diffSomaJ1:
                    if escolhaJogador2[2] < resultadoJogador2[1]:
                        print(f"{nomeJogador2} chegou mais próximo! O menor valor será revelado na {posicaoEscolhidaJogador2} escolhida...")
                        menorNumeroTab = getLowestNumber(escolhaJogador2, tabuleiroGabaritoJ2, tabuleiroEntradasJ2)
                        pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                        tabuleiroEntradasJ2 = revealOne(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, menorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroEntradasJ2, menuInicial)
                    else:
                        print(f"{nomeJogador2} chegou mais próximo! O maior valor será revelado na {posicaoEscolhidaJogador2} escolhida...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador2, tabuleiroGabaritoJ2, tabuleiroEntradasJ2)
                        pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                        tabuleiroEntradasJ2 = revealOne(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, maiorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroEntradasJ2, menuInicial)
                else:
                    print("Ambos os jogadores chegaram bem perto!")
                    if escolhaJogador1[2] < resultadoJogador1[1]:
                        print(f"O menor valor da {posicaoEscolhidaJogador1} escolhida por {nomeJogador1} será revelado...")
                        menorNumeroTab = getLowestNumber(escolhaJogador1, tabuleiroGabaritoJ1, tabuleiroEntradasJ1)
                        pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                        tabuleiroEntradasJ1 = revealOne(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, menorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
                    else:
                        print(f"O maior valor da {posicaoEscolhidaJogador1} escolhida por {nomeJogador1} será revelado...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador1, tabuleiroGabaritoJ1, tabuleiroEntradasJ1)
                        pontosJogador1 = getPoints(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, escolhaJogador1, pontosJogador1)
                        tabuleiroEntradasJ1 = revealOne(tabuleiroEntradasJ1, tabuleiroGabaritoJ1, maiorNumeroTab, escolhaJogador1)
                        printMatrixSingle(tabuleiroEntradasJ1, menuInicial)
                    if escolhaJogador2[2] < resultadoJogador2[1]:
                        print(f"O menor valor da {posicaoEscolhidaJogador2} escolhida por {nomeJogador2} será revelado...")
                        menorNumeroTab = getLowestNumber(escolhaJogador2, tabuleiroGabaritoJ2, tabuleiroEntradasJ2)
                        pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                        tabuleiroEntradasJ2 = revealOne(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, menorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroEntradasJ2, menuInicial)
                    else:
                        print(f"O maior valor da {posicaoEscolhidaJogador2} escolhida por {nomeJogador2} será revelado...")
                        maiorNumeroTab = getBiggestNumber(escolhaJogador2, tabuleiroGabaritoJ2, tabuleiroEntradasJ2)
                        pontosJogador2 = getPoints(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, escolhaJogador2, pontosJogador2)
                        tabuleiroEntradasJ2 = revealOne(tabuleiroEntradasJ2, tabuleiroGabaritoJ2, maiorNumeroTab, escolhaJogador2)
                        printMatrixSingle(tabuleiroEntradasJ2, menuInicial)

            # O placar parcial e o historico de cada jogador são exibidos ao fim de cada rodada.
            print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
            print(f"{nomeJogador1} - {pontosJogador1} Pontos")
            print(f"{nomeJogador2} - {pontosJogador2} Pontos")
            print("-=" * 14, " Historico de Jogadas ", "=-" * 14, sep="")
            print(f"-=- No tabuleiro de {nomeJogador1} -=-")
            printHistory(HistoricoJogador1)
            print()
            print(f"-=- No tabuleiro de {nomeJogador2} -=-")
            printHistory(HistoricoJogador2)

            # Caso algum dos tabuleiros de entrada esteja completo o jogo é encerrado, caso contrário o número de rodadas é decresido de 1.
            if verifyBoardIsComplete(tabuleiroEntradasJ1) and verifyBoardIsComplete(tabuleiroEntradasJ2):
                numeroRodadas -= 1
                rounds += 1
            else:
                numeroRodadas = 0

    # Ao fim do jogo os pontos são computados e o vencedor (ou empate) é declarado.
    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
    if pontosJogador1 > pontosJogador2:
        print(f"Parabéns {nomeJogador1} você venceu!")
        print("-=" * 16, " Placar Final ", "=-" * 16)
        print(f"{nomeJogador1} - {pontosJogador1} Pontos")
        print(f"{nomeJogador2} - {pontosJogador2} Pontos")
    elif pontosJogador2 > pontosJogador1:
        print(f"Parabéns {nomeJogador2} você venceu!")
        print("-=" * 16, " Placar Final ", "=-" * 16)
        print(f"{nomeJogador1} - {pontosJogador1} Pontos")
        print(f"{nomeJogador2} - {pontosJogador2} Pontos")
    else:
        print(f"Empate! Parabéns a ambos os jogadores!")
        print("-=" * 16, " Placar Final ", "=-" * 16)
        print(f"{nomeJogador1} - {pontosJogador1} Pontos")
        print(f"{nomeJogador2} - {pontosJogador2} Pontos")

    # Caso o usuário escolha "Sim" o jogo reinicia.
    print("-=" * 15 + " Somas Esquecidas " + "=-" * 15, sep="")
    continuarJogo = input("Deseja jogar novamente?\n"
                          "- Sim\n"
                          "- Não\n"
                          "> ").lower().replace(" ", "") == "sim"

print("\nOk! Até a próxima...")
