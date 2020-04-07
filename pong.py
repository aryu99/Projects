import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

time = 10
width = 750
height = 500
init_position  = [width/2, height/2]
vel = [0,0]
vel_ball = [0,0]
rad = 14
score1 = 0
score2 = 0
width_gut1 = 40
width_gut2 = 710 
pad_height = 40
mov1 = 0
mov2 = 0
timer_val = 100
flag = 0
acc = 6





def ball_move():
	global init_position
	global flag
	global vel_ball
	if flag == 0:
		vel_ball[0] = random.randrange(-3, 3) 
		vel_ball[1] = random.randrange(-2, 2) 
		if vel_ball[0] == 0:
			vel_ball[0] = random.randrange(-3, 3)
		if vel_ball[1] == 0:
			vel_ball[1] = random.randrange(-2, 2)
		init_position[0] = width/2
		init_position[1] = height/2 

		flag = 1

	init_position[0] += vel_ball[0]
	init_position[1] += vel_ball[1]
	reflection()	
	
	#reflection
def reflection():
	global vel_ball
	global flag
	global score1
	global score2

	if init_position[0] <= rad + width_gut1:#left wall
		if ((height/2)-pad_height+mov1) < init_position[1] < ((height/2)+pad_height+mov1):
			vel_ball[0] = -(vel_ball[0] - 3)
		else:
			init_position[0] = width/2
			init_position[1] = height/2
			flag = 0
			score2 += 1
			ball_move()
			
			
	if init_position[0] >= width_gut2 - rad:#right wall
		if ((height/2)-pad_height+mov2) < init_position[1] < ((height/2)+pad_height+mov2):
			vel_ball[0] = -(vel_ball[0] + 3)
		else:
			init_position[0] = width/2
			init_position[1] = height/2
			flag = 0
			score1 += 1
			ball_move()
			
			
	
	if init_position[1] <= rad:#up wall
		vel_ball[1] = -vel_ball[1]
	
	if init_position[1] >= height-rad:#down wall
		vel_ball[1] = -vel_ball[1]


def draw(canvas):
	global mov1
	global mov2
	global vel

	mov1 += vel[0]
	mov2 += vel[1]
	if ((height/2)-pad_height+mov1)<0 :
		mov1 = pad_height - (height/2)
	if ((height/2)+pad_height+mov1)>height:
		mov1 = height - pad_height - (height/2)

	if ((height/2)-pad_height+mov2)<0 :
		mov2 = pad_height - (height/2)
	if ((height/2)+pad_height+mov2)>height:
		mov2 = height - pad_height - (height/2)
	
	
	
	
	
	
	ball_move()
	

	
	#drawing divider
	canvas.draw_line((width/2, 0), (width/2, height), 2, 'white')

	#drawing ball	
	canvas.draw_circle(init_position, rad, 5, "orange", "orange" )
	
	#drawing gutters
	canvas.draw_line((width_gut1, 0), (width_gut1, height), 2, 'white')
	canvas.draw_line((width_gut2, 0), (width_gut2, height), 2, 'white')
	
	#drawing scores
	canvas.draw_text(str(score1), (350, 50), 30, "white")
	canvas.draw_text(str(score2), (387, 50), 30, "white")
	
	#making paddles
	#right
	canvas.draw_polygon([(width, (height/2)-pad_height+mov2), (width_gut2, (height/2)-pad_height+mov2 ), 
		(width_gut2, (height/2)+pad_height+mov2), (width, (height/2)+pad_height+mov2)], 12, 'blue', 'blue')
	#left
	canvas.draw_polygon([(0, (height/2)-pad_height+mov1), (width_gut1, (height/2)-pad_height+mov1 ), 
		(width_gut1, (height/2)+pad_height+mov1), (0, (height/2)+pad_height+mov1)], 12, 'red', 'red')
	

#def accel():
#	keydown()

def keydown(key):
		
		global vel
		if key == simplegui.KEY_MAP["w"]:
			vel[0] -= acc
		elif key == simplegui.KEY_MAP["s"]:
			vel[0] += acc
		elif key == simplegui.KEY_MAP["up"]:
			vel[1] -= acc
		elif key == simplegui.KEY_MAP["down"]:
			vel[1] += acc


def keyup(key):
		
		global vel
		if key == simplegui.KEY_MAP["w"]:
			vel[0] -= (-acc)
		elif key == simplegui.KEY_MAP["s"]:
			vel[0] += (-acc)
		elif key == simplegui.KEY_MAP["up"]:
			vel[1] -= (-acc)
		elif key == simplegui.KEY_MAP["down"]:
			vel[1] += (-acc)

def reset():

	global score1
	global score2
	global flag
	score1 = 0
	score2 = 0
	flag = 0



frame = simplegui.create_frame("test pong", width, height)
frame.add_button("Reset", reset)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.set_draw_handler(draw)

frame.start()
