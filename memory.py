import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

deck = [1,2,3,4,5,6,7,1,2,3,4,5,6,7]
width = 1092
height = 130
width_card = width/14
card_lines = []
mouseclick = []
card = 0 #card number
flag = 0
click_flag = 0
check = [0,0] #values of card
correct_ls = []
check_pos=[0,0]
correct_num_pos = [] #positions of correct number pos

def play_deck():
	global deck
	random.shuffle(deck)
	
	

def choose(pos):
	global mouseclick, click_flag
	mouseclick = list(pos)
	lines()
	

def lines():
	global flag
	lines = range(13)
	x = 0
	if flag == 0:
		for n in lines:
			x = int(78 + width_card*n)
			card_lines.append(x)
		flag = 1
	compare()



def compare():
	global card, click_flag, check, correct_ls, check_pos, correct_num_pos
	card_no = 0
	for a in card_lines:
		if mouseclick[0]>a:
			card_no += 1
	card = card_no
	if click_flag == 0:
		check[0] = deck[card]
		check_pos[0] = card
		click_flag = 1

	elif click_flag == 1:
		check[1] = deck[card]
		check_pos[1] = card
		click_flag = 0

	print (check)
	if click_flag == 0:	

		if check[0] == check[1]:
			correct_ls.extend(check)
			correct_num_pos.extend(check_pos)
			check[0] = 0
			check[1] = 0

		elif check[0] != check[1]:
			check[0] = 0
			check[1] = 0

	print ("check list is : ",check)
	print ("correct list is:", correct_ls)
	print ("correct list positions:", correct_num_pos)



	
	
	
	
	
	





def draw(canvas):
	lines = range(13)
	z = 0
	for n in lines:
		z = 78 + width_card*n 
		canvas.draw_line((z, 0), (z, height), 3, 'white')
	

	if flag == 1:
		num_pos = 28 + (width_card*card)	
		canvas.draw_text(str(deck[card]), (num_pos, height/2), 40, 'red')
		# for cards in correct_ls:
		# 	num_pos = 28 + (width_card*cards)	
		# 	canvas.draw_text(str(deck[cards]), (num_pos, height/2), 40, 'red')





frame = simplegui.create_frame("Memory Game", width, height)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(choose)


play_deck()
frame.start()
