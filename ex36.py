def door_1():
	print "Not finished yet."

def door_2():
	print "There's cake! Do you eat it?"
	next = raw_input(" >> ")
	
	if "y" in next or "Y" in next:
		print "It was delicious! You go home and tweet about it."
		exit(0)
	elif "n" in next or "N" in next:
		print "It turns out you had a gastrointenstinal infestation to which this cake",
		print "held the antidote. You live your mediocre life a few more months",
		print "and then die."
		exit(0)
	else: 
		print "What's wrong with you?"
		exit(0)
	
def door_3():
	print "You found the clowns. Learn to juggle?"
	
	next = raw_input(" >> ")
	
	if "y" in next or "Y" in next:
		print "You have lots of fun!"
		exit(0)
	elif "n" in next or "N" in next:
		print "You hurt the clowns' feelings. They feel sad and dejected."
		exit(0)
	else: 
		print "What's wrong with you?"
		exit(0)

def go_upstairs():
	print "At the top of the stairs are three doors. Which door do you open?"
	next = raw_input(" >> ")
	
	if "1" in next or "one" in next:
		door_1()
	elif "2" in next or "two" in next:
		door_2()
	elif "3" in next or "three" in next:
		door_3()
	else:
 		print "You stumble backwards, fall down the stairs and break your neck."
 		exit(0)

def turn_right():
	print "Not finished yet."

def turn_left():
	print "Not finished yet."

def enter_house():
	print "You enter the house. You can turn down the hall on the left, down the hall",
	print "on the right, or go up the stairs. Which do you choose?"
	next = raw_input(" >> ")
	
	if "left" in next:
		turn_left()
	elif "right" in next:
		turn_right()
	elif "stairs" in next:
		go_upstairs()
	else:
		print "You stumble around, trip on a rusty nail, and die of tetanus. Tough luck."
		exit(0)

def leave_house():
	print "You decided to go home. You're a bit of a scaredy cat, but treat yourself to",
	print "a hot bath and a cup of tea, and get some sleep. Maybe tomorrow."
	exit(0)

def start():
	while True:
		print "\nYou've arrived at the Carnival House. Do you want to enter or leave?"
		next = raw_input(" >> ")
	
		if "enter" in next:
			enter_house()
		elif "leave" in next:
			leave_house()
		else:
			print "That was unintelligible, try again."


start()