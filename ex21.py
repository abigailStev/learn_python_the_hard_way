def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a+b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a-b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a*b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a/b
	
print "Math time!" 

age = add(20,4)
height = subtract(70,2)
weight = multiply(80,2)
iq = divide(100,2)

print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: %d" % what
print "That becomes:", what, "Can you do it by hand?"
# you can use a function's return as an argument to another function!