def name(card):
    '''Takes the initials of a card and returns its name'''
    suit = card[1]
    value = card[0]
    if value == "A":
        value = "Ace"
    elif value == "K":
        value = "King"
    elif value == "Q":
        value = "Qeen"
    elif value == "J":
        value = "Jack"

    if suit == "H":
        suit = "Hearts"
    elif suit == "D":
        suit = "Diamonds"
    elif suit == "C":
        suit = "Clubs"
    elif suit == "S":
        suit = "Spades"



    return(f"{value} of {suit}")