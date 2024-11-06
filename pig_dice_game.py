import random


def roll(): # Função que simula o lançamento de um dado de 6 lados
    min_value = 1 # Valor mínimo que o dado pode ter
    max_value = 6 # Valor máximo que o dado pode ter
    roll = random.randint(min_value, max_value) # Gera um número aleatório entre 1 e 6

    return roll # Retorna o valor do dado

while True: # Loop para pedir o número de jogadores, que deve estar entre 2 e 4
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit(): # Verifica se o valor inserido é um número
        players = int(players)
        if 2 <= players <= 4: # Verifica se o número de jogadores está entre 2 e 4
            break # Se estiver dentro do limite, sai do loop
        else:
            print("Must be between 2 - 4 players.") # Mensagem de erro se o número não estiver no intervalo
    else:
        print("Invalid, try again.") # Mensagem de erro se o valor inserido não for um número

max_score = 50 # Define a pontuação máxima para vencer
player_scores = [0 for _ in range(players)] # Cria uma lista para armazenar as pontuações de cada jogador, inicializada com zero

while max(player_scores) < max_score: # Loop principal que continua enquanto nenhum jogador atingir a pontuação máxima  

    for player_idx in range(players): # Loop para cada jogador, por vez
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0 # Pontuação atual do turno é reiniciada para cada jogador

        while True: # Loop para rolar o dado até o jogador decidir parar ou tirar 1
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y": # Se o jogador não quiser rolar, o turno acaba
                break

            value = roll() # Chama a função roll() para obter o valor do dado
            if value == 1: # Se o jogador rolar um 1, perde a pontuação acumulada no turno e o turno acaba
                print("You rolled a 1! Turn done!")
                current_score = 0 # Reseta a pontuação atual do turno
                break
            else:
                current_score += value # Adiciona o valor do dado à pontuação do turno
                print("You rolled a", value)

            print("Your score is:", current_score)
    
        player_scores[player_idx] += current_score # Adiciona a pontuação do turno à pontuação total do jogador
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores) # Identifica o jogador com a maior pontuação
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score) # Exibe o vencedor do jogo
