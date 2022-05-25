def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(f'{suit} of {rank}')

    return deck

'''my_deck = create_deck()
print(my_deck)'''