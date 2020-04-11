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

import random

ls=[1,2,3,4,5,6,7]
print (ls.pop(-1))
print(ls.pop(-1))
