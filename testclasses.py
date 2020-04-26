# class Character:
# 	def __init__(self, health, name):
# 		self.health = health
# 		self.name = name
# 		self.inventory = []

# 	def __str__(self):
# 		s = "health:" + str(self.health) + "  name:" + str(self.name) + "  inventory:" + str(self.inventory)
# 		return s

# 	def add_inventory(self, item):
# 		self.inventory.append(item)
		
# 	def show_health(self):
# 		return self.health


# def test():
# 	me = Character(100, "Aryaman")
# 	print (str(me))
# 	me.add_inventory("football")
# 	me.add_inventory("studds")
# 	print (str(me))
# 	print (me.show_health())

# test()

# hello = "test"

# def test():
# 	global sing
# 	sing = "bro"
# 	sing()
# def sing():
# 	global sing
# 	print (sing + "hello")
# test()


# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# import math

# width = 200
# height = 200
# rad = 20
# ball_pos = []
# ball_col = "red"

# def distance(p, q):
# 	return math.sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))

# def click(pos):
# 	global ball_pos
# 	ball = []
# 	ball = list(pos)
# 	ball_pos.append(ball)
	 
		


# def draw(canvas):
# 	for ball in ball_pos:
# 		canvas.draw_circle(ball, rad, 1, "black", ball_col)


# frame = simplegui.create_frame("test", width, height)
# frame.set_canvas_background("white")
# frame.set_mouseclick_handler(click)
# frame.set_draw_handler(draw)

# frame.start()

# import random

# ls=[1,2,3,4,5,6,7]
# print (ls.pop(-1))
# print(ls.pop(-1))
# demo for drawing using tiled images

# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# define globals for cards
# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
# import math

# width = 200
# height = 200
# rad = 20
# ball_pos = []
# ball_col = "red"

# def distance(p, q):
# 	return math.sqrt(((p[0]-q[0])**2)+((p[1]-q[1])**2))

# def click(pos):
# 	global ball_pos
# 	ball = []
# 	ball = list(pos)
# 	ball_pos.append(ball)
	 
		


# def draw(canvas):
# 	for ball in ball_pos:
# 		canvas.draw_circle(ball, rad, 1, "black", ball_col)


# frame = simplegui.create_frame("test", width, height)
# frame.set_canvas_background("white")
# frame.set_mouseclick_handler(click)
# frame.set_draw_handler(draw)

# frame.start()

# import random

# ls=[1,2,3,4,5,6,7]
# print (ls.pop(-1))
# print(ls.pop(-1))
# demo for drawing using tiled images

# import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# # define globals for cards
# RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
# SUITS = ('C', 'S', 'H', 'D')

# # card sprite - 950x392
# CARD_CENTER = (36.5, 49)
# CARD_SIZE = (73, 98)
# card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")



# define card class
# class Card:
#     def __init__(self, suit, rank):
#         self.rank = rank
#         self.suit = suit

#     def draw(self, canvas, loc):
#         i = RANKS.index(self.rank)
#         j = SUITS.index(self.suit)
#         card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
#                     CARD_CENTER[1] + j * CARD_SIZE[1]]
#         canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# # define draw handler        
# def draw(canvas):
#     one_card.draw(canvas, (155, 90))

# # define frame and register draw handler
# frame = simplegui.create_frame("Card draw", 300, 200)
# frame.set_draw_handler(draw)

# # createa card
# one_card = Card('S', '6')

# frame.start()




# define card class
# class Card:
#     def __init__(self, suit, rank):
#         self.rank = rank
#         self.suit = suit

#     def draw(self, canvas, loc):
#         i = RANKS.index(self.rank)
#         j = SUITS.index(self.suit)
#         card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
#                     CARD_CENTER[1] + j * CARD_SIZE[1]]
#         canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# # define draw handler        
# def draw(canvas):
#     one_card.draw(canvas, (155, 90))

# # define frame and register draw handler
# frame = simplegui.create_frame("Card draw", 300, 200)
# frame.set_draw_handler(draw)

# # createa card
# one_card = Card('S', '6')

# frame.start()

# def solution(nums, target):
#     sol_list = list(nums)
#         for element in nums:
#             sol_list.remove(element)
#             for piece in sol_list:
#                 if element + piece == target:
#             	    x = nums.index(element)
#             	    nums.remove(element)
#             	    y = nums.index(piece) + 1
#             	    return (x, y)	

        
# print (solution([-1,3,6], 5))

# def solution(nums, target):
# 	copy = list(nums)
# 	for num in nums:
# 		copy.remove(num)
	
# 		try:
# 			return (nums.index(num), copy.index(target - num) + 1)
			
# 		except:
# 			copy = list(nums)

		

# print(solution([3,3,6], 6))

# h = [1,2,3,4,5]

# if h.index(5) == True:
# 	print('h')
# def solution(nums, target):
# 	copy = list(nums)
# 	for num in list(nums):
# 		nums.remove(num)

# 		if (target - num) in nums
		
	
# 		try:
# 			return (nums.index(num), copy.index(target - num) + 1)
			
# 		except:
# 			copy = list(nums)

		

# print(solution([3,3,6], 6))

j = [1,2,3,4,5]

for i in list(j):
	list(j).remove(i)
print (list(j))	
print(j)

