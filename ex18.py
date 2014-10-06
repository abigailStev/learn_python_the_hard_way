# functions!
def print_two(*args):
	arg1, arg2 = args # need to unpack args before we can use them separately, but useful if you don't know how many args you'll get
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# *args is like argv but for functions instead of the command line

def print_two_again(arg1, arg2): # good for a small, defined number of args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg1):
	print "arg1: %r" % arg1
	
def print_none():
	print "I got nothin'."


print_two("Abigail","Stevens")
print_two_again("Abbie","Stev")
print_one("First!")
print_none()