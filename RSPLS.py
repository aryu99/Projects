import random
import math

 

"""rock = 0
spock = 1
paper = 2
lizard = 3
scissors = 4"""

#defining function for computing game


def faceoff(human):
	#generating choices made by computer

	comp = random.randrange(0,5)
	print ("val_comp", comp)
	print ("val_human", human)
	result = human - comp
	print ("computed_val", result)


	if result == (1 or 2 or -3 or -4):
		print("human wins")
	else:
		print("human lost")





faceoff(0)
faceoff(1)
faceoff(2)
faceoff(3)
faceoff(4)


