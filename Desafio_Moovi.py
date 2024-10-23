# Linguagem Python
# Programa criado para desafio proposto pela Moovi Education
# Foi solicitado para criar um jogo joken-po contra a maquina
# Incrementos de funções extras: Modos de partida, Resultados, Ao sair mostra as estatistica gerais.
# Precisa-se revisar ( pode conter erros )

from random import randint
from time import sleep
import textwrap

def menu():
    menu = """\n
    ======= Opções de Jogo =======
    [1]\tSequencia de Partidas
    [3]\tMelhor de 3 Partidas
    [7]\tMelhor de 7 Partidas
    [9]\tMelhor de 9 Partidas
    [0]\tSair
    
    => """
   
    return input(textwrap.dedent(menu) + "Selecione o modo de partidas desejado: ")

# Estatísticas
total_partidas = 0
total_vitorias_player = 0
total_vitorias_maquina = 0
empates = 0


#Inserir Jogada do User
def Player():
    #Apresentar as opções:
    print(""" - Por favor escolha uma dentre as 3 opções:
    [0] Tesoura
    [1] Pedra
    [2] Papel """)
    
    while True:
        try: 
            player = int(input("\nInsira sua escolha: "))
            if player in [0, 1, 2]:
                print(f"Você escolheu o item: {itens[player]}")
                return player
            else:
                print("Opção selecionada está incorreta. Insira novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número (0, 1 ou 2).")
            

# Vaiavel Itens
itens = ("tesoura", "pedra", "papel")

def jogar_partida():
    maquina = randint(0, 2)
    player = Player()


    # Iniciando a disputa
    print("\nJO-KEN-PO\n")


    # Mostrando as jogadas de cada player
    print('*' * 20)
    print(f'-> Maquina Escolheu: {itens[maquina]}')
    print(f'-> Player Escolheu: {itens[player]}')
    print('*' * 20)

    # Estrutura Lógica
    #Tesoura
    if maquina == 0:
        if player == 0:
            print("\nEmpate")
            return "empate"
            
        elif player == 1:
            print("\nVocê Ganhou! Parabéns!")
            return "player"
            
        elif player == 2:
            print("\nMaquina Ganhou! Não Desista!")
            return "maquina"
            
        else:
            print("\nOpção selecionada está incorreto")

    #Pedra
    if maquina == 1:
        if player == 0:
            print("\nMaquina Ganhou! Não Desista!")
            return "maquina"
            
        elif player == 1:
            print("\nEmpate!")
            return "empate"
            
        elif player == 2:
            print("\nVocê Ganhou! Parabéns!!")
            return "player"
            
        else:
            print("\nOpção selecionada está incorreto")
            
    #Papel
    if maquina == 2:
        if player == 0:
            print("\nVocê Ganhou! Parabéns!!")
            return "player"
            
        elif player == 1:
            print("\nMaquina Ganhou! Não Desista!")
            return "maquina"
            
        elif player == 2:
            print("\nEmpate!!")
            return "empate"
            
        else: 
            print("\nOpção selecionada está incorreto")
            
            
            
# Loop principal para o menu e o jogo
while True:
    option = menu()

    if option == "0":
        print("\nSaindo do jogo. Até a próxima!")
        if total_partidas > 0:
            percentual_vitorias = (total_vitorias_player / total_partidas) * 100
            percentual_derrotas = (total_vitorias_maquina / total_partidas) * 100
            percentual_empates = (empates / total_partidas) * 100
            
            print(f"\nEstatísticas do Jogo:")
            print(f"-> Total de Partidas Jogadas: {total_partidas}")
            print(f"-> Vitórias: {total_vitorias_player} ({percentual_vitorias:.2f}%)")
            print(f"-> Derrotas: {total_vitorias_maquina} ({percentual_derrotas:.2f}%)")
            print(f"-> Empates: {empates} ({percentual_empates:.2f}%)")
        else:
            print("\nNenhuma partida foi jogada.")
        break
    
    elif option in ["1", "3", "7", "9"]:
        partidas = int(option)
        vitorias_player = 0
        vitorias_maquina = 0

        if partidas == 1:
            while True:
                vencedor = jogar_partida()
                total_partidas += 1
                if vencedor == "player":
                    #vitorias_player += 1
                    total_vitorias_player += 1
                elif vencedor == "maquina":
                    #vitorias_maquina += 1
                    total_vitorias_maquina += 1
                else:
                    empates += 1    

                jogar_novamente = input("\nDeseja continuar jogando? (y/n): ")
                if jogar_novamente != "y":
                    break

        else:
            for _ in range(partidas):
                vencedor = jogar_partida()
                total_partidas += 1
                if vencedor == "player":
                    vitorias_player += 1
                    total_vitorias_player += 1
                elif vencedor == "maquina":
                    vitorias_maquina += 1
                    total_vitorias_maquina
                else:
                    empates += 1

            print(f"\nResultado Final: Player {vitorias_player} x {vitorias_maquina} Máquina")
            if vitorias_player > vitorias_maquina:
                print("\nParabéns, você venceu a série!")
            elif vitorias_player < vitorias_maquina:
                print("\nA máquina venceu a série. Não desista!")
            else:
                print("\nA série terminou empatada!")

    else:
        print("--- Opção Inválida ---")

menu()
