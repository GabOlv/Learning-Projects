from boardsettings import Board

class Main():
    def __init__(self):
        board = Board()
        board.main_loop()
        

if __name__ == '__main__':
    start = Main()