import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random


CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")


CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")  

in_play = False
outcome = ""
score = 0
game_number = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

#initializing classes for objects


class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def get_suit(self):
		return self.suit

	def get_rank(self):
		return self.rank

	def draw(self, canvas, pos):
		card_loc = (CARD_CENTER[0] + CARD_SIZE[0]*RANKS.index(self.rank),
					CARD_CENTER[1] + CARD_SIZE[1]*SUITS.index(self.suit) )
		canvas.draw_image(card_images, card_loc, CARD_SIZE, (CARD_CENTER[0] + pos[0], CARD_CENTER[1] + pos[1]), CARD_SIZE)

class Hand:

    def __init__(self):
        self.hand_card = []

    def __str__(self):
        
        hand = "Hand contains:" 
        for i in range(len(self.hand_card)):
            hand += str(self.hand_card[i])

        return hand

    
    def add_card(self, card):
        self.hand_card.append(card)

    def get_value(self):
    	value = 0
    	aces = False

    	for cards in self.hand_card:
    		value += VALUES[cards.get_rank()]
    		if (cards.get_rank() == 'A'):
    			aces = True

    	if not aces:
    		return value
    	else:
    		if value + 10 <= 21:
    			return value + 10
    		else:
    			return value

    def draw(self, canvas, pos):
        n_card = 0

        for card in self.hand_card:
            if pos[1] == 310 and n_card == 0 and in_play == True:
                # draw card back
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                                  [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                                  CARD_BACK_SIZE)
            else:
                # draw face card
                card.draw(canvas, [pos[0] + (n_card % 7) * 77, pos[1] + (n_card // 7) * 102])
            n_card += 1

	

class Deck:
    def __init__(self):
        self.deck = []

        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))



    def shuffle(self):
    	random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop(0)	# deal a card object from the deck
    
    def __str__(self):
    	result = ""
    	for card in self.deck:
        	result += " " + str(card)

    	return "Deck contains" + result
        	# return a string representing the deck


def deal():
	global score, in_play, outcome, player_hand, dealer_hand, game_number

	deck.shuffle()
	player_hand.hand_card = []
	dealer_hand.hand_card = []

	game_number += 1

	player_hand.add_card(deck.deal_card())
	player_hand.add_card(deck.deal_card())

	dealer_hand.add_card(deck.deal_card())
	dealer_hand.add_card(deck.deal_card())

	print(player_hand)

	if in_play:
		score -= 1
		outcome = "You lost the round: "
	else:
		outcome = "Do you want to hit or stand?"

	in_play = True

def hit():
	global score, in_play, outcome, player_hand, deck, outcome

	if in_play:
		player_hand.add_card(deck.deal_card())
		if player_hand.get_value() <= 21:
			outcome = "Hit or Stand?"
		else:
			outcome = "You got busted!"
			score -= 1
			in_play = False


def stand():
	global score, in_play, outcome, player_hand, dealer_hand, deck, outcome

	if in_play:
		in_play = False
		if player_hand.get_value() > 21:
			outcome = "You got busted!"
		else:
			while dealer_hand.get_value() < 17:
				dealer_hand.add_card(deck.deal_card())
			if dealer_hand.get_value() > 21:
				outcome = "Dealer went bust! You won!"
				score += 1
			elif player_hand.get_value() <= dealer_hand.get_value():
				outcome = "Dealer has higher value of cards than yours! You lost!"
				score -= 1
			else:
			
				outcome = "You won!"
				score += 1	





def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [230, 25], 30, "Red")

    # draw text
    canvas.draw_text("Player", [10, 45], 24, "Black")
    canvas.draw_text("Dealer", [10, 295], 24, "Black")
    canvas.draw_text("Score: " + str(score), [500, 25], 24, "Yellow")
    canvas.draw_text("Game # " + str(game_number), [500, 45], 21, "White")
    canvas.draw_text(outcome, [90, 575], 24, "White")

    # draw cards
    player_hand.draw(canvas, [10, 60])
    dealer_hand.draw(canvas, [10, 310])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

player_hand = Hand()
dealer_hand = Hand()
deck = Deck()
# get things rolling
deal()
frame.start()








