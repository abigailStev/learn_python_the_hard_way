my_name = "Abigail Stevens" # can use double or single quotes to assign a string
my_age = 24
my_height = 68 #inches
my_weight = 150 #lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name # includes a string
print "She's %d inches tall." % my_height # includes a float/double
print "She's %d pounds heavy." % my_weight # includes a float/double
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair) # the extra parentheses are important!!
print "Her teeth are usually %s." % my_teeth

# Super important to include these in order.
print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print