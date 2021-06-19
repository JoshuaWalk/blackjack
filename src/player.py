class Player:
    '''
    description:
        holds cards, tracks hand total 
    attributes:
        name
        hand - list of cards
        total - total value of cards
        is_busted - determines if player has busted
        
    '''
    def __init__(self, name, wager):
        self.name = name
        self.hand = []
        self.total = 0
        self.is_busted = False
        self.wager = wager
        self.reward = 0
        
    def restart(self):
        self.hand = []
        self.total = 0
        self.is_busted = False


class BlackjackDealer(Player):
    '''
    description:
        same as player, currently holds dealer show hand logic
    attributes:
        
    
    methods:
        showHand - calls show method on every card in hand
    '''
    def __init__(self, game):
        Player.__init__(self, 'Dealer', None)
        self.hide_card = True
        self.game = game


    def turn(self):
        self.game.hit(self)


    def soft_hand(self):
        for card in self.hand:
            if card.value == 'Ace' and card.is_used == False and self.total <= 17:
                self.game.hit(self)

    def show_one_card(self):
        ''' displays 1 of dealers cards '''
        print(f"========= {self.name}'s Hand ========")
        print('==================================')
        print(f'{self.hand[0].value} of {self.hand[0].suit}')
        print('Hidden Card')
        print('==================================')




    def restart(self):
        self.hand = []
        self.total = 0
        self.is_busted = False
        self.hide_card = True