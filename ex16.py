from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER."
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#file_contents = target.read() # you can't read a file if you tell it 'w' in the open line
# the w command tells it that we want to write to the file, but also erases existing contents
# a is append
# r is read
# if no options are given, open just does read mode
# but truncate wasn't working in r+ mode?

# type pydoc open in the command line to see more details

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines of text."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")
# Writes to it twice here

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.write("\n%s\n%s\n%s\n" % (line1, line2, line3))
# the above way is much more succinct, and will be useful for table writing!!

print "And finally, we close it."
target.close()