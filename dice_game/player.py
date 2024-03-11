import random

class PlayerTurn:
    def __init__(self):
        # initialize the history of the players movement
        self.log_player_1 = []
        self.log_player_2 = []
    
    # handles the log list of the player movement
    def movement_log(self,player, opponent):
        self.log_player_1.append(player)
        self.log_player_2.append(opponent)
        return self.log_player_1, self.log_player_2
    
    # handles the single player game
    def start_movement_single(self):
        choice = input("Aperte um botão para rolar o dado: ") # Fazer uma verificação para pular a vez
        player_value = random.randint(1, 6)
        opponent_value = random.randint(1,6)
        self.movement_log(player_value, opponent_value)
        return player_value, opponent_value, choice 
    
    # handles the multiplayer game
    def start_movement_multi(self):
        choice_player_1 = input("P1 Aperte um botão para rolar o dado: ")
        player1_value = random.randint(1, 6)
        choice_player_2 = input("P2 Aperte um botão para rolar o dado: ")
        player2_value = random.randint(1,6)
        self.movement_log(player1_value, player2_value)
        return player1_value, player2_value, choice_player_1, choice_player_2 
            