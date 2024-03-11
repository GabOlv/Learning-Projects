from board import BoardPath

# Main class
class Menu():
    # Start the board Istance and initialize the first method
    def __init__(self, players):
        self.players = players 
        self.board = BoardPath()
        self.start()

    # Start the board Istance and initialize the first method
    def start(self):
        if self.players >= 1 and self.players <= 2: # player vs another players
            self.board.start(self.board.map_length(), self.players)
        else: # Error
            pass
# handles the number of players, 1 = player vs CPU, 2 = two players        
def player_number():
    try:
        players = int(input("Select the number of players(max 2): "))
    except Exception as e:
        print(f'Error: {e}')
    return players
# Starts all the program
if __name__ == '__main__':
    players = player_number()
    start = Menu(players)