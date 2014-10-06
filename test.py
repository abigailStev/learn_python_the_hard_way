def is_int(num):
	try: 
		b = int(num)
		return True
	except ValueError:
		return False

def is_float(num):
	try:
		b = float(num)
		return True
	except ValueError:
		return False

a = raw_input("Enter a number: ")


if is_int(a):
	print "It's an integer!"
elif is_float(a):
	print "It's a float!"
else:
	print "Not a real number."