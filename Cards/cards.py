import random


def name(card):
    """Takes the initials of a card and returns its name
    :param card: a card e.g. "AS"
    :type card: str
    :return: card name e.g. Ace of Spades
    :rtype: str
    """
    suit = card[1]
    val = card[0]
    if val == "A":
        val = "Ace"
    elif val == "K":
        val = "King"
    elif val == "Q":
        val = "Queen"
    elif val == "J":
        val = "Jack"
    elif val == "0":
        val = "10"

    if suit == "H":
        suit = "Hearts"
    elif suit == "D":
        suit = "Diamonds"
    elif suit == "C":
        suit = "Clubs"
    elif suit == "S":
        suit = "Spades"
    return f"{val} of {suit}"


def value(card):
    """Finding the value of a card
    :param card: short hand for a card
    :type card: str
    :return: value
    :rtype: int
    """
    val = card[0]
    if val == "A":
        val = 11
    elif val == "K":
        val = 10
    elif val == "Q":
        val = 10
    elif val == "J":
        val = 10
    elif val == "0":
        val = 10
    else:
        val = int(val)
    return val


def hand_score(cards):
    """Get the score of cards in a hand
    :param cards: an array of cards
    :type cards: list[str]
    :return: score
    :rtype: int
    """
    total = 0
    for card in cards:
        card = value(card)
        total += card
    return total


def deck():
    """Puts all the cards into a random order and gets an array for it
    :return: cards
    :rtype: list[str]
    """
    cards = []
    for suit in ["C", "H", "S", "D"]:
        for val in ["0", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]:
            card = f"{val}{suit}"
            cards += [card]

    random.shuffle(cards)
    return cards


if __name__ == '__main__':
    print(deck())
