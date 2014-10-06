def loop_it(top, increment):
	i = 0
	numbers = []

	while i < top:
		print "At the top, i is %f" % i
		numbers.append(i)
	
		i += increment
		print "Numbers now: ", numbers
		print "At the bottom, i is %f" % i
	
	print "\nDone! The numbers:" ,

	for num in numbers:
		print num,
		# remember, that comma after num keeps it from making a new line

print "Max of while loop:",
max = float(raw_input())
# the above two lines make it so that you enter it on the same line as the print statement

print "Increment:",
incr = float(raw_input())
print 
if incr > 0:
	loop_it(max, incr)
else:
	print "You dummy, you'll break the loop! The increment must be greater than 0."