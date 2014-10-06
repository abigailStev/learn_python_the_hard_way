varia = 6.5
print varia
del varia
#print varia # get an error saying "name 'varia' is not defined"

global a # now 'a' will be defined for the entirety of this program
a = 8  # can't assign something to a global variable in the instantiation line

# with <object> as <variable>

for i in range(1,5,2):
	pass # does nothing, but sometimes syntactically required
	
temp1 = 3
temp2 = 5
if temp1 > temp2:
	pass
else:
	print "Here"
# probably easier in this instance to just flip the if statement and not use 'pass'

# 'yield' is used to return generators the way 'return' returns lists
# generators have (), lists have []