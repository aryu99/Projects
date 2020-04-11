import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random 
import math

width = 1092
height = 130
width_card = width/14
deck = [1,2,3,4,5,6,7,1,2,3,4,5,6,7]
card_lines = []
card_no = 0 # so that draw handler knows which card number to draw
draw_flag = 0 # so that first card gets drawn only after first click
card_compare = [0, 0] #for comparing two consecutive card clicks
correct_cards = []
correct_cards_pos = []
card_no_ls = []
flag = 0 #for mouseclicks

def reset():
	global flag, card_no, draw_flag, card_compare, correct_cards, correct_cards_pos, card_no_ls
	flag = 0
	card_lines = []
	card_no = 0 # so that draw handler knows which card number to draw
	draw_flag = 0 # so that first card gets drawn only after first click
	card_compare = [0, 0] #for comparing two consecutive card clicks
	correct_cards = []
	correct_cards_pos = []
	card_no_ls = []
	random.shuffle(deck)
	


def shuffle():
	global deck, card_lines
	random.shuffle(deck)
	lines = range(13)
	
	#drawing the lines
	for n in lines:
		x = int(78 + width_card*n)
		card_lines.append(x)
	

def click(pos):
	print ('x cord pos of lines', card_lines)
	global flag, card_compare, correct_cards, correct_cards_pos, card_no, draw_flag
	card = list(pos)
	card_no = 0
	draw_flag = 1

	#click flags
	if flag == 0:
		flag = 1
	elif flag == 1:
	 	flag = 0
	
	#numbering the cards
	for n in card_lines:
		if card[0]>n : 
			card_no += 1
		elif card[0]<n :
			pass
	print ('card no', card_no)
	print ('flag', flag)
	card_no_ls.append(card_no)

	
	#assigning card values to list and setting up for comparing
	if flag == 1:
		card_compare[0] = deck[card_no]
		
	elif flag == 0:
		card_compare[1]	= deck[card_no]
		

	print ('comparing', card_compare)

	#comparing after two clicks
	if flag == 0:
		if card_compare[0] == card_compare[1]:
			correct_cards.extend(card_compare)
			correct_cards_pos.append(card_no_ls.pop(-1))
			correct_cards_pos.append(card_no_ls.pop(-1))
		
		# elif card_compare[0] != card_compare[1]:
		# 	rem = [-1, -1]
		# 	for x in rem:
		# 		correct_cards_pos.pop(x)

	print ('correct cards list:',correct_cards)			
	print ('pos of corect cards:', correct_cards_pos)





def draw(canvas):
	lines = range(13)
	z = 0
	for n in lines:
		z = 78 + width_card*n 
		canvas.draw_line((z, 0), (z, height), 3, 'white')

	

	if draw_flag == 1:	
		num_pos = 28 + (width_card*card_no)	
		canvas.draw_text(str(deck[card_no]), (num_pos, height/2), 40, 'red')

	x = 0
	for cards_vals in correct_cards:
		if len(correct_cards_pos)>1:
			num_pos = 28 + (width_card*correct_cards_pos[x])
		 	
			canvas.draw_text(str(cards_vals), (num_pos, height/2), 40, 'red')
			x += 1
		






frame = simplegui.create_frame("Memory Game", width, height)
frame.set_draw_handler(draw)
frame.add_button("Reset", reset)
frame.set_mouseclick_handler(click)

shuffle()
frame.start()
