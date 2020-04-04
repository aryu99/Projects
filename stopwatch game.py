import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

timer_val = 100
mil = 0
sec = 0
minute = 0
final = "0:0.0"
flag = 0
win  = 0
chances = 0
game_print = " Game Score :" + "0/0"



def start():
	global flag
	flag = 1

def stop():
	global flag
	flag = 2
	game()

def reset():
	global flag 
	global win 
	global chances
	flag = 3
	win = 0
	chances = 0
	game()


def increment():
	global mil
	global sec 
	global minute
	global final
	if flag == 1:
		mil = int(mil)
		mil = mil + 1
		stopwatch()
	elif flag == 2:
		format()
	else:
		mil = 0
		sec = 0
		minute = 0

		final = "0:0.0"
		format()

def stopwatch():
	global mil
	global sec 
	global minute
	sec = int(sec)
	minute = int(minute)
	if (mil % 10 == 0):
		mil = 0
		sec = sec + 1
		if (sec % 60 == 0):
			sec = 0
			minute = minute + 1

	format()

	
	

def game():
	global win
	global chances
	global game_print
	global mil
	mil = int(mil)
	if flag == 2:
		chances = chances + 1
		if mil == 0:
			win = win + 1
	game_print = "Game Score :" + str(win) + "/" + str(chances)
	return game_print

			
		
def format():

	global mil
	global sec
	global minute
	global final

	mil = str(mil)
	sec = str(sec)
	minute = str(minute)

	
	final = minute + ":" + sec + "." + mil
	return final
	
	

def draw(canvas):
	canvas.draw_text(final, (250, 250), 50, "green")
	canvas.draw_text(game_print, (350, 50), 20, "red")




frame = simplegui.create_frame("Stopwatch Game", 500, 500)
timer = simplegui.create_timer(timer_val, increment)
frame.set_canvas_background("cyan")
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)


timer.start()
frame.start()
