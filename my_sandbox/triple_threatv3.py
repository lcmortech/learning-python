#NOTES




# =========

# Import modules
import random
import copy
import time

#Variables

starting_deck = {}
    

#COPYING STARTING DECK BY VALUE TO EMPTY CARD DECK
#card_deck = {}
card_deck = copy.deepcopy(starting_deck)

#Getting the keys of the deck as an array for each hand played
hand = card_deck.keys()

#Initializing empty deck for player
my_deck = {}
#Initializing empty deck for computer
comp_deck = {}
my_turn = random.sample(list(hand), 3)
comp_turn = random.sample(list(hand), 3)

#counters for keeping score
my_score = 0 
comp_score = 0

#sum of hand per turn for each player
my_hand = 0
comp_hand = 0


#--------------------------

def start_game():
    global starting_deck
    global card_deck

    starting_deck = {
		'A of Hearts': 1,
		'A of Diamonds': 1,
		'A of Clubs': 1,
		'A of Spades': 1,
		'2 of Hearts': 2,
		'2 of Diamonds': 2,
		'2 of Clubs': 2,
		'2 of Spades': 2,
		'3 of Hearts': 3,
		'3 of Diamonds': 3,
		'3 of Clubs': 3,
		'3 of Spades': 3,
		'4 of Hearts': 4,
		'4 of Diamonds': 4,
		'4 of Clubs': 4,
		'4 of Spades': 4,
		'5 of Hearts': 5,
		'5 of Diamonds': 5,
		'5 of Clubs': 5,
		'5 of Spades': 5,
		'6 of Hearts': 6,
		'6 of Diamonds': 6,
		'6 of Clubs': 6,
		'6 of Spades': 6,
		'7 of Hearts': 7,
		'7 of Diamonds': 7,
		'7 of Clubs': 7,
		'7 of Spades': 7,
		'8 of Hearts': 8,
		'8 of Diamonds': 8,
		'8 of Clubs': 8,
		'8 of Spades': 8,
		'9 of Hearts': 9,
		'9 of Diamonds': 9,
		'9 of Clubs': 9,
		'9 of Spades': 9,
		'10 of Hearts': 10,
		'10 of Diamonds': 10,
		'10 of Clubs': 10,
		'10 of Spades': 10,
		'Jack of Hearts': 3,
		'Jack of Diamonds': 3,
		'Jack of Clubs': 3,
		'Jack of Spades': 3,
		'Queen of Hearts': 3,
		'Queen of Diamonds': 3,
		'Queen of Clubs': 3,
		'Queen of Spades': 3,
		'King of Hearts': 3,
		'King of Diamonds': 3,
		'King of Clubs': 3,
		'King of Spades': 3,
		'Joker A': 10,
		'Joker B': 10
	}

    # Main Greeting 
    print('Hello there! Welcome to Triple Threat! Would you like to play a round?')
	#print('')
	#create_deck()
    
    play_game = input('Enter Y/y to play, and N/n to get out of here!\n')
    play_game = play_game.upper()

	#If player selects yes vs. no	
    if play_game == "Y":
        play_turn()
        
    elif play_game == "N":
        print("Game Over")
        return None
	
	# While the deck isn't empty:
    while len(card_deck) > 1:		
		
        cont_game = input('Nice round! Care to try again? Y/N \n')
        cont_game = cont_game.upper()	
		
		
		# Continue to next round:	
        if cont_game == "Y":
            play_turn()
        elif cont_game == "N":
            print("Game Over")
            return None

#--------------------------
def play_turn():
	global hand
	global my_score
	global comp_score
	global my_hand
	global comp_hand
	global starting_deck
	global card_deck

	#picking out 3 cards at random from the keys in hand variable
	my_turn = random.sample(list(hand), 3)
	comp_turn = random.sample(list(hand), 3)

	#display remaining cards in card deck
	print(card_deck)
	
	print(f"Cards remaining in deck: {len(card_deck)}")