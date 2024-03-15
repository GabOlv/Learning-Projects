import random

class Player():
    def __init__(self):
        self.point_p1, self.point_p2 = 0, 0

    def card_combinations(self):
        return ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc', 'AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
        
    def players(self):
        player_1_cards = random.sample(self.card_combinations(), 2)
        player_2_cards = random.sample(self.card_combinations(), 2)
        return player_1_cards, player_2_cards