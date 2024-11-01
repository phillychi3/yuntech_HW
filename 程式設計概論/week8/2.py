import random

class CardDeck:
    def __init__(self):
        self.deck = [f"{suit}{rank}" for suit in '♠♥♦♣' for rank in range(1, 14)]

    def print_original_deck(self):
        print(f"Original deck (in order):\n{self.deck}")

    def fisher_yates_shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

        print(f"Shuffled deck:\n{self.deck}")

    def deal_cards(self, num_players, cards_per_player):
        hands = [[] for _ in range(num_players)]
        for _ in range(cards_per_player):
            for i in range(num_players):
                if self.deck:
                    hands[i].append(self.deck.pop(0))
        return hands

deck = CardDeck()
deck.print_original_deck()

deck.fisher_yates_shuffle()

hands = deck.deal_cards(num_players=4, cards_per_player=13)
for i, hand in enumerate(hands, start=1):
    print(f"Player {i}'s hand: {hand}")