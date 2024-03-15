from playersettings import Player
import os
import time
import random

class Board():
    def __init__(self):
        self.cards = []
        self.player = Player()
        
    def select_players(self):
            self.player_count = input('Select the number of players (Max 2): ')
            if self.player_count == '1' or self.player_count == '2':
                return self.player.players()
            else:
                print(f"Error, input {self.player_count} not valid")
        
    def get_cards(self):
        if len(self.cards) == 0:
            self.cards = random.sample(self.player.card_combinations(),3) 
        else:
            self.cards.append(random.choice(self.player.card_combinations()))  
        
    def show_hands(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.player_count  == '1':
            print(f'Your Cards: {self.player_hands[0]} points: {self.player.point_p1}')
        else:
            choice = input('select the hand you want to see (p1, p2): ')
            if choice == 'p1':
                print(f'P1 Cards: {self.player_hands[0]}, points: {self.player.point_p1}')
            elif choice == 'p2':
                print(f'P2 Cards: {self.player_hands[0]}, points: {self.player.point_p2}')
            else:
                return
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            
    def pontuation(self):
        for card in self.player_hands[0]:
            if card.islower() and card in self.cards:
                self.player.point_p1 += 1
            elif card.isupper() and card in self.cards:
                self.player.point_p1 += 2
        for card in self.player_hands[1]:
            if card.islower() and card in self.cards:
                self.player.point_p2 += 1
            elif card.isupper() and card in self.cards:
                self.player.point_p2 += 2
    
    def game_result(self):
        print(f'cards on Desk: {self.cards}')
        if self.player_count == '2':
            if self.player.point_p1 > self.player.point_p2:
                print(f'Player 1 wins!!\n Player 1 cards: {self.player_hands[0]} Points: {self.player.point_p1} Points.\nPlayer 2 cards: {self.player_hands[1]} points: {self.player.point_p2}')
            elif self.player.point_p1 < self.player.point_p2:
                print(f'Player 2 wins!!\nPlayer 2 cards: {self.player_hands[1]} Points: {self.player.point_p2} Points.\nPlayer 1 cards: {self.player_hands[0]} Points: {self.player.point_p1}')
            else:
                print(f'Its a Tie!!\nPlayer 1 cards: {self.player_hands[0]} Points: {self.player.point_p1}\nPlayer 2 cards: {self.player_hands[1]} Points: {self.player.point_p2}')
        elif self.player_count == '1':
            print(f'Player 1 cards: {self.player_hands[0]} Points: {self.player.point_p1}\nOpponent cards: {self.player_hands[1]} Points: {self.player.point_p2}')
            
    def main_loop(self):
        self.player_hands = self.select_players()
        while len(self.cards) < 6:
            print(f'cards on Desk: {self.cards}, Cards remaining: "TODO"')
            self.commands = input("Command[(show)|(next)|(quit)]: ").lower()
            if self.commands == 'show':
                self.show_hands()
            if self.commands == 'next' and len(self.cards) < 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.get_cards()
                self.pontuation()
            elif len(self.cards) == 5 and self.commands == 'next':
                break
            if self.commands == 'quit':
                break
        if self.commands != 'quit':
            self.game_result()
            
        