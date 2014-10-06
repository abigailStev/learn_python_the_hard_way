from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0) # moving to the start of the file, refers to bytes not lines
	
def print_a_line(line_count, f):
	print line_count, f.readline(),
	# the readline function returns the \n that's in the file at the end of that line
	# so the print function's \n is being added to the one already returned by readline
	# putting the comma at the end suppresses print's \n
	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)
current_line += 1
print_a_line(current_line, current_file)

print