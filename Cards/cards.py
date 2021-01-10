def name(card):
    '''Takes the initials of a card and returns its name'''
    suit = card[1]
    value = card[0]
    if value == "A":
        value = "Ace"
    elif value == "K":
        value = "King"
    elif value == "Q":
        value = "Queen"
    elif value == "J":
        value = "Jack"
    elif value == "0":
        value = "10"

    if suit == "H":
        suit = "Hearts"
    elif suit == "D":
        suit = "Diamonds"
    elif suit == "C":
        suit = "Clubs"
    elif suit == "S":
        suit = "Spades"



    return(f"{value} of {suit}")