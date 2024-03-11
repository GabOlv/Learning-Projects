from player import PlayerTurn
import os

# Class to handle major part of the movimentation of the players
class BoardPath:
    def __init__(self):
        # Initizalize the instance of the turn, values of players and an "emergency quit"
        self.force_exit = 'no'
        self.players_turn = PlayerTurn()
        self.player_1, self.player_2 = 0, 0
    
    # Defines how many points to win
    def map_length(self):
        length = int(input("Select the map lenght (24 - 144): "))
        if length >= 24 and length <= 144:
            return length 
        else:
            return f'Error, out of bounds {length}'
    
    # Handles the pontuation of the players
    def map_movimentation(self, players_movement, length):
        if self.player_1 != length or self.player_2 != length:
            self.player_1 += players_movement[0]
            self.player_2 += players_movement[1]
        elif self.player_1 == length:
            print("Player 1 Win!")
        elif self.player_2 == length:
            print("Player 2 Win!")
    
    # handles the overflow of points        
    def points_handler(self, length):   
        if (self.player_1 > length):
            temp_player_1 = self.player_1 - length # 22 - 20 = 2
            self.player_1 = length - temp_player_1
        if (self.player_2 > length):
            temp_player_2 = self.player_2 - length # 22 - 20 = 2
            self.player_2 = length - temp_player_2
    
    # To do: Funtion to handle same positions
    def verify_positions(self, lenght):
        pass
    
    # Handles all the loop process of the game
    def start(self, length, number_players):
        # Only runs if there are no winner yet
        while ((self.player_1 != length) or (self.player_2 != length)):
            # Single player
            if number_players == 1:
                players_movement = self.players_turn.start_movement_single()
                if players_movement[2] == 'break':
                    break
            # Multiplayer
            if number_players == 2:
                players_movement = self.players_turn.start_movement_multi()
                if players_movement[2] == 'break' and players_movement[3] == 'break':
                    break
            # Calls the method to give points
            self.map_movimentation(players_movement, length)   
            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')
            # Prints the position of each player and the history of they movements
            print(f"player 1 Points: {self.player_1}/{length} Movements: {self.players_turn.log_player_1}")
            print(f"player 2 Points: {self.player_2}/{length} Movements: {self.players_turn.log_player_2}")
            # Calls the function to verify and correct the overflow of points
            self.points_handler(length)
            # Verify if the players won at the same time
            if ((self.player_1 == self.player_2) and (self.player_1 == length) and (self.player_2 == length)):
                print("Draw!")
                break
            if self.player_1 == length:
                print("Player 1 wins!")
                break
            if self.player_2 == length:
                print("Plater 2 Wins!")
                break
