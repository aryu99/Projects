import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def tick():
	print ("Tick!")


timer = simplegui.create_timer(1000, tick)

timer.start()	
timer.stop()
