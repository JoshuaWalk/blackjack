from game import Game
from player import BlackjackDealer

class Blackjack(Game):
    def __init__(self):
        Game.__init__(self)
        self.name = 'Blackjack'
        self.dealer = BlackjackDealer(self)
        self.winner = []
        self.init_deck()

    def deal(self):
        ''' deals 2 cards to every player in the game '''
        for player in self.players:
            self.hit(player)
            self.hit(player)
        self.hit(self.dealer)
        self.hit(self.dealer)

    def hit(self, player):
        ''' pulls card from deck to player hand '''
        card = self.deck.cards.pop()
        self.card_to_hand(player, card)

    def card_to_hand(self, player, card):
        ''' adds a card to players hand'''
        player.hand.append(card)
        self.add_card(player, card)

    def add_card(self, player, card):
        ''' adds value of card to players total '''
        if card.value == 'Ace' and player.total + 11 > 21:
            player.total += 1
            card.is_used = True
        elif card.value == 'Ace' and player.total + 11 <= 21:
            player.total += 11
        elif card.value == 'Jack' or card.value == 'Queen' or card.value == 'King':
            player.total += 10
        else: player.total += card.value
        self.bust_check(player)

    def bust_check(self, player):
        ''' determines if player is busted, calls busted_aces '''
        self.busted_aces(player)
        if player.total > 21:
            player.is_busted = True

    def busted_aces(self, player):
        ''' if player is over 21 and has ace in hand -10 '''
        for card in player.hand:
            if card.value == 'Ace' and card.is_used == False:
                if player.total <= 21: break
                player.total -= 10
                card.is_used = True

    def evaluate_payout_all(self):
        for player in self.players:
            self.evaluate_payout(player)

    def evaluate_payout(self, player):
        if player.is_busted == True: 
            player.reward = 0
        elif player.total > self.dealer.total:
            player.reward = int(player.wager) * 2
        elif self.dealer.is_busted == True and player.is_busted == False:
            player.reward = int(player.wager) * 2
        elif player.total == self.dealer.total:
            player.reward = player.wager

    def reset(self):
        for player in self.players:
            player.hand = []
            player.total = 0
            player.is_busted = False
        self.dealer.hand = []
        self.dealer.total = 0
        self.dealer.is_busted = False

    def reset_wager(self, player, bet):
        player.wager = bet
        
        
            