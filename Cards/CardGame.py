from cards import deck, name, hand_score

# Players get dealt a number of cards, the cards are determined by the user
# Whoever has the highest hand wins

# Game gets a deck of cards
# Players get dealt some cards

cards = deck()

player1 = []
player2 = []

for i in range(1, 6):
    player1 += [cards.pop()]
    player2 += [cards.pop()]

player1score = hand_score(player1)
player2score = hand_score(player2)


print(f"Player 1's hand is {list(map(name, player1))} and their score is {player1score} ")
print(f"Player 2's hand is {list(map(name, player2))} and their score is {player2score}")


if player1score > player2score:
    print("Player 1 won")
elif player2score > player1score:
    print("Player 2 won")
else:
    print("It's a draw")
