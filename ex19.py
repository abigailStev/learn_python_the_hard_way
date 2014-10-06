# defines the function 'cheese_and_crackers', takes 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints stuff
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!\n"

# need to define your function before you call it, obviously

print "We can just give the function numbers directy:"
# printing and hardcoding values to send to the function
cheese_and_crackers(20,30) # calling the function


print "OR, we can use variables from our script:"
# declaring variables and sending those to the function
# these variables are separate and live outside the function
# you want to avoid global variables with the same name as function variables
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # calling the function

print "We can even do math inside too:"
# doing math inside the function call
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
# doing math on the variables inside the function call
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) # calling the function