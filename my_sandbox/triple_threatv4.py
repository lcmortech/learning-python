# Import modules
import random
import copy
import time

# Function to start the game
def start_game():
    global starting_deck
    global card_deck

    # Initialize the deck with card values
    starting_deck = {
        'A of Hearts': 1, 'A of Diamonds': 1, 'A of Clubs': 1, 'A of Spades': 1,
        '2 of Hearts': 2, '2 of Diamonds': 2, '2 of Clubs': 2, '2 of Spades': 2,
        '3 of Hearts': 3, '3 of Diamonds': 3, '3 of Clubs': 3, '3 of Spades': 3,
        '4 of Hearts': 4, '4 of Diamonds': 4, '4 of Clubs': 4, '4 of Spades': 4,
        '5 of Hearts': 5, '5 of Diamonds': 5, '5 of Clubs': 5, '5 of Spades': 5,
        '6 of Hearts': 6, '6 of Diamonds': 6, '6 of Clubs': 6, '6 of Spades': 6,
        '7 of Hearts': 7, '7 of Diamonds': 7, '7 of Clubs': 7, '7 of Spades': 7,
        '8 of Hearts': 8, '8 of Diamonds': 8, '8 of Clubs': 8, '8 of Spades': 8,
        '9 of Hearts': 9, '9 of Diamonds': 9, '9 of Clubs': 9, '9 of Spades': 9,
        '10 of Hearts': 10, '10 of Diamonds': 10, '10 of Clubs': 10, '10 of Spades': 10,
        'Jack of Hearts': 3, 'Jack of Diamonds': 3, 'Jack of Clubs': 3, 'Jack of Spades': 3,
        'Queen of Hearts': 3, 'Queen of Diamonds': 3, 'Queen of Clubs': 3, 'Queen of Spades': 3,
        'King of Hearts': 3, 'King of Diamonds': 3, 'King of Clubs': 3, 'King of Spades': 3,
        'Joker A': 10, 'Joker B': 10
    }

    # Copying the starting deck into card_deck
    card_deck = copy.deepcopy(starting_deck)
    
    print('Hello there! Welcome to Triple Threat! Would you like to play a round?')
    play_game = input('Enter Y/y to play, and N/n to exit:\n').upper()

    if play_game == "Y":
        play_turn()
    elif play_game == "N":
        print("Game Over")
        return

    # Keep playing while deck is not empty
    while len(card_deck) > 2:
        cont_game = input('Nice round! Care to try again? Y/N \n').upper()

        if cont_game == "Y":
            play_turn()
        elif cont_game == "N":
            print("Game Over")
            return

# Function to play a turn
def play_turn():
    global card_deck

    if len(card_deck) < 3:
        print("Not enough cards left to continue the game!")
        return

    hand = list(card_deck.keys())  # Refresh hand from the updated deck
    my_turn = random.sample(hand, 3)
    comp_turn = random.sample(hand, 3)

    # Player and computer round scores
    my_hand = 0
    comp_hand = 0

    print(f"\nCards remaining in deck: {len(card_deck)}")
    print("\nIt's your turn!")
    print(my_turn)
    
    for card in my_turn:
        print(f"You drew {card}: {card_deck[card]} points")
        my_hand += card_deck[card]
        del card_deck[card]  # Remove card from deck

    print("\nIt's the computer's turn!")
    time.sleep(1)
    print(comp_turn)

    for card in comp_turn:
        print(f"Computer drew {card}: {card_deck[card]} points")
        comp_hand += card_deck[card]
        del card_deck[card]  # Remove card from deck

    print(f"\nYour total this round: {my_hand}")
    print(f"Computer's total this round: {comp_hand}")

# Start the game
start_game()
