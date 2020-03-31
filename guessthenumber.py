import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import math

range = 0
guess = 0
number = 0 
guesses_left_100 = 7
guesses_left_1000 = 10

def random_no_gen(range):
	global number
	number = random.randrange(0, range)


def button_range_100():
	global range
	range = 100
	random_no_gen(range)
	return number



def button_range_1000():
	global range
	range = 1000
	random_no_gen(range)
	return number


def input(inp):

	global guess
	guess = float(inp)
	compute(guess, number)

def compute(guess, number):
	if guess<number:
		print ("Guess is wrong! The secret number is higher")
		number_of_guesses()
	elif guess>number:
		print ("Guess is wrong! The secret number is lower")
		number_of_guesses()
	else:
		print ("Your guess is correct!")

def number_of_guesses():
	global guesses_left_1000
	global guesses_left_100
	global number
	if range == 100:
		guesses_left_100 = guesses_left_100 - 1
		print ("Number of guesses left:", guesses_left_100)
		if guesses_left_100 == 0:
			print ("You lost! Starting new game")
			print ("Your Number was:", number)
			guesses_left_100 = 7
			random_no_gen(range)
		else:	
			return guesses_left_100
		
	else:
		guesses_left_1000 = guesses_left_1000 - 1
		print ("Number of guesses left:", guesses_left_1000)
		if guesses_left_1000 == 0:
			print ("You lost! Starting new game")
			print ("Your Number was:", number)
			guesses_left_1000 =10
			random_no_gen(range)
		return guesses_left_1000
	





f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range: 0 to 100", button_range_100, 100) 
f.add_button("Range: 0 to 1000", button_range_1000,100)
input = f.add_input("Your guess", input, 100)


f.start()