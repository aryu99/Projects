import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

time = 10
width = 750
height = 500
init_position  = [width/2, height/2]
vel = [0,0]
rad = 20




def draw(canvas):
	global init_position
	init_position[0] += vel[0]
	init_position[1] += vel[1]

	if init_position[0] <= rad:
		vel[0] = -vel[0]
	if init_position[0] >= width - rad:
		vel[0] = -vel[0]

	canvas.draw_circle(init_position, rad, 12, "red" )

def keydown(key):
	acc = 1
	global vel
	if key == simplegui.KEY_MAP["left"]:
		vel[0] -= acc
	elif key == simplegui.KEY_MAP["right"]:
		vel[0] += acc
	elif key == simplegui.KEY_MAP["up"]:
		vel[1] -= acc
	elif key == simplegui.KEY_MAP["down"]:
		vel[1] += acc







frame = simplegui.create_frame("test pong", width, height)
frame.set_keydown_handler(keydown)

frame.set_draw_handler(draw)

frame.start()
