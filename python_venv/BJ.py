import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10',
        'Jack', 'Queen', 'King', 'Ace'
    ]
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card['rank'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['rank'] == 'Ace':
            aces += 1
            value += 11
        else:
            value += int(card['rank'])
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, name):
    print(f"{name}'s hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand(player_hand, "Player")
    display_hand([dealer_hand[0]], "Dealer")

    while calculate_hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            display_hand(player_hand, "Player")
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    while dealer_value < 17:
        dealer_hand.append(deck.pop())
        dealer_value = calculate_hand_value(dealer_hand)

    display_hand(dealer_hand, "Dealer")

    if player_value > 21:
        print("You bust! Dealer wins.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

play_blackjack()