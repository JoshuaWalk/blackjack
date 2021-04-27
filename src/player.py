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
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.is_busted = False
        
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
    def __init__(self):
        Player.__init__(self, 'Dealer')
        self.hide_card = True


    def showHand(self):
        print("\nDealer's Hand:")
        if self.hide_card == False:
            print('DEALER TOTAL: ', self.total, '\n')
        for card in self.hand:
            if self.hide_card == True:
                print('hidden card')
                self.hide_card = False
            else:
                card.show()

    def restart(self):
        self.hand = []
        self.total = 0
        self.is_busted = False
        self.hide_card = True