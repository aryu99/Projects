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

hello = "test"

def test():
	global sing
	sing = "bro"
	sing()
def sing():
	global sing
	print (sing + "hello")
test()

