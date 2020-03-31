import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

counter = 0

def increment():

	global counter 
	counter = counter + 1

def tick():

	increment()
	print (counter)

def reset():
	global counter
	counter = 0

timer = simplegui.create_timer(1000, tick)
frame = simplegui.create_frame("test", 100, 100)
frame.add_button("click!", reset)

timer.start()
frame.start()